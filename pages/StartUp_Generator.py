import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

# PAGE 
st.set_page_config(
    page_title="Startup Generator · NIC",
    page_icon="🚀",
    layout="wide"
)


GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# HEADER
st.title("🚀 Startup Idea Generator")

st.markdown("Generate complete startup plans using AI")

st.markdown("---")

# LAYOUT
left_col, right_col = st.columns([1, 1.3])

# INPUT SECTION
with left_col:

    st.subheader("Your Inputs")

    problem = st.text_area(
        "Problem you're solving",
        placeholder="e.g. People struggle to find affordable used cars online"
    )

    theme = st.multiselect(
        "Domain / Theme",
        ["SaaS", "AI", "E-commerce", "FinTech", "HealthTech", "EdTech"]
    )

    keywords = st.text_input(
        "Keywords (comma separated)",
        placeholder="mobile, web, AI"
    )

    audience = st.text_input(
        "Target Audience",
        placeholder="students, businesses, consumers"
    )

    stage = st.selectbox(
        "Startup Stage",
        ["Idea", "MVP", "Growth"]
    )

    generate = st.button("🚀 Generate Startup Plan")


# OUTPUT 
with right_col:

    st.subheader("Startup Plan")

    # ── GENERATE RESPONSE ──
    if generate:

        if not problem and not keywords:
            st.warning("Please enter a problem or keywords")
            st.stop()

        client = Groq(api_key=GROQ_API_KEY)

        prompt = f"""
You are a startup expert.

Create a complete startup plan.

Problem: {problem}
Theme: {theme}
Keywords: {keywords}
Audience: {audience}
Stage: {stage}

Return output in markdown with:
- Startup Name
- Elevator Pitch
- Problem
- Solution
- Market
- Business Model
- Revenue
- MVP
- Marketing Strategy
"""

        with st.spinner("Generating startup plan..."):
            try:
                response = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[{"role": "user", "content": prompt}],
                    temperature=0.5
                )

                result = response.choices[0].message.content

                st.session_state["result"] = result

            except Exception as e:
                st.error(f"Error: {e}")

    # ── DISPLAY RESULT (IMPORTANT FIX) ──
    if "result" in st.session_state:
        st.markdown(st.session_state["result"])

    else:
        st.info("Your AI-generated startup plan will appear here.")