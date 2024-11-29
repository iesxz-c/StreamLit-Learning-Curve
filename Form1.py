import streamlit as st
from datetime import datetime
#FORM

st.title("User Info")
st.write("Please fill in the form below to submit your user information")

fo ={
    "Name": None,
    "Age": None,
    "Gender": None,
    "DOB":None,
    "Height":None,
}
min=datetime(1990,1,1)
max=datetime.now()
with st.form(key="user_info"):
    
    fo["Name"] = st.text_input("Enter your Name: ")
    fo["Age"] = st.number_input("Enter your Age: ")
    fo["Height"] = st.number_input("Enter your Height: ")
    fo["Gender"] = st.selectbox("Select your Gender: ", ["Male", "Female"])
    fo["DOB"] = st.date_input("Enter your Date of Birth: ",max_value=max,min_value=min)
    
    
    
    su = st.form_submit_button(label="submit") #this willl run at first --- first it will will be false 
    # then it will run again ---  becomes true
    
    if su:
        if not all(fo.values()):
            st.warning("Please fill in all the fields")
        else:
            st.balloons()
            st.write("### Info")
            for key, value in fo.items():
                st.write(f"{key}: {value}")
                         