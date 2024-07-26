import base64
import streamlit as st
import pandas as pd
import numpy as np
from streamlit import session_state as ss

import requests
import json

from models.models import DatoRegistro

# Replace with the correct URL


def obtenerListaIDS(dato, TokenMisi): 
    url = "https://sopaqa.ircnl.gob.mx/serviciosmiportal/api/Visor/obtenerListado_IDLibros"
    data = json.dumps(dato.__dict__)
    response = requests.post(
        url, 
        json = json.loads(data), 
        headers = {
            'TokenMisi': TokenMisi 
            }
    )
    json_dict = json.loads(response.content)
    st.session_state['listaIDS'] = json_dict

# Obtener archivo
def obtenerArchivo(IDLibro, Inscripcion, Municipio, TokenMisi):
    url = "https://sopaqa.ircnl.gob.mx/serviciosmiportal/api/Visor/obtenerDocumento"
    response = requests.get(
        url, 
        params={
            'IDLibro': IDLibro,
            'Inscripcion' : Inscripcion,
            'Municipio' : Municipio
        }, 
        headers={
            'TokenMisi': TokenMisi
        })
    
    return response.content

def displayPDF(IDLibro, Inscripcion, Municipio, TokenMisi):
    
    resultadoPDF = obtenerArchivo(IDLibro, Inscripcion, Municipio, TokenMisi)
    base64_pdf = base64.b64encode(resultadoPDF).decode("utf-8", 'ignore')
    pdf_display = F'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf"></iframe>'

    # Displaying File
    st.markdown(pdf_display, unsafe_allow_html=True)

st.title('Visor Prueba')


if 'listaIDS' not in st.session_state:
    st.session_state['listaIDS'] = []

dato = DatoRegistro('','','','','','')

dato.Anio = st.text_input("Año", "")
dato.Volumen = st.text_input("Volumen", "")
dato.Libro = st.text_input("Libro", "")
dato.Inscripcion = st.text_input("Inscripcion", "")
dato.Municipio = st.text_input("Municipio", "")
dato.Seccion = st.text_input("Seccion", "")
tokenMisi = st.text_input("TokenMisi", "")
st.button("Buscar", type="primary", on_click = obtenerListaIDS, args=[dato, tokenMisi]) 

option = st.selectbox(
    "Escoge un ID",
    st.session_state['listaIDS'],
    index=None,
    placeholder="ID"
)

st.button("Visualizar", on_click = displayPDF, args=[option, dato.Inscripcion, dato.Municipio, tokenMisi])