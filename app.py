
import streamlit as st
import joblib
from pathlib import Path

# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="Cyber Shield | SMS Threat Detector",
    page_icon="🛡️",
    layout="wide"
)

# ================= LOAD MODEL =================
@st.cache_resource
def load_model():
    model_path = Path(__file__).parent / "spam_model.pkl"
    return joblib.load(model_path)

try:
    model = load_model()
except Exception as e:
    st.error("Unable to load the trained model.")
    st.code(str(e))
    st.stop()

# ================= CUSTOM CSS =================
st.markdown("""
<style>
.stApp {
    background:
        radial-gradient(circle at 10% 10%, #172554 0%, transparent 30%),
        radial-gradient(circle at 90% 10%, #312e81 0%, transparent 28%),
        linear-gradient(135deg, #070b18, #0d1428 55%, #11152b);
    color: #f8fafc;
}

.block-container {
    max-width: 1150px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

header[data-testid="stHeader"] {
    background: transparent;
}

.hero {
    text-align: center;
    padding: 35px 15px;
    border: 1px solid rgba(99, 102, 241, 0.4);
    border-radius: 22px;
    background: linear-gradient(120deg,
        rgba(30, 41, 80, 0.85),
        rgba(20, 25, 55, 0.85));
    box-shadow: 0 0 35px rgba(59, 130, 246, 0.15);
    margin-bottom: 30px;
}

.hero-tag {
    color: #67e8f9;
    font-size: 12px;
    font-weight: 800;
    letter-spacing: 4px;
}

.hero h1 {
    color: white;
    font-size: clamp(30px, 5vw, 48px);
    font-weight: 850;
    margin: 12px 0;
}

.hero p {
    color: #b8c4e8;
    font-size: 16px;
}

.section-title {
    color: #e0e7ff;
    font-size: 22px;
    font-weight: 800;
    margin: 25px 0 15px;
}

.info-card {
    background: rgba(19, 28, 55, 0.9);
    border: 1px solid rgba(129, 140, 248, 0.3);
    border-radius: 16px;
    padding: 20px;
    min-height: 120px;
    box-shadow: 0 8px 25px rgba(0,0,0,0.2);
}

.info-label {
    color: #9caed4;
    font-size: 12px;
    letter-spacing: 1px;
}

.info-value {
    color: #ffffff;
    font-size: 25px;
    font-weight: 850;
    margin-top: 10px;
}

.info-note {
    color: #67e8f9;
    font-size: 12px;
    margin-top: 5px;
}

.result-card {
    border-radius: 18px;
    padding: 24px;
    margin: 20px 0;
    background: rgba(15, 23, 42, 0.95);
}

.spam-card {
    border: 1px solid #fb7185;
    box-shadow: 0 0 25px rgba(244, 63, 94, 0.15);
}

.ham-card {
    border: 1px solid #34d399;
    box-shadow: 0 0 25px rgba(16, 185, 129, 0.15);
}

.result-title {
    font-size: 25px;
    font-weight: 850;
    margin-bottom: 10px;
}

.result-description {
    color: #cbd5e1;
    font-size: 14px;
}

div.stButton > button {
    width: 100%;
    min-height: 48px;
    border: 1px solid #6366f1;
    border-radius: 12px;
    color: white;
    font-weight: 800;
    background: linear-gradient(90deg, #2563eb, #7c3aed);
    transition: 0.2s;
}

div.stButton > button:hover {
    border-color: #67e8f9;
    box-shadow: 0 0 20px rgba(34, 211, 238, 0.35);
    color: white;
}

div[data-testid="stTextArea"] textarea {
    background: #111a31;
    color: white;
    border: 1px solid #475569;
    border-radius: 13px;
}

div[data-testid="stTextArea"] textarea:focus {
    border: 1px solid #22d3ee;
    box-shadow: 0 0 12px rgba(34, 211, 238, 0.2);
}

.footer {
    text-align: center;
    color: #8492b8;
    font-size: 12px;
    padding: 25px 5px;
    border-top: 1px solid rgba(129, 140, 248, 0.2);
    margin-top: 40px;
}
</style>
""", unsafe_allow_html=True)

# ================= HEADER =================
st.markdown("""
<div class="hero">
    <div class="hero-tag">🛡️ CYBER SHIELD • AI SECURITY SYSTEM</div>
    <h1>SMS THREAT DETECTOR</h1>
    <p>Intelligent Machine Learning System for SMS Spam Detection</p>
    <div class="hero-tag" style="letter-spacing:2px;">
        ● SYSTEM STATUS: ONLINE
    </div>
</div>
""", unsafe_allow_html=True)

# ================= DASHBOARD METRICS =================
st.markdown(
    '<div class="section-title">⚡ SYSTEM OVERVIEW</div>',
    unsafe_allow_html=True
)

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
    <div class="info-card">
        <div class="info-label">MODEL ACCURACY</div>
        <div class="info-value">96.05%</div>
        <div class="info-note">Test dataset result</div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="info-card">
        <div class="info-label">ML ALGORITHM</div>
        <div class="info-value" style="font-size:21px;">Naive Bayes</div>
        <div class="info-note">Multinomial classifier</div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="info-card">
        <div class="info-label">FEATURE EXTRACTION</div>
        <div class="info-value">TF-IDF</div>
        <div class="info-note">Text vectorization</div>
    </div>
    """, unsafe_allow_html=True)

# ================= SMS SCANNER =================
st.markdown(
    '<div class="section-title">🔍 SCAN YOUR SMS MESSAGE</div>',
    unsafe_allow_html=True
)

st.write(
    "Enter an SMS message below to analyze it using our machine learning model."
)

samples = {
    "Select a sample": "",
    "Spam Example": "Congratulations! You won a free iPhone. Click here to claim your prize now!",
    "Genuine Example": "Hey, are you coming to college tomorrow? We have a practical class at 10 AM."
}

selected_sample = st.selectbox(
    "TRY A SAMPLE MESSAGE",
    list(samples.keys())
)

load_col, clear_col = st.columns(2)

with load_col:
    if st.button("📩 LOAD SAMPLE"):
        st.session_state["sms_input"] = samples[selected_sample]
        st.rerun()

with clear_col:
    if st.button("🧹 CLEAR"):
        st.session_state["sms_input"] = ""
        st.session_state.pop("last_sms", None)
        st.session_state.pop("last_prediction", None)
        st.rerun()

sms = st.text_area(
    "MESSAGE INPUT",
    key="sms_input",
    height=150,
    placeholder="Paste or type your SMS message here..."
)

if st.button("🛡️ ANALYZE MESSAGE"):
    if not sms.strip():
        st.warning("Please enter an SMS message before scanning.")
    else:
        prediction = model.predict([sms])[0]

        st.session_state["last_sms"] = sms
        st.session_state["last_prediction"] = int(prediction)

# ================= RESULT =================
if "last_prediction" in st.session_state:

    prediction = st.session_state["last_prediction"]
    scanned_sms = st.session_state["last_sms"]

    st.markdown(
        '<div class="section-title">📊 SCAN RESULT</div>',
        unsafe_allow_html=True
    )

    if prediction == 1:
        st.markdown("""
        <div class="result-card spam-card">
            <div class="result-title" style="color:#fb7185;">
                🚨 SPAM MESSAGE DETECTED
            </div>
            <div class="result-description">
                This message has been classified as potential spam.
                Be careful before clicking links or sharing personal information.
            </div>
        </div>
        """, unsafe_allow_html=True)

    else:
        st.markdown("""
        <div class="result-card ham-card">
            <div class="result-title" style="color:#34d399;">
                ✅ HAM MESSAGE DETECTED
            </div>
            <div class="result-description">
                This message has been classified as genuine by the AI model.
                Always verify unexpected requests independently.
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("**SCANNED MESSAGE**")
    st.info(scanned_sms)

    # Class probabilities
    if hasattr(model, "predict_proba"):
        try:
            probabilities = model.predict_proba([scanned_sms])[0]
            classes = list(model.classes_)

            spam_index = classes.index(1)
            ham_index = classes.index(0)

            spam_probability = float(probabilities[spam_index])
            ham_probability = float(probabilities[ham_index])

            p1, p2 = st.columns(2)

            with p1:
                st.metric(
                    "Spam Probability",
                    f"{spam_probability * 100:.2f}%"
                )
                st.progress(spam_probability)

            with p2:
                st.metric(
                    "Ham Probability",
                    f"{ham_probability * 100:.2f}%"
                )
                st.progress(ham_probability)

            st.caption(
                "Probabilities are model estimates, not guarantees."
            )

        except Exception:
            st.caption("Probability details are unavailable.")

# ================= HOW IT WORKS =================
st.markdown(
    '<div class="section-title">⚙️ HOW THE SYSTEM WORKS</div>',
    unsafe_allow_html=True
)

h1, h2, h3 = st.columns(3)

with h1:
    st.markdown("""
    <div class="info-card">
        <div class="info-value">01</div>
        <b>SMS INPUT</b>
        <p class="info-note">User enters a message for analysis.</p>
    </div>
    """, unsafe_allow_html=True)

with h2:
    st.markdown("""
    <div class="info-card">
        <div class="info-value">02</div>
        <b>TF-IDF PROCESSING</b>
        <p class="info-note">Text is converted into numerical features.</p>
    </div>
    """, unsafe_allow_html=True)

with h3:
    st.markdown("""
    <div class="info-card">
        <div class="info-value">03</div>
        <b>AI PREDICTION</b>
        <p class="info-note">Naive Bayes predicts Spam or Ham.</p>
    </div>
    """, unsafe_allow_html=True)

# ================= FOOTER =================
st.markdown("""
<div class="footer">
    <b>CYBER SHIELD | SMS THREAT DETECTOR</b><br><br>
    IML Mini Project • Machine Learning Based SMS Classification<br>
    Built with Python, Streamlit, TF-IDF and Multinomial Naive Bayes<br><br>
    ⚠️ This tool provides an automated prediction, not a guarantee.
    Always verify suspicious messages independently.
</div>
""", unsafe_allow_html=True)
