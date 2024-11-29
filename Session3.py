import streamlit as st

if "step" not in st.session_state:
    st.session_state.step =1
if "info" not in st.session_state:
    st.session_state.info ={}
    
if st.session_state.step ==1:
    st.header("Part 1 : Info")
    name = st.text_input("Name", value=st.session_state.info.get("name",""))
    if st.button("Next") :
        st.session_state.info["name"] = name
        st.session_state.step = 2
        
elif st.session_state.step ==2:
    st.header("Part 2 : Review")
    st.subheader("PLease review this")
    st.write(f"**Name**: {st.session_state.info.get('name','')}")
    if st.button("Submit"):
        st.success("Great")
        st.balloons()
        st.session_state.info ={}
    if st.button("Back"):
        st.session_state.step =1
        
        
        #the reruns is  a prob
        