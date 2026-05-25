"""
LittleSteps AI — Launch with ngrok
Starts Streamlit and creates a public ngrok tunnel.

Usage:
    python run_ngrok.py

Setup (first time):
    1. Sign up at https://ngrok.com (free)
    2. Get your auth token from https://dashboard.ngrok.com/get-started/your-authtoken
    3. Set it below or export it as NGROK_AUTHTOKEN environment variable
"""

import os
import sys
import time
import subprocess
from pyngrok import ngrok, conf

# ── Configuration ─────────────────────────────────────────────────────────────
PORT = 8501
NGROK_AUTH_TOKEN = os.getenv("NGROK_AUTHTOKEN", "")  # set in .env or here directly

# ── Setup ngrok auth ──────────────────────────────────────────────────────────
if NGROK_AUTH_TOKEN:
    conf.get_default().auth_token = NGROK_AUTH_TOKEN
else:
    print("⚠️  NGROK_AUTHTOKEN not set.")
    print("   Get your free token at: https://dashboard.ngrok.com/get-started/your-authtoken")
    print("   Add it to your .env file: NGROK_AUTHTOKEN=your_token_here")
    print("   Proceeding without auth (limited tunnel)...")
    print()

# ── Start Streamlit ───────────────────────────────────────────────────────────
print(f"🚀 Starting Streamlit on port {PORT}...")
streamlit_process = subprocess.Popen(
    [sys.executable, "-m", "streamlit", "run", "app.py",
     "--server.port", str(PORT),
     "--server.headless", "true"],
    cwd=os.path.dirname(os.path.abspath(__file__)),
)

# Wait for Streamlit to be ready
time.sleep(3)

# ── Start ngrok tunnel ────────────────────────────────────────────────────────
print("🌐 Creating ngrok tunnel...")
try:
    tunnel = ngrok.connect(PORT)
    public_url = tunnel.public_url

    print("\n" + "=" * 60)
    print("✅ LittleSteps AI is LIVE!")
    print(f"   🌍 Public URL : {public_url}")
    print(f"   💻 Local URL  : http://localhost:{PORT}")
    print("=" * 60)
    print("\nPress Ctrl+C to stop the server.\n")

    streamlit_process.wait()

except KeyboardInterrupt:
    print("\n\n🛑 Shutting down...")
except Exception as e:
    print(f"\n❌ ngrok error: {e}")
    print(f"   App is still running at: http://localhost:{PORT}")
    try:
        streamlit_process.wait()
    except KeyboardInterrupt:
        pass
finally:
    streamlit_process.terminate()
    ngrok.kill()
    print("👋 Server stopped.")
