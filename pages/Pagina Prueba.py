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
    data = json(dato)
    st.write(data)
    response = requests.post(
        url, 
        json = data, 
        headers = {
            'TokenMisi': TokenMisi 
            }
    )
    return response

# Obtener archivo
def obtenerArchivo(IDLibro, Inscripcion, Municipio, TokenMisi):
    url = "https://sopaqa.ircnl.gob.mx/serviciosmiportal/api/Visor/obtenerListado_IDLibros"
    data = json(DatoRegistro)
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

listaIDS = ()

dato = DatoRegistro('','','','','','')

dato.Anio = st.text_input("Año", "")
dato.Volumen = st.text_input("Volumen", "")
dato.Libro = st.text_input("Libro", "")
dato.Inscripcion = st.text_input("Inscripcion", "")
dato.Municipio = st.text_input("Municipio", "")
dato.Seccion = st.text_input("Seccion", "")

option = st.selectbox(
    "Escoge un ID",
    listaIDS
)

st.title('Pagina de prueba')

st.write("Hola6")
tokenMisi = st.text_input("TokenMisi", "")

st.button("Buscar", type="primary", on_click = obtenerListaIDS, args=[dato, tokenMisi]) 
