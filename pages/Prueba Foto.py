import streamlit as st

if st.query_params["foliohash"] != None:
    st.write("Hola.")
else:
    st.write("Pon un folio no seas wey")