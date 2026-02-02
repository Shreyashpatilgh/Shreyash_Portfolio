import streamlit as st
import base64
from pathlib import Path

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="Shreyash Patil | Portfolio",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------- SESSION STATE ----------
if "current_page" not in st.session_state:
    st.session_state.current_page = "Home"
if "show_connect" not in st.session_state:
    st.session_state.show_connect = False

# ---------- PATHS ----------
BASE_DIR = Path(__file__).parent
PROFILE_IMG = BASE_DIR / "imgld.png"
RESUME_PDF = BASE_DIR / "Shreyash_Patil_Resume.pdf"

# ---------- GLOBAL CSS ----------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap');
* { font-family: 'Inter', sans-serif !important; }

#MainMenu, footer { visibility: hidden; }

/* ---------- FULL PAGE BACKGROUND ---------- */
.stApp {
    background: linear-gradient(
        135deg,
        #0f2027,
        #203a43,
        #2c5364
    );
    background-attachment: fixed;
}

/* Content spacing */
.block-container {
    padding-top: 3rem !important;
}

/* ---------- BUTTONS ---------- */
button[kind="primary"] {
    padding: 16px 30px !important;
    border: 2px solid #e91e63 !important;
    border-radius: 30px !important;
    font-weight: 800 !important;
    font-size: 17px !important;
    color: #e91e63 !important;
    background: white !important;
    height: 56px !important;
}

/* ---------- HERO ---------- */
.hero-title {
    font-size: 56px;
    font-weight: 800;
    color: white;
}
.hero-sub {
    font-size: 28px;
    color: #ff4081;
    font-weight: 700;
}
.hero-desc {
    font-size: 20px;
    line-height: 1.8;
    color: #e0e0e0;
}

/* ---------- SECTIONS ---------- */
.section {
    background: rgba(255, 255, 255, 0.96);
    border-radius: 22px;
    padding: 3.5rem;
    margin: 2.5rem 0;
    box-shadow: 0 20px 50px rgba(0,0,0,0.25);
}

.section-title {
    font-size: 42px;
    font-weight: 800;
    text-align: center;
    margin-bottom: 3rem;
    background: linear-gradient(135deg, #e91e63, #c2185b);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

/* ---------- CARDS ---------- */
.card {
    background: #f9fafb;
    border-radius: 18px;
    padding: 2rem;
    margin-bottom: 2rem;
    border-left: 7px solid #e91e63;
}

.card h3 {
    font-size: 24px;
    font-weight: 800;
}

.card p, .card li {
    font-size: 18px;
    line-height: 1.7;
}

/* ---------- PROFILE ---------- */
.profile-img img {
    width: 150px;
    height: 150px;
    border-radius: 50%;
    border: 5px solid #e91e63;
}

/* ---------- RESUME BUTTON ---------- */
.resume-btn {
    padding: 16px 32px;
    border-radius: 14px;
    font-size: 18px;
    font-weight: 700;
    background: linear-gradient(135deg, #e91e63, #c2185b);
    color: white;
    text-decoration: none;
    display: inline-block;
    margin-top: 14px;
}
</style>
""", unsafe_allow_html=True)

# ---------- NAVBAR ----------
pages = ["Home", "Education", "Skills", "Projects", "Certifications"]
cols = st.columns(len(pages))
for i, p in enumerate(pages):
    with cols[i]:
        if st.button(p, use_container_width=True):
            st.session_state.current_page = p
            st.rerun()

# ---------- HOME ----------
if st.session_state.current_page == "Home":
    c1, c2 = st.columns([8, 4])

    with c1:
        st.markdown("""
        <div class="hero-title">Hi, I'm Shreyash Patil</div>
        <div class="hero-sub">Data Scientist | Machine Learning | Gen AI</div>
        <p class="hero-desc">
        Results-driven analytics professional skilled in transforming complex datasets into actionable insights using machine learning, statistical analysis, and data-driven methodologies.
        </p>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown('<div class="profile-img">', unsafe_allow_html=True)
        st.image(PROFILE_IMG)
        st.markdown('</div>', unsafe_allow_html=True)

        with open(RESUME_PDF, "rb") as f:
            b64 = base64.b64encode(f.read()).decode()

        st.markdown(
            f'<a class="resume-btn" href="data:application/pdf;base64,{b64}" download="Shreyash_Patil_Resume.pdf">📄 View Resume</a>',
            unsafe_allow_html=True
        )

        if st.button("🤝 Let's Connect"):
            st.session_state.show_connect = not st.session_state.show_connect
            st.rerun()

        if st.session_state.show_connect:
            st.markdown("""
            <div class="card">
            📧 <b>Email:</b> shreyash1608patil@gmail.com<br><br>
            📞 <b>Phone:</b> +91 74482 31179<br><br>
            <a href="https://www.linkedin.com/in/shreyash-patil-s16/" target="_blank">💼 LinkedIn</a><br><br>
            <a href="https://github.com/Shreyashpatilgh" target="_blank">⭐ GitHub</a>
            </div>
            """, unsafe_allow_html=True)

# ---------- EDUCATION ----------
elif st.session_state.current_page == "Education":
    st.markdown('<div class="section-title">Education</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="card">
    🎓 <h3>MCA – KIT IMER, Kolhapur</h3>
    <p>Pursuing | Expected 2026</p>
    </div>
    <div class="card">
    🎓 <h3>BCA – Shivaji University, Kolhapur</h3>
    <p>2023 | CGPA: 8.3</p>
    </div>
    <div class="card">
    🎓 <h3>HSC – K.M. College, Sarawade</h3>
    <p>2020 | 71.38%</p>
    </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ---------- SKILLS ----------
elif st.session_state.current_page == "Skills":
    st.markdown('<div class="section-title">Professional Skills</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="card">
    <b>Programming:</b> Python, SQL, R<br><br>
    <b>Machine Learning:</b> Predictive Modeling, Model Evaluation<br><br>
    <b>Data Analysis:</b> Data Cleaning, EDA, Feature Engineering<br><br>
    <b>Visualization:</b> Power BI, Matplotlib, Seaborn, Excel<br><br>
    <b>Tools:</b> Streamlit, Git, GitHub, Jupyter Notebook<br><br>
    <b>AI:</b> Generative AI
    </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ---------- PROJECTS ----------
elif st.session_state.current_page == "Projects":
    st.markdown('<div class="section-title">Projects</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
    <h3>Market Sentiment Analysis of Trading Behavior</h3>
    <ul>
        <li>Built end-to-end sentiment-based trading analysis</li>
        <li>Developed predictive models for market trends</li>
        <li>Identified fear–greed patterns affecting price movement</li>
    </ul>
    <b>Tools:</b> Python, Pandas, NumPy, Scikit-learn, Streamlit<br><br>
    <a href="https://github.com/Shreyashpatilgh" target="_blank">🔗 View on GitHub</a>
    </div>

    <div class="card">
    <h3>Analysis of Student’s Social Media Usage</h3>
    <ul>
        <li>Analyzed 5,000+ student responses</li>
        <li>Improved EDA efficiency by 20%</li>
        <li>Identified behavioral patterns impacting academics</li>
    </ul>
    <b>Tools:</b> Python, Pandas, Matplotlib, Seaborn<br><br>
    <a href="https://github.com/Shreyashpatilgh" target="_blank">🔗 View on GitHub</a>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# ---------- CERTIFICATIONS ----------
else:
    st.markdown('<div class="section-title">Certifications</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="card">🏆 <b>IBM Applied Data Science with Python</b><br>Coursera – 2024</div>
    <div class="card">🏆 <b>Machine Learning with Python</b><br>Simplilearn – 2024</div>
    <div class="card">🏆 <b>Introduction to Data Analytics</b><br>Coursera – 2023</div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
