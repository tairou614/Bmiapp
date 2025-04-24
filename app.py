import streamlit as st
bg1="""
<style>
.stApp {
 background-color: #FF525F;
 color: #FFFFFF;
 }
 </style>
 """
st.html(bg1)
st.title("BMI Calculation")
st.image("OIP.jpg")
st.markdown("---")
kg=st.number_input("น้ำหนักของคุณ",step=1,min_value=10,max_value=200)
t=st.number_input("ส่วนสูงของคุณ",step=1,min_value=10,max_value=200)
if st.button("calculation"):
    bmi=kg/(t/100)**2
    st.subheader(f"ค่าดัชนีมวลกายของคุณคือ {bmi:.1f}")
    if bmi < 18.5 :
        st.image("1.jpg")
        st.info("น้ำหนักต่ำกว่าเกณฑ์")
        st.caption("เสี่ยงเป็นโรคขาดสารอาหาร")
    elif bmi < 23 :
        st.image("2.jpg")
        st.success("น้ำหนักสมส่วน")
        st.caption("อาจมีโรคแทรกซ้อนเล็กน้อย")
    elif bmi < 25 :
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
      
