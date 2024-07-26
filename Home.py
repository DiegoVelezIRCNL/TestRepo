import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Portal de datos chidos. ")

st.write_stream(
    """
    Hola me llamo Diego y soy bien chingon
"""
)
