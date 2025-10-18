import streamlit as st

st.title("🔢 Simple Numpad")


if "number" not in st.session_state:
    st.session_state.number = ""


st.text_input("Number:", st.session_state.number, key="display", disabled=True)


buttons = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    ["*", 0, "#"]
]


for row in buttons:
    cols = st.columns(3)
    for i, val in enumerate(row):
        if cols[i].button(str(val)):
            st.session_state.number += str(val)
            st.rerun()


c1, c2, c3 = st.columns(3)
if c1.button("Clear"):
    st.session_state.number = ""
    st.rerun()
if c2.button("Back"):
    st.session_state.number = st.session_state.number[:-1]
    st.rerun()
if c3.button("Enter"):
    st.success(f"You entered: {st.session_state.number}")
