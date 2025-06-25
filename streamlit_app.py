import streamlit as st
import qrcode
import io
from PIL import Image, ImageDraw

st.set_page_config(page_title="Code Combinations Midterm", page_icon="🔢")

# Sidebar QR Code
st.sidebar.header("Scan the QR Code")
qr_link = "https://code-combinations.streamlit.app"
qr = qrcode.make(qr_link)
buf = io.BytesIO()
qr.save(buf)
buf.seek(0)
st.sidebar.image(buf, width=250, caption=qr_link)

st.title("Code Combinations – Midterm Practice")

# Problem 1
st.header("Problem 1")
st.markdown('''
**Suppose that the five-character code has the following restrictions.**  
**Restrictions:**  
- Numbers and letters  
- Uppercase and lowercase letters  
''')

# Image
st.image("5ch.png")

q1_options = {
    "10 numbers": 10,
    "26 letters": 26,
    "10 numbers and 26 letters": 36,
    "10 numbers and 52 letters": 62
}
q1_answer = 62
q1 = st.radio("1. What characters can make up the code?", list(q1_options.keys()))

q2_options = {
    "a-z (lowercase letters)": 26,
    "A-Z (uppercase letters)": 26,
    "0-9 (numbers)": 10,
    "All of the above": 62
}
q2_answer = 62
q2 = st.radio("2. What sets of characters can the code contain?", list(q2_options.keys()))

q3_options = {
    "60 possible letters and numbers": 60,
    "61 possible letters and numbers": 61,
    "62 possible letters and numbers": 62,
    "59 possible letters and numbers": 59
}
q3_answer = 62
q3 = st.radio("3. How many possible characters are there for the first spot in the password?", list(q3_options.keys()))

q4_options = q3_options
q4_answer = 62
q4 = st.radio("4. How many possible characters are there for the fifth spot in the password?", list(q4_options.keys()))

q5_options = {
    "44,261,653,680 possible combinations": 44261653680,
    "916,132,832 possible combinations": 916132832,
    "776,520,240 possible combinations": 776520240,
    "13,388,280 possible combinations": 13388280
}
q5_answer = 916132832
q5 = st.radio("5. How many total password combinations are possible?", list(q5_options.keys()))

p1_correct = (
    q1_options[q1] == q1_answer and
    q2_options[q2] == q2_answer and
    q3_options[q3] == q3_answer and
    q4_options[q4] == q4_answer and
    q5_options[q5] == q5_answer
)

if st.button("Check Problem 1"):
    if p1_correct:
        st.success("✅ Problem 1 is correct.")
    else:
        st.error("❌ Some answers in Problem 1 are incorrect.")

# Problem 2
if p1_correct:
    st.header("Problem 2")
    st.markdown('''
**Suppose that the five-character code has the following restrictions.**  
**Restrictions:**  
- Numbers only  
- Cannot repeat characters  
''')

    # Image
    st.image("5ch.png")

    q6_options = {
        "10 numbers": 10,
        "26 letters": 26,
        "10 numbers and 26 letters": 36,
        "10 numbers and 52 letters": 62
    }
    q6_answer = 10
    q6 = st.radio("6. What characters can make up the code?", list(q6_options.keys()))

    q7_options = {
        "a-z (lowercase letters)": 26,
        "A-Z (uppercase letters)": 26,
        "0-9 (numbers)": 10,
        "All of the above": 62
    }
    q7_answer = 10
    q7 = st.radio("7. What sets of characters can the code contain?", list(q7_options.keys()))

    q8_options = {
        "52 possible letters and numbers": 52,
        "62 possible letters and numbers": 62,
        "10 possible numbers": 10,
        "9 possible numbers": 9
    }
    q8_answer = 10
    q8 = st.radio("8. How many possible characters are there for the first spot in the password?", list(q8_options.keys()))

    q9_options = {
        "52 possible letters and numbers": 52,
        "62 possible letters and numbers": 62,
        "10 possible numbers": 10,
        "6 possible numbers": 6
    }
    q9_answer = 6
    q9 = st.radio("9. How many possible characters are there for the fifth spot in the password?", list(q9_options.keys()))

    q10_options = {
        "44,261,653,680 possible combinations": 44261653680,
        "380,204,032 possible combinations": 380204032,
        "100,000 possible combinations": 100000,
        "30,240 possible combinations": 30240
    }
    q10_answer = 30240
    q10 = st.radio("10. How many total password combinations are possible?", list(q10_options.keys()))

    if st.button("Check Problem 2"):
        p2_correct = (
            q6_options[q6] == q6_answer and
            q7_options[q7] == q7_answer and
            q8_options[q8] == q8_answer and
            q9_options[q9] == q9_answer and
            q10_options[q10] == q10_answer
        )
        if p2_correct:
            st.success("✅ Problem 2 is correct.")
            st.subheader("Final Score: 10 / 10")
            st.balloons()
        else:
            st.error("❌ Problem 2 is incorrect.")
            st.subheader("Final Score: 5 / 10")
