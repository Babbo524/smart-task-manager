
import streamlit as st

st.set_page_config(page_title="Smart Task Manager", layout="wide")

st.title("🧠 Smart Task Manager")
st.markdown("Welcome to your task companion—flexible, simple, and built for real life.")

st.subheader("✅ Today's Task Checklist")
tasks = [
    "Laundry", "Dishes", "Take Meds", "Feed Pet", "Walk Dog",
    "Water Plants", "Exercise", "Clean Bathroom", "Check Email", "Make Bed"
]
for task in tasks:
    st.checkbox(task)

st.text_input("Add your own task:")

st.markdown("---")

st.subheader("📅 Calendar View (Coming Soon)")
st.caption("Daily/weekly planner with task rescheduling.")

st.markdown("---")

with st.expander("🧠 ADHD Support Features"):
    st.markdown("**Need motivation?** Click below.")
    if st.button("I feel stuck"):
        st.info("You’re not lazy. You’re overloaded. Try picking just one small task to start with. 💛")
    st.markdown("**Routine Builder (Coming Soon)**")

st.markdown("---")
st.caption("Powered by W&B Design Co.")
