import streamlit as st
st.title("BMI Calculation")
st.image("b.jpg")
st.markdown("---")

b="""
<style>
.stApp {
  background-image: url("https://cdn1.vectorstock.com/i/1000x1000/69/95/abstract-backgroundblue-triangleabstract-vector-23986995.jpg");
  background-size: cover;
}
</style>
"""

st.html(b)

sex = st.radio("เพศ",("หญิง","ชาย"), horizontal=True)

kg=st.slider('Kgs',10.0,200.0,50.0,0.5)
st.write(kg)
cm=st.slider('cms',10.0,200.0,50.0,0.5)
st.write(cm)

if st.button("calculation"):
    bmi=kg/(t/100)**2
    st.subheader(f"ค่าดัชนีมวลกายของคุณคือ {bmi:.1f}")
    if sex =="หญิง" :
        if bmi < 18.5 :
            st.image("11.jpg")
            st.info("น้ำหนักต่ำกว่าเกณฑ์")
            st.caption("เสี่ยงเป็นโรคขาดสารอาหาร")
        elif bmi < 23 :
            st.image("22.jpg")
            st.success("น้ำหนักสมส่วน")
            st.caption("อาจมีโรคแทรกซ้อนเล็กน้อย")
        elif bmi < 25 :
            st.image("33.jpg")
            st.warning("น้ำหนักเกินเกณฑ์")
            st.caption("ภาวะน้ำหนักเกินระยะเริ่มต้น")
        elif bmi < 30 :
            st.image("44.jpg")
            st.error("น้ำหนักอยู่ในเกณฑ์อ้วน")
            st.caption("ภาวะน้ำหนักเกินมากระยะอ้วนเริ่มต้น")
        elif bmi >= 30 :
            st.image("55.jpg")
            st.error("น้ำหนักอยู่ในเกณฑ์อ้วนมาก")
            st.caption("ภาวะน้ำหนักเกินมากโรคอ้วน")
    else :
        if bmi < 19.5 :
            st.image("1.jpg")
            st.info("น้ำหนักต่ำกว่าเกณฑ์")
            st.caption("เสี่ยงเป็นโรคขาดสารอาหาร")
        elif bmi < 24 :
            st.image("2.jpg")
            st.success("น้ำหนักสมส่วน")
            st.caption("อาจมีโรคแทรกซ้อนเล็กน้อย")
        elif bmi < 26 :
            st.image("3.jpg")
            st.warning("น้ำหนักเกินเกณฑ์")
            st.caption("ภาวะน้ำหนักเกินระยะเริ่มต้น")
        elif bmi < 30 :
            st.image("4.jpg")
            st.error("น้ำหนักอยู่ในเกณฑ์อ้วน")
            st.caption("ภาวะน้ำหนักเกินมากระยะอ้วนเริ่มต้น")
        elif bmi >= 30 :
            st.image("5.jpg")
            st.error("น้ำหนักอยู่ในเกณฑ์อ้วนมาก")
            st.caption("ภาวะน้ำหนักเกินมากโรคอ้วน")
