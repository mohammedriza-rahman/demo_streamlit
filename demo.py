## importing the library
import streamlit as st

## creating a title with streamlit

st.title("hello! world")

st.header("this is a header")

st.subheader("this is a subheader")

st.text("this is a text")

st.markdown("this is a markdown")

## taking the users inputs 

# in text

name = st.text_input("this is a text input")

st.sidebar.header(f"hello ! {name}")

## number input

number= st.number_input("this is a number input")


# st.write(f"my name is {name} and my age is {Age}")

## radio input

gender= st.radio("select gender",["male","female"])


## slider option

Age= st.slider("select age",0,100)

## dropdown option

city= st.selectbox("select city",["bangalore","mumbai","chennai","hyderabad"])


if st.button("submit"):
    st.balloons()
    st.write(f"my name is {name} and my age is {Age} i am {gender} and i live in {city}")

