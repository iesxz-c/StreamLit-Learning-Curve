import streamlit as st

## Session  States ------------- Dynamic Forms  

# Session state is a dictionary that is stored in memory for the duration of the session.
# It can be used to store data that needs to be remembered between function calls.
# Session state is not persisted across sessions, so it will be lost when the user closes the browser
# or when the app is restarted.

# ss is smth taht we can use to store values within the same user session
# per session is per refresh of the trab or per reload of the tab or the webpage

if "counter" not in st.session_state:
    #if counter is in the session
    st.session_state.counter = 0
# st.session_state.counter = 0
st.write(f"Counter value: {st.session_state.counter}")
if st.button("Increment Counter"):
    st.session_state.counter += 1
    st.write(f"Counter increment to {st.session_state.counter}")
if st.button("Reset"):
    st.session_state.counter = 0
else:
    st.write(f"Counter is not reset")

#here the counetr lacks behind the incrementer by 1 
    
                  