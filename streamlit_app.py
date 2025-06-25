import streamlit as st
import qrcode
import io

st.set_page_config(page_title="Code Combinations Practice", page_icon="🔢")

# Sidebar with QR code
st.sidebar.header("📲 Scan to Access This App")
qr_link = "https://code-combinations.streamlit.app"
qr = qrcode.make(qr_link)
buf = io.BytesIO()
qr.save(buf)
buf.seek(0)
st.sidebar.image(buf, width=250, caption=qr_link)

# Title and image upload
st.title("🧠 Code Combinations Practice (Midterm Style)")

st.markdown("Upload a picture of your worksheet or code space reference:")
uploaded_image = st.file_uploader("Upload Code Space Image", type=["png", "jpg", "jpeg"])
if uploaded_image:
    st.image(uploaded_image, caption="Code Space", use_column_width=True)
else:
    st.info("📸 Add your worksheet image here if needed.")

# --- Problem 1: Repetition allowed, full set of characters ---
st.header("🔢 Problem 1: Letters (upper & lower) and numbers – repetition allowed")

st.markdown("""
**Rules:**  
- Use 0–9, a–z, A–Z  
- Characters can repeat  
- Total possible characters per position = 62
""")

p1_answers = {
    "p1_q1": 62,                   # Total characters (10 + 26 + 26)
    "p1_q2": 62,                   # Same set
    "p1_q3": 62,                   # First character
    "p1_q4": 62,                   # Fifth character
    "p1_q5": 62**5                 # Total combinations
}

# Problem 1 Inputs
user_p1 = {}
for i in range(1, 6):
    user_p1[f"p1_q{i}"] = st.number_input(f"Problem 1 – Question {i}:", min_value=0, step=1, key=f"p1_q{i}")

# --- Problem 2: Numbers only, no repetition ---
st.header("🔢 Problem 2: Numbers only – no repeated characters")

st.markdown("""
**Rules:**  
- Use digits 0–9  
- No repeated characters  
- Total combinations = P(10, 5)
""")

p2_answers = {
    "p2_q1": 10,                  # Total characters
    "p2_q2": 10,                  # Same set
    "p2_q3": 10,                  # First spot
    "p2_q4": 6,                   # Fifth spot (after 4 used)
    "p2_q5": 10 * 9 * 8 * 7 * 6   # Total permutations = 30,240
}

# Problem 2 Inputs
user_p2 = {}
for i in range(1, 6):
    user_p2[f"p2_q{i}"] = st.number_input(f"Problem 2 – Question {i+5}:", min_value=0, step=1, key=f"p2_q{i}")

# --- Check Answers ---
if st.button("✅ Submit Answers"):
    score = 0
    st.subheader("🧾 Results")

    # Check Problem 1
    for i in range(1, 6):
        correct = p1_answers[f"p1_q{i}"]
        user_input = user_p1[f"p1_q{i}"]
        if user_input == correct:
            st.success(f"✅ Problem 1, Question {i}: Correct")
            score += 1
        else:
            st.error(f"❌ Problem 1, Question {i}: Incorrect (Expected {correct})")

    # Check Problem 2
    for i in range(1, 6):
        correct = p2_answers[f"p2_q{i}"]
        user_input = user_p2[f"p2_q{i}"]
        if user_input == correct:
            st.success(f"✅ Problem 2, Question {i+5}: Correct")
            score += 1
        else:
            st.error(f"❌ Problem 2, Question {i+5}: Incorrect (Expected {correct})")

    st.markdown(f"## 🏁 Final Score: {score} / 10")
    if score == 10:
        st.balloons()
        st.success("🎉 Perfect! Great job!")
    elif score >= 7:
        st.info("👍 Good work! Keep practicing.")
    else:
        st.warning("📘 Review your combinations and try again.")

