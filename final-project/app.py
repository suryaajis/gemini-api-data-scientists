"""
LittleSteps AI — Streamlit App
Baby Growth & Development Assistant
"""

import os
import streamlit as st
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()

# ── Page Config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="LittleSteps AI 🍼",
    page_icon="🍼",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800;900&display=swap');
html, body, [class*="css"] { font-family: 'Nunito', sans-serif !important; }
.ls-header {
    background: linear-gradient(135deg, #FF8FAB 0%, #B794F4 55%, #63B3ED 100%);
    border-radius: 18px; padding: 24px 36px; margin-bottom: 18px;
    text-align: center; box-shadow: 0 8px 30px rgba(159,122,234,0.28);
}
.ls-header h1 { color: #fff; font-size: 2.2rem; font-weight: 900; margin: 0 0 6px 0; }
.ls-header p  { color: rgba(255,255,255,0.95); font-size: 1rem; font-weight: 600; margin: 0; }
.ls-disclaimer {
    background: #FFFBE6; border-radius: 10px; border-left: 5px solid #F6AD55;
    padding: 10px 14px; font-size: 0.82rem; color: #7B4F12;
    font-weight: 600; line-height: 1.5; margin-top: 10px;
}
.ls-footer {
    text-align: center; padding: 16px 0 4px; color: #9B8ABE;
    font-size: 0.78rem; font-weight: 700; letter-spacing: 0.3px;
}
</style>
""", unsafe_allow_html=True)

# ── Milestone Data ────────────────────────────────────────────────────────────
MILESTONES = {
    (0, 1): {
        "title": "Newborn (0–1 Month)", "emoji": "🌸",
        "motor": ["Reflexive movements (rooting, sucking, grasping)", "Turns head side to side when on tummy", "Brings hands near face"],
        "cognitive": ["Focuses on faces 20–30 cm away", "Responds to loud sounds", "Prefers high-contrast patterns"],
        "social": ["Calms with familiar voice or touch", "Brief eye contact"],
        "feeding": "Breastfeed or formula every 2–3 hours (8–12 times/day). No solid foods.",
        "sleep": "16–17 hours/day in short stretches (2–4 hrs). Always back-to-sleep on firm surface.",
        "tips": ["Skin-to-skin contact strengthens bonding", "Talk and sing to your baby — they know your voice!", "Tummy time 3–5 min, 2–3 times/day"],
    },
    (1, 3): {
        "title": "2–3 Months", "emoji": "😊",
        "motor": ["Lifts head and chest during tummy time", "Opens and shuts hands", "Pushes down on legs when feet on flat surface"],
        "cognitive": ["Tracks moving objects with eyes", "Recognizes familiar faces", "Bats at dangling toys"],
        "social": ["Social smiles begin! (6–8 weeks)", "Coos and makes gurgling sounds", "Enjoys playtime"],
        "feeding": "Breast milk or formula every 3–4 hours. Still no solid foods or water.",
        "sleep": "14–16 hours/day. Longer nighttime stretches beginning (3–5 hrs).",
        "tips": ["Introduce a simple bedtime routine: bath, feed, song, sleep", "Read high-contrast picture books!", "Talk about what you're doing"],
    },
    (3, 6): {
        "title": "4–6 Months", "emoji": "🌈",
        "motor": ["Rolls from tummy to back", "Holds head steady without support", "Brings objects to mouth", "Reaches for and grabs objects"],
        "cognitive": ["Curious — looks around at new environments", "Responds to own name (~5–6 months)", "Understands cause and effect"],
        "social": ["Laughs and squeals", "Enjoys social play; mirror play is fascinating", "Recognizes emotions in your voice"],
        "feeding": "Breast milk or formula primary. Around 6 months, can begin iron-rich purées.",
        "sleep": "14–15 hours/day. 2–3 naps. Many can sleep 6+ hour stretches at night.",
        "tips": ["Offer teethers — teething may begin around 4–7 months", "Try peek-a-boo!", "Begin solids with single-ingredient purées"],
    },
    (6, 9): {
        "title": "7–9 Months", "emoji": "🎉",
        "motor": ["Sits without support", "Gets into sitting position independently", "May start crawling or scooting", "Developing pincer grasp"],
        "cognitive": ["Object permanence develops", "Bangs objects together", "Finds partially hidden objects"],
        "social": ["Separation anxiety may begin", "Waves bye-bye", "Babbles ('ba-ba', 'da-da', 'ma-ma')"],
        "feeding": "Expanding variety of purées and mashed foods. Breast milk/formula still primary.",
        "sleep": "12–15 hours. Usually 2 naps. Many sleep through the night.",
        "tips": ["Babyproof your home — mobility is coming!", "Narrate everything!", "Separation anxiety is a healthy developmental sign"],
    },
    (9, 12): {
        "title": "10–12 Months", "emoji": "🚶",
        "motor": ["Pulls to stand and cruises along furniture", "May take first independent steps", "Mature pincer grasp", "Throws objects purposefully"],
        "cognitive": ["Points to objects when named", "Imitates actions and gestures", "Stacks 2 blocks"],
        "social": ["Says 1–2 words with meaning ('mama', 'dada')", "Plays pat-a-cake", "Shows affection to familiar people"],
        "feeding": "Transition toward family foods. Avoid honey, whole cow's milk as main drink, choking hazards.",
        "sleep": "12–14 hours. Transitioning to 1–2 naps.",
        "tips": ["Celebrate the first birthday! 🎂", "Offer finger foods for self-feeding", "Read interactive books with flaps and textures"],
    },
    (12, 18): {
        "title": "12–18 Months (1 Year)", "emoji": "🏃",
        "motor": ["Walking independently", "Climbs onto low furniture", "Uses spoon and fork with help"],
        "cognitive": ["Follows simple 1-step instructions", "Points to 3–6 body parts when asked", "Scribbles with crayon"],
        "social": ["Vocabulary growing to 10–25 words by 18 months", "Parallel play", "Shows strong emotions (tantrums normal)"],
        "feeding": "Whole cow's milk can replace formula. 3 meals + 2 snacks. Variety of family foods.",
        "sleep": "11–14 hours total. Transitioning to 1 nap around 15–18 months.",
        "tips": ["Tantrums are normal — stay calm and validate feelings", "Encourage independence", "Limit screen time; prioritize outdoor exploration"],
    },
    (18, 24): {
        "title": "18–24 Months", "emoji": "🗣️",
        "motor": ["Runs (though often falls)", "Kicks a ball", "Walks up stairs with support", "Builds tower of 4–6 blocks"],
        "cognitive": ["Completes simple shape puzzles", "Understands 'mine' concept", "Pretend play begins"],
        "social": ["50+ words by 24 months; beginning 2-word phrases", "Points to show interesting objects", "Growing independence"],
        "feeding": "3 meals + 2 snacks from family table. Encourage self-feeding. Milk 2–3 cups/day.",
        "sleep": "11–14 hours. One afternoon nap (1–2 hours).",
        "tips": ["Big feelings need big understanding", "Offer controlled choices ('Apple or banana?')", "Toilet training readiness may begin"],
    },
    (24, 36): {
        "title": "2–3 Years", "emoji": "🧒",
        "motor": ["Jumps with both feet", "Pedals a tricycle", "Turns book pages one at a time", "Draws circles and lines"],
        "cognitive": ["Follows 2–3 step instructions", "Sorts objects by shape and color", "Understands 'same' and 'different'"],
        "social": ["200–1000+ word vocabulary", "Sentences of 4–6 words", "Cooperative play", "Starts to understand rules"],
        "feeding": "Family foods. May be picky eater — offer without pressure. 3 meals + 2 snacks.",
        "sleep": "11–13 hours. Nap typically until 3 years.",
        "tips": ["Read together every day!", "Offer consistent routines", "Encourage outdoor play: climbing, running, water play"],
    },
}

QUICK_PROMPTS = [
    "🌟 Apa milestone bayi saya sekarang?",
    "🍼 Kapan mulai MPASI?",
    "😴 Tips meningkatkan kualitas tidur bayi?",
    "🧠 Cara stimulasi otak bayi?",
    "⚖️ Apakah berat badan bayi saya normal?",
    "🦷 Kapan bayi mulai tumbuh gigi?",
]

# ── Helper Functions ──────────────────────────────────────────────────────────
def build_system_prompt(profile: dict) -> str:
    name       = profile.get("name", "your baby")
    age_months = profile.get("age_months")
    gender     = profile.get("gender", "unknown")
    weight_kg  = profile.get("weight_kg")
    height_cm  = profile.get("height_cm")
    age_str    = f"{age_months} months old" if age_months is not None else "age not specified"
    pronoun    = "he" if gender == "Male" else "she" if gender == "Female" else "they"
    pronoun_o  = "him" if gender == "Male" else "her" if gender == "Female" else "them"
    weight_str = f"{weight_kg} kg" if weight_kg else "not recorded"
    height_str = f"{height_cm} cm" if height_cm else "not recorded"
    return f"""You are LittleSteps AI, a warm, caring, and knowledgeable baby development assistant.
You support parents with evidence-based guidance on infant and toddler care.

## Baby Profile
- Name: {name}
- Age: {age_str}
- Gender: {gender} ({pronoun}/{pronoun_o})
- Weight: {weight_str}
- Height: {height_str}

## Your Personality
- Warm, empathetic, and encouraging — like a trusted friend who is also a pediatric expert
- Use the baby's name ({name}) naturally in responses
- Celebrate parents' efforts and normalize challenges
- Use gentle, positive language; never judgmental
- Use relevant emojis sparingly (👶, 🌟, ❤️, 🍼, 😴)

## Key Rules
- Always tailor responses to {name}'s age ({age_str})
- For medical symptoms or health concerns: always recommend consulting a pediatrician
- Never diagnose conditions or prescribe treatments
- If situation sounds urgent, advise seeking emergency care immediately
- Base advice on WHO guidelines and AAP evidence-based practices
- Keep responses conversational — parents are busy!
- When giving milestone info, always mention the typical range

## Response Format
- JAWAB pertanyaan secara LANGSUNG dan LENGKAP terlebih dahulu — jangan tunda dengan preamble panjang
- Sertakan data konkret atau rentang normal jika relevan (misalnya berat, tinggi, milestone)
- Gunakan bullet points atau bagian pendek untuk informasi yang terstruktur
- Tambahkan hangat dan semangat di akhir respons
- Akhiri dengan catatan dorongan atau pertanyaan lanjutan
- Targetkan 200–450 kata; utamakan kelengkapan daripada singkatnya
"""


def get_milestones_for_age(age_months):
    if age_months is None:
        return None
    for (low, high), data in MILESTONES.items():
        if low <= age_months < high:
            return data
    return MILESTONES[(24, 36)] if age_months >= 36 else MILESTONES[(0, 1)]


def format_milestone_card(age_months, baby_name="Your Baby"):
    data = get_milestones_for_age(age_months)
    if not data:
        return "Please enter baby's age to see milestone recommendations."
    lines = [
        f"### {data['emoji']} {baby_name}'s Milestones — {data['title']}", "",
        "**🏃 Motor Development**",
    ]
    for m in data["motor"]: lines.append(f"- {m}")
    lines += ["", "**🧠 Cognitive Development**"]
    for m in data["cognitive"]: lines.append(f"- {m}")
    lines += ["", "**💬 Social & Emotional**"]
    for m in data["social"]: lines.append(f"- {m}")
    lines += ["", f"**🍼 Feeding**", data["feeding"], "", f"**😴 Sleep**", data["sleep"], "", "**💡 Parenting Tips**"]
    for t in data["tips"]: lines.append(f"- {t}")
    lines += ["", "---", "*Every baby develops at their own pace! These are typical ranges, not strict deadlines.*", "*If you have concerns, always consult your pediatrician.* 🩺"]
    return "\n".join(lines)


# ── LittleStepsBot ────────────────────────────────────────────────────────────
class LittleStepsBot:
    MODEL = "gemini-2.5-flash"

    def __init__(self, api_key: str, baby_profile: dict):
        self.api_key      = api_key
        self.baby_profile = baby_profile
        self._client      = None
        self._chat        = None

    def _initialize(self):
        self._client = genai.Client(api_key=self.api_key)
        self._chat   = self._client.chats.create(
            model=self.MODEL,
            config=types.GenerateContentConfig(
                system_instruction=build_system_prompt(self.baby_profile),
                temperature=0.7,
                top_p=0.9,
                max_output_tokens=1500,
            ),
        )

    def update_profile(self, profile: dict):
        self.baby_profile = profile
        self._chat = None

    def reset(self):
        self._chat = None

    def chat(self, message: str) -> str:
        if not message.strip():
            return "Please type your question! I'm here to help. 😊"
        if not self.api_key:
            return "⚠️ API key tidak tersedia. Periksa file .env kamu."
        if self._chat is None:
            self._initialize()
        try:
            response = self._chat.send_message(message)
            return response.text
        except Exception as e:
            err = str(e)
            if "API_KEY_INVALID" in err or "API key not valid" in err:
                return "❌ API key tidak valid. Periksa GEMINI_API_KEY di file .env."
            elif "quota" in err.lower():
                return "⚠️ Kuota API habis. Periksa penggunaan di Google AI Studio."
            elif "safety" in err.lower():
                return "Saya tidak bisa menjawab pertanyaan itu. Coba ulangi dengan kata-kata berbeda. 😊"
            else:
                return f"⚠️ Terjadi error: {err[:200]}. Coba lagi."


# ── Session State ─────────────────────────────────────────────────────────────
for key, default in [
    ("messages", []),
    ("bot", None),
    ("profile_saved", False),
    ("profile", {}),
    ("quick_prompt", None),
]:
    if key not in st.session_state:
        st.session_state[key] = default

# ── API Key (from .env, not shown in UI) ─────────────────────────────────────
api_key = os.getenv("GEMINI_API_KEY", "")
if not api_key:
    st.error("⚠️ GEMINI_API_KEY tidak ditemukan. Tambahkan ke file .env lalu restart app.", icon="🔑")
    st.stop()

# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("## 👶 Profil Bayi")
    baby_name  = st.text_input("Nama Bayi", placeholder="Budi, Sari, Arya...")
    age_months = st.number_input("Usia (bulan)", min_value=0, max_value=48, step=1, value=0)
    gender     = st.selectbox("Jenis Kelamin", ["Prefer not to say", "Male", "Female"])
    col_w, col_h = st.columns(2)
    with col_w:
        weight_kg = st.number_input("Berat (kg)", min_value=0.0, max_value=30.0, step=0.1, value=0.0)
    with col_h:
        height_cm = st.number_input("Tinggi (cm)", min_value=0.0, max_value=120.0, step=0.5, value=0.0)

    if st.button("💾 Simpan Profil & Update AI", use_container_width=True, type="primary"):
        if not baby_name.strip():
            st.warning("Masukkan nama bayi!")
        else:
            profile = {
                "name":       baby_name.strip(),
                "age_months": int(age_months) if age_months else None,
                "gender":     gender,
                "weight_kg":  float(weight_kg) if weight_kg else None,
                "height_cm":  float(height_cm) if height_cm else None,
            }
            st.session_state.profile = profile
            icon = "👦" if gender == "Male" else "👧" if gender == "Female" else "🧒"
            if st.session_state.bot is None:
                st.session_state.bot = LittleStepsBot(api_key, profile)
            else:
                st.session_state.bot.api_key = api_key
                st.session_state.bot.update_profile(profile)
            st.session_state.profile_saved = True
            st.success(f"✅ Profil disimpan! Halo, {baby_name}! {icon}")

    st.divider()
    if st.button("🗑️ Reset Percakapan", use_container_width=True):
        st.session_state.messages = []
        if st.session_state.bot:
            st.session_state.bot.reset()
        st.rerun()

    st.markdown(
        '<div class="ls-disclaimer">'
        "⚕️ <strong>Perhatian Medis:</strong> LittleSteps AI memberikan panduan parenting umum. "
        "Selalu konsultasikan kondisi kesehatan bayi dengan <strong>dokter anak</strong>."
        "</div>",
        unsafe_allow_html=True,
    )

# ── Main Area ─────────────────────────────────────────────────────────────────
st.markdown("""
<div class="ls-header">
    <h1>🍼 LittleSteps AI</h1>
    <p>Asisten Tumbuh Kembang Bayi yang Hangat &amp; Cerdas</p>
</div>
""", unsafe_allow_html=True)

# Milestone expander
profile = st.session_state.profile
if profile and profile.get("age_months"):
    with st.expander(f"🌟 Milestone {profile.get('name','Bayi')} — Usia {profile['age_months']} bulan", expanded=False):
        st.markdown(format_milestone_card(profile["age_months"], profile.get("name", "Bayi")))
elif not st.session_state.profile_saved:
    st.info("👈 Isi profil bayi di sidebar, lalu klik **Simpan Profil** untuk memulai!", icon="🍼")

# Quick prompts
st.markdown("**💬 Pertanyaan Cepat:**")
qcols = st.columns(3)
for i, qp in enumerate(QUICK_PROMPTS):
    if qcols[i % 3].button(qp, key=f"qp_{i}", use_container_width=True):
        st.session_state.quick_prompt = qp

# Handle quick prompt
if st.session_state.quick_prompt:
    injected = st.session_state.quick_prompt
    st.session_state.quick_prompt = None
    if st.session_state.bot:
        st.session_state.messages.append({"role": "user", "content": injected})
        with st.spinner("LittleSteps AI sedang menjawab..."):
            reply = st.session_state.bot.chat(injected)
        st.session_state.messages.append({"role": "assistant", "content": reply})
    else:
        st.warning("Simpan profil bayi terlebih dahulu!", icon="👶")

st.divider()

# Chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"], avatar="👶" if msg["role"] == "assistant" else None):
        st.markdown(msg["content"])

# Chat input
prompt = st.chat_input("Tanyakan apa saja tentang bayi Anda... 💕")
if prompt:
    if st.session_state.bot is None:
        st.warning("Simpan profil bayi terlebih dahulu!", icon="👶")
    else:
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        with st.chat_message("assistant", avatar="👶"):
            with st.spinner("LittleSteps AI sedang menjawab..."):
                reply = st.session_state.bot.chat(prompt)
            st.markdown(reply)
        st.session_state.messages.append({"role": "assistant", "content": reply})

# Footer
st.markdown(
    '<div class="ls-footer">'
    "🍼 LittleSteps AI &nbsp;·&nbsp; Final Project — Maju Bareng AI &nbsp;·&nbsp; "
    "Hacktiv8 × Google.org × AVPN × ADB"
    "</div>",
    unsafe_allow_html=True,
)
