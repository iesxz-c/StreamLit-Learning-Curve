import streamlit as st
import pandas as pd
#data elements

st.title("Streamlit Data elemnts")
st.subheader("DataFrame")
df=pd.DataFrame({
    "name": ["Alice", "Bob", "Charlie", "Diana", "Eve"],
    "age": [25, 30, 35, 40, 28],
    "occupation": ["Engineer", "Doctor", "Artist", "Teacher", "Designer"]
})
st.dataframe(df)

st.subheader("Data Editor")
editable_df = st.data_editor(df)

st.subheader("Static Table")
st.table(df)

st.subheader("Metrics")
st.metric(label="Total Rows", value=len(df))
st.metric(label="Average age", value = round(df['age'].mean(),1))

st.subheader("Json and Dictionary")
sampledict ={
    "name": "John",
    "age":25,
    "city":"New York"
    
}
st.json(sampledict)

st.write("Dictionary view ", sampledict)