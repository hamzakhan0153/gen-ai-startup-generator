import streamlit as st

# ── PAGE CONFIG ─────────────────────────────
st.set_page_config(
    page_title="NIC AI Startup Generator",
    page_icon="🚀",
    layout="centered"
)

# ── SIMPLE CSS ──────────────────────────────
st.markdown("""
<style>
#MainMenu, footer, header{
    visibility:hidden;
}

.block-container{
    padding-top:2rem;
    max-width:850px;
}

html, body, [class*="css"]{
    background:#0F172A;
    color:white;
    font-family:Arial;
}

/* hero */
.hero{
    text-align:center;
    padding:3rem 1rem;
}

.title{
    font-size:52px;
    font-weight:700;
    margin-bottom:10px;
}

.highlight{
    color:#4F8EF7;
}

.sub{
    color:#94A3B8;
    font-size:18px;
    max-width:600px;
    margin:auto;
    line-height:1.7;
}

/* button */           
.stButton > button{
    width: 100%;
    border:none;
    border-radius:10px;
    background:#4F8EF7;
    color:white;
    padding:14px;
    font-size:18px;
    font-weight:600;
}

.stButton > button:hover{
    background:#3578e5;
}

/* cards */
.card{
    background:#1E293B;
    padding:20px;
    border-radius:12px;
    text-align:center;
    margin-top:15px;
}

.icon{
    font-size:32px;
}

.card-title{
    font-size:18px;
    font-weight:600;
    margin-top:10px;
}

.card-text{
    color:#94A3B8;
    font-size:14px;
}

.footer{
    text-align:center;
    margin-top:60px;
    color:#64748B;
    font-size:13px;
}
</style>
""", unsafe_allow_html=True)

# ── HERO ────────────────────────────────────
st.markdown("""
<div class='hero'>
<div style='font-size:14px;color:#4F8EF7'>
NIC • AI Startup Studio
</div>

<div class='title'>
Turn Ideas Into <span class='highlight'>Startup Plans</span>
</div>

<div class='sub'>
Describe your idea and generate a complete startup blueprint powered by AI in seconds.
</div>
</div>
""", unsafe_allow_html=True)

# ── BUTTON ──────────────────────────────────
c1,c2,c3=st.columns(3)

with c2:
    if st.button("🚀 Generate Startup Plan"):
       st.switch_page("pages/StartUp_Generator.py")

st.markdown("<br>", unsafe_allow_html=True)

# ── FEATURES ────────────────────────────────
c1,c2,c3=st.columns(3)

with c1:
    st.markdown("""
    <div class='card'>
    <div class='icon'>🎯</div>
    <div class='card-title'>Idea to Pitch</div>
    <div class='card-text'>
    Turn problems into startup ideas.
    </div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class='card'>
    <div class='icon'>📊</div>
    <div class='card-title'>Business Model</div>
    <div class='card-text'>
    Generate revenue and market strategy.
    </div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class='card'>
    <div class='icon'>🚀</div>
    <div class='card-title'>MVP Plan</div>
    <div class='card-text'>
    Get roadmap and feature suggestions.
    </div>
    </div>
    """, unsafe_allow_html=True)

# ── FOOTER ──────────────────────────────────
st.markdown("""
<div class='footer'>
Built by Muhammad Hamza • National Incubation Center
</div>
""", unsafe_allow_html=True)