import streamlit as st
import qrcode
import io
from PIL import Image

st.set_page_config(page_title="Code Combinations Midterm Practice", page_icon="🔢")

# Sidebar QR code
st.sidebar.header("Scan the QR Code")
qr_link = "https://code-combinations.streamlit.app"
qr = qrcode.make(qr_link)
buf = io.BytesIO()
qr.save(buf)
buf.seek(0)
st.sidebar.image(buf, width=250, caption=qr_link)

st.title("Code Combinations – Midterm Practice")

# === Problem 1 ===
st.header("Problem 1")
st.text("Numbers and letters\nUppercase and lowercase letters")
st.markdown("**Code length: 5 characters**")

try:
    problem1_img = Image.open("problem1.png")
    st.image(problem1_img, caption="Problem 1 Code Space", use_column_width=True)
except FileNotFoundError:
    st.warning("⚠️ Image 'problem1.png' not found.")

p1_q1 = st.number_input("8. What characters can make up the code?", min_value=0, step=1)
p1_q2 = st.number_input("9. What sets of characters can the code contain?", min_value=0, step=1)
p1_q3 = st.number_input("10. How many possible characters are there for the first spot in the password?", min_value=0, step=1)
p1_q4 = st.number_input("11. How many possible characters are there for the fifth spot in the password?", min_value=0, step=1)
p1_q5 = st.number_input("12. How many total password combinations are possible?", min_value=0, step=1)

p1_correct = (
    p1_q1 == 62 and
    p1_q2 == 62 and
    p1_q3 == 62 and
    p1_q4 == 62 and
    p1_q5 == 916132832
)

if st.button("Check Problem 1"):
    if p1_correct:
        st.success("✅ Problem 1 is correct.")
    else:
        st.error("❌ Some answers in Problem 1 are incorrect. Please check again.")

# === Problem 2 ===
if p1_correct:
    st.header("Problem 2")
    st.text("Numbers\nCannot repeat characters")
    st.markdown("**Code length: 5 characters**")

    try:
        problem2_img = Image.open("problem2.png")
        st.image(problem2_img, caption="Problem 2 Code Space", use_column_width=True)
    except FileNotFoundError:
        st.warning("⚠️ Image 'problem2.png' not found.")

    p2_q1 = st.number_input("13. What characters can make up the code?", min_value=0, step=1)
    p2_q2 = st.number_input("14. What sets of characters can the code contain?", min_value=0, step=1)
    p2_q3 = st.number_input("15. How many possible characters are there for the first spot in the password?", min_value=0, step=1)
    p2_q4 = st.number_input("16. How many possible characters are there for the fifth spot in the password?", min_value=0, step=1)
    p2_q5 = st.number_input("17. How many total password combinations are possible?", min_value=0, step=1)

    if st.button("Check Problem 2"):
        score = 5  # From Problem 1

        if p2_q1 != 10:
            st.error("❌ Q13 is incorrect.")
            score -= 1
        else:
            st.success("✅ Q13 is correct.")

        if p2_q2 != 10:
            st.error("❌ Q14 is incorrect.")
            score -= 1
        else:
            st.success("✅ Q14 is correct.")

        if p2_q3 != 10:
            st.error("❌ Q15 is incorrect.")
            score -= 1
        else:
            st.success("✅ Q15 is correct.")

        if p2_q4 != 6:
            st.error("❌ Q16 is incorrect.")
            score -= 1
        else:
            st.success("✅ Q16 is correct.")

        if p2_q5 != 30240:
            st.error("❌ Q17 is incorrect.")
            score -= 1
        else:
            st.success("✅ Q17 is correct.")

        st.subheader(f"Final Score: {score} / 10")
        if score == 10:
            st.balloons()
