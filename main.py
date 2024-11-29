import streamlit as st

if "step" not in st.session_state:
    st.session_state.step =1
if "info" not in st.session_state:
    st.session_state.info ={}

def go_to_step2(name):
    st.session_state.info["name"] = name
    st.session_state.step = 2

if st.session_state.step ==1:
    st.header("Part 1 : Info")
    name = st.text_input("Name", value=st.session_state.info.get("name",""))
    st.button("Next",on_click=go_to_step2,args=(name,))
        
### Callback run before any other code on the next rerun




if st.session_state.step ==2:
    st.header("Part 2 : Review")
    st.subheader("PLease review this")
    st.write(f"**Name**: {st.session_state.info.get('name','')}")
    if st.button("Submit"):
        st.success("Great")
        st.balloons()
        st.session_state.info ={}
    if st.button("Back"):
        st.session_state.step =1
        