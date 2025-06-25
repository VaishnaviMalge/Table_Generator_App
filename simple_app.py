import streamlit as st

def table(n):
        for i in range(1,11):
            st.write(f"{n} x {i} =", i*n)

st.title("Table Generator")
st.subheader("Welcome to Table Generator App.")
st.text("We are here to help you in your studies.")
st.markdown('<span style="color:violet;"> *In this app you can enter any number and by just a simple click you will get a table of that number*</span>',unsafe_allow_html=True)


n = st.number_input("Enter a Number:", step=1,value=1)

if st.button("Create a Table"):
    st.write(f"Table of {n}:\n")    
    table(n)
    st.write("We are here to support you in your learning journey.")
    st.write("Feel free to visit us again😊")


