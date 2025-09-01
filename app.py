import streamlit as st
import pandas as pd
import numpy as np
import random

from numpy.ma.core import min_val

#-------------------- App Config ---------------------------
st.set_page_config(page_title="Mini Streamlit App", layout="wide")

#--------------------- Header -------------------------------
st.title("Mini Streamlit App")
st.write("Welcome! This is a small and attractive app built with Streamlit")

#---------------------- Navigation --------------------------
st.sidebar.header("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Form", "Data Viz", "Fun Zone"])

# ---------------------- Home --------------------------------
if page == "Home":
    st.subheader("Welcome Page")
    st.image("https://streamlit.io/images/brand/streamlit-mark-color.png", width=150)
    st.write("This is mini app demonstrates forms, charts, and fun features using streamlit!")

# ----------------------- FORM -----------------------------------
elif page == "Form":
    st.subheader("User Information Form")
    with st.form("user_form"):
        name = st.text_input("Enter your name")
        age = st.number_input("Enter your age", min_value=1, max_value= 100, step=1)
        mood = st.selectbox("How are you feeling today?", ["😊 Happy", "😴 Tired", "🤔 Curious", "🔥 Excited"])
        submitted = st.form_submit_button("Submit")

        if submitted:
            st.success(f"Hello **{name}**! You are {age} years old and feeling {mood} today.")

# ----------------------- Data Viz ------------------------------------
elif page == "Data Viz":
    st.subheader("Random Data Visualization")
    data = pd.DataFrame(np.random.randn(20,3), columns=['A','B','C'])
    st.line_chart(data)
    st.bar_chart(data)

# ------------------------ Fun Zone -------------------------------------
elif page == "Fun Zone":
    st.subheader("Random Motivational Quote")
    quotes = [
        "Believe in yourself! 🌟",
        "Every day is a second chance. 💪",
        "Stay positive, work hard, make it happen. 🚀",
        "Dream big, start small, act now. ✨"
    ]
    st.success(random.choice(quotes))


