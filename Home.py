import time
import numpy as np
import pandas as pd
import streamlit as st

def stream_data(text):
    for word in text.split(" "):
        yield word + " "
        time.sleep(0.02)

    yield pd.DataFrame(
        np.random.randn(5, 10),
        columns=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"],
    )

    for word in text.split(" "):
        yield word + " "
        time.sleep(0.02)

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Portal de datos chidos. ")

st.write_stream(stream_data(
    """
    Hola me llamo Diego y soy bien chingon
    """
))
    

