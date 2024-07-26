import streamlit as st

if(st.query_params.__contains__("foliohash")):
    st.write("Hola.")
else:
    st.write("Pon un folio no seas wey")