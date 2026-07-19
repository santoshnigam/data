import streamlit as st
st.title("HELLO there")
st.header("HELLO SANTOSH")
st.text_input("Enter your Name")
st.sidebar.title("Menu")
name=st.sidebar.text_input("Enter your gmail")
left, middle, right = st.columns(3)
if left.button("Plain button", width="stretch"):
    left.markdown("You clicked the plain button.")
if middle.button("Emoji button", icon="😃", width="stretch"):
    middle.markdown("You clicked the emoji button.")
if right.button("Material button", icon=":material/mood:", width="stretch"):
    right.markdown("You clicked the Material button.")