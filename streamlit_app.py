import streamlit as st
import qrcode
import io

st.set_page_config(page_title="Code Combinations Midterm", page_icon="🔢")

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

# Question 8
q8_options = {
    "10 numbers": 10,
    "26 letters": 26,
    "10 numbers and 26 letters": 36,
    "10 numbers and 52 letters": 62
}
q8_answer = 62
q8 = st.radio("8. What characters can make up the code?", options=list(q8_options.keys()))

# Question 9
q9_options = {
    "a-z (lowercase letters)": 26,
    "A-Z (uppercase letters)": 26,
    "0-9 (numbers)": 10,
    "All of the above": 62
}
q9_answer = 62
q9 = st.radio("9. What sets of characters can the code contain?", options=list(q9_options.keys()))

# Question 10
q10_options = {
    "60 possible letters and numbers": 60,
    "61 possible letters and numbers": 61,
    "62 possible letters and numbers": 62,
    "59 possible letters and numbers": 59
}
q10_answer = 62
q10 = st.radio("10. How many possible characters are there for the first spot in the password?", options=list(q10_options.keys()))

# Question 11
q11_options = q10_options
q11_answer = 62
q11 = st.radio("11. How many possible characters are there for the fifth spot in the password?", options=list(q11_options.keys()))

# Question 12
q12_options = {
    "44,261,653,680 possible combinations": 44261653680,
    "916,132,832 possible combinations": 916132832,
    "776,520,240 possible combinations": 776520240,
    "13,388,280 possible combinations": 13388280
}
q12_answer = 916132832
q12 = st.radio("12. How many total password combinations are possible?", options=list(q12_options.keys()))

p1_correct = (
    q8_options[q8] == q8_answer and
    q9_options[q9] == q9_answer and
    q10_options[q10] == q10_answer and
    q11_options[q11] == q11_answer and
    q12_options[q12] == q12_answer
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

    # Question 13
    q13_options = q8_options
    q13_answer = 10
    q13 = st.radio("13. What characters can make up the code?", options=list(q13_options.keys()))

    # Question 14
    q14_options = q9_options
    q14_answer = 10
    q14 = st.radio("14. What sets of characters can the code contain?", options=list(q14_options.keys()))

    # Question 15
    q15_options = {
        "52 possible letters and numbers": 52,
        "62 possible letters and numbers": 62,
        "10 possible numbers": 10,
        "9 possible numbers": 9
    }
    q15_answer = 10
    q15 = st.radio("15. How many possible characters are there for the first spot in the password?", options=list(q15_options.keys()))

    # Question 16
    q16_options = {
        "52 possible letters and numbers": 52,
        "62 possible letters and numbers": 62,
        "10 possible numbers": 10,
        "6 possible numbers": 6
    }
    q16_answer = 6
    q16 = st.radio("16. How many possible characters are there for the fifth spot in the password?", options=list(q16_options.keys()))

    # Question 17
    q17_options = {
        "44,261,653,680 possible combinations": 44261653680,
        "380,204,032 possible combinations": 380204032,
        "100,000 possible combinations": 100000,
        "30,240 possible combinations": 30240
    }
    q17_answer = 30240
    q17 = st.radio("17. How many total password combinations are possible?", options=list(q17_options.keys()))

    if st.button("Check Problem 2"):
        score = 5
        correct_answers = {
            13: q13_options[q13] == q13_answer,
            14: q14_options[q14] == q14_answer,
            15: q15_options[q15] == q15_answer,
            16: q16_options[q16] == q16_answer,
            17: q17_options[q17] == q17_answer
        }

        for q_num, correct in correct_answers.items():
            if correct:
                st.success(f"✅ Q{q_num} is correct.")
            else:
                st.error(f"❌ Q{q_num} is incorrect.")
                score -= 1

        st.subheader(f"Final Score: {score} / 10")
        if score == 10:
            st.balloons()
