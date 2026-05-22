"""
AI Agents with LangGraph
Part 1 — SQL Agent
Part 2 — BaristaBot

Requirements:
    pip install langgraph langchain-google-genai python-dotenv

Setup:
    Copy .env.example to .env and set GEMINI_API_KEY=your_key
"""

import os
import sqlite3
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import InMemorySaver

load_dotenv()
os.environ["GOOGLE_API_KEY"] = os.getenv("GEMINI_API_KEY", "")

# ══════════════════════════════════════════════════════════════════════════════
# PART 1 — SQL AGENT
# ══════════════════════════════════════════════════════════════════════════════

db_file = "sample.db"


def setup_database():
    """Create and populate the sample SQLite database."""
    with sqlite3.connect(db_file) as conn:
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS products (
                product_id   INTEGER PRIMARY KEY AUTOINCREMENT,
                product_name VARCHAR(255) NOT NULL,
                price        DECIMAL(10, 2) NOT NULL
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS staff (
                staff_id   INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name VARCHAR(255) NOT NULL,
                last_name  VARCHAR(255) NOT NULL
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS orders (
                order_id      INTEGER PRIMARY KEY AUTOINCREMENT,
                customer_name VARCHAR(255) NOT NULL,
                staff_id      INTEGER NOT NULL,
                product_id    INTEGER NOT NULL,
                FOREIGN KEY (staff_id)   REFERENCES staff (staff_id),
                FOREIGN KEY (product_id) REFERENCES products (product_id)
            )
        """)

        cursor.execute("SELECT COUNT(*) FROM products")
        if cursor.fetchone()[0] == 0:
            cursor.executemany(
                "INSERT INTO products (product_name, price) VALUES (?, ?)",
                [("Laptop", 799.99), ("Keyboard", 129.99), ("Mouse", 29.99)],
            )
            cursor.executemany(
                "INSERT INTO staff (first_name, last_name) VALUES (?, ?)",
                [("Alice", "Smith"), ("Bob", "Johnson"), ("Charlie", "Williams")],
            )
            cursor.executemany(
                "INSERT INTO orders (customer_name, staff_id, product_id) VALUES (?, ?, ?)",
                [("David Lee", 1, 1), ("Emily Chen", 2, 2), ("Frank Brown", 1, 3)],
            )

        conn.commit()


setup_database()


# ── SQL Tools ─────────────────────────────────────────────────────────────────

def list_tables() -> list[str]:
    """Retrieve the names of all tables in the database."""
    print(" - DB CALL: list_tables")
    with sqlite3.connect(db_file) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        return [t[0] for t in cursor.fetchall()]


def describe_table(table_name: str) -> list[tuple[str, str]]:
    """Look up the table schema.

    Returns:
        List of (column_name, column_type) tuples.
    """
    print(" - DB CALL: describe_table")
    with sqlite3.connect(db_file) as conn:
        cursor = conn.cursor()
        cursor.execute(f"PRAGMA table_info({table_name});")
        return [(col[1], col[2]) for col in cursor.fetchall()]


def execute_query(sql: str) -> list[list[str]]:
    """Execute a SELECT statement, returning the results."""
    print(" - DB CALL: execute_query")
    with sqlite3.connect(db_file) as conn:
        cursor = conn.cursor()
        cursor.execute(sql)
        return cursor.fetchall()


# ── Build SQL Agent ───────────────────────────────────────────────────────────

db_tools = [list_tables, describe_table, execute_query]

sql_instruction = """You are a helpful chatbot that can interact with an SQL database for a computer
store. You will take the users questions and turn them into SQL queries using the tools
available. Once you have the information you need, you will answer the user's question using
the data returned. ALWAYS start by calling list_tables to discover the available tables.
ALWAYS call describe_table on the relevant table before writing any SQL query.
Never assume or guess table names or column names — always verify first."""

sql_model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite", temperature=0)

sql_agent = create_react_agent(
    model=sql_model,
    tools=db_tools,
    prompt=sql_instruction,
)


def ask_sql_agent(question: str) -> str:
    response = sql_agent.invoke(
        {"messages": [{"role": "user", "content": question}]}
    )
    return response["messages"][-1].content


# ══════════════════════════════════════════════════════════════════════════════
# PART 2 — BARISTABOT
# ══════════════════════════════════════════════════════════════════════════════

barista_instruction = """
You are a BaristaBot, an interactive cafe ordering system.
A human will talk to you about the available products you have and you will answer any questions
about menu items (and only about menu items - no off-topic discussion, but you can chat about the
products and their history). The customer will place an order for 1 or more items from the menu,
which you will structure and send to the ordering system after confirming the order with the human.

Add items to the customer's order with add_to_order, and reset the order with clear_order.
To see the contents of the order so far, call get_order (this is shown to you, not the user).
Always confirm_order with the user (double-check) before calling place_order.
Calling confirm_order will display the order items to the user and returns their response to seeing
the list. Their response may contain modifications. Always verify and respond with drink and modifier
names from the MENU before adding them to the order.
If you are unsure a drink or modifier matches those on the MENU, ask a question to clarify or redirect.
You only have the modifiers listed on the menu.
Once the customer has finished ordering items, call confirm_order to ensure it is correct then make
any necessary updates and then call place_order.
Once place_order has returned, thank the user and say goodbye!
"""

customer_order: list[str] = []


def get_menu() -> str:
    """Provide the latest up-to-date menu."""
    return """
    MENU:
    Coffee Drinks:
    Espresso, Americano, Cold Brew

    Coffee Drinks with Milk:
    Latte, Cappuccino, Cortado, Macchiato, Mocha, Flat White

    Tea Drinks:
    English Breakfast Tea, Green Tea, Earl Grey

    Tea Drinks with Milk:
    Chai Latte, Matcha Latte, London Fog

    Other Drinks:
    Steamer, Hot Chocolate

    Modifiers:
    Milk options: Whole, 2%, Oat, Almond, 2% Lactose Free; Default: Whole
    Espresso shots: Single, Double, Triple, Quadruple; Default: Double
    Caffeine: Decaf, Regular; Default: Regular
    Hot-Iced: Hot, Iced; Default: Hot
    Sweeteners: vanilla sweetener, hazelnut sweetener, caramel sauce, chocolate sauce, sugar free vanilla sweetener

    "dirty" means add a shot of espresso to a drink that doesn't usually have it.
    "Regular milk" is the same as whole milk.
    Soy milk is not available today.
    """


def add_to_order(item: str) -> str:
    """Add an item to the customer's order."""
    global customer_order
    customer_order.append(item)
    print(f"Adding '{item}' to order. Current: {customer_order}")
    return f"I've added '{item}' to your order."


def clear_order() -> str:
    """Clear all items from the customer's order."""
    global customer_order
    customer_order.clear()
    print("Order cleared.")
    return "Your order has been cleared."


def get_order() -> list[str]:
    """Get the current items in the customer's order."""
    global customer_order
    print(f"Getting order: {customer_order}")
    return customer_order


def confirm_order() -> str:
    """Confirm the order with the customer."""
    global customer_order
    if not customer_order:
        return "Your order is currently empty. What can I get for you?"
    return f"Your order contains: {', '.join(customer_order)}. Is this correct?"


def place_order() -> str:
    """Place the final order."""
    global customer_order
    if not customer_order:
        return "There's nothing in your order to place."
    summary = ", ".join(customer_order)
    customer_order.clear()
    return f"Your order for '{summary}' has been placed! It will be ready shortly."


# ── Build BaristaBot ──────────────────────────────────────────────────────────

barista_tools = [get_menu, add_to_order, clear_order, get_order, confirm_order, place_order]

barista_model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite", temperature=0.2)
checkpointer = InMemorySaver()

barista_agent = create_react_agent(
    model=barista_model,
    tools=barista_tools,
    prompt=barista_instruction,
    checkpointer=checkpointer,
)


def chat_with_barista():
    """Interactive CLI session with BaristaBot."""
    thread_id = "1"
    config = {"configurable": {"thread_id": thread_id}}

    print("Welcome to BaristaBot! Type 'q' to quit.\n")

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in ("q", "quit", "exit"):
            print("BaristaBot: Thank you for visiting! Have a great day!")
            break

        response = barista_agent.invoke(
            {"messages": [{"role": "user", "content": user_input}]},
            config=config,
        )
        print(f"BaristaBot: {response['messages'][-1].content}\n")


# ══════════════════════════════════════════════════════════════════════════════
# MAIN — Demo
# ══════════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    print("=" * 60)
    print("PART 1 — SQL Agent")
    print("=" * 60)

    q1 = "Siapa saja orang yang terdaftar di database ini?"
    print(f"\nUser: {q1}")
    print(f"Agent: {ask_sql_agent(q1)}\n")

    q2 = "Barang apa yang dijual di toko ini dan berapa harganya?"
    print(f"User: {q2}")
    print(f"Agent: {ask_sql_agent(q2)}\n")

    print("=" * 60)
    print("PART 2 — BaristaBot (Interactive)")
    print("=" * 60)
    chat_with_barista()
