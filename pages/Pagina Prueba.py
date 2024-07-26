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
    st.write(dato)
    data = json.dumps(dato.__dict__)
    response = requests.post(
        url, 
        json = data, 
        headers = {
            'TokenMisi': TokenMisi 
            }
    )
    
    if(response.status_code == 200):
        st.session_state['listaIDS'] = response

# Obtener archivo
def obtenerArchivo(IDLibro, Inscripcion, Municipio, TokenMisi):
    url = "https://sopaqa.ircnl.gob.mx/serviciosmiportal/api/Visor/obtenerListado_IDLibros"
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
    
    return response

def displayPDF(DatoRegistro):
    resultadoPDF = obtenerArchivo(DatoRegistro)
    # Opening file from file path
    base64_pdf = base64.b64encode(resultadoPDF).decode('utf-8')
    # Embedding PDF in HTML
    pdf_display = F'<embed src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf">'

    # Displaying File
    st.markdown(pdf_display, unsafe_allow_html=True)

if 'listaIDS' not in st.session_state:
    st.session_state['listaIDS'] = []

dato = DatoRegistro('','','','','','')

dato.Anio = st.text_input("Año", "")
dato.Volumen = st.text_input("Volumen", "")
dato.Libro = st.text_input("Libro", "")
dato.Inscripcion = st.text_input("Inscripcion", "")
dato.Municipio = st.text_input("Municipio", "")
dato.Seccion = st.text_input("Seccion", "")

option = st.selectbox(
    "Escoge un ID",
    st.session_state['listaIDS'],
    index=None,
    placeholder="ID",
)

st.title('Pagina de prueba')

st.write("Hola6")
tokenMisi = st.text_input("TokenMisi", "")

st.button("Buscar", type="primary", on_click = obtenerListaIDS, args=[dato, tokenMisi]) 
