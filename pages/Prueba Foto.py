import json
import requests
import streamlit as st

from models.models import ObjDatosAlerta

# Obtener archivo
def obtenerDatosAlerta(hashFolio):
    url = "https://localhost:44337/api/InformativoAlertas/ObtenerDatos_Alerta"
    response = requests.get(
        url, 
        params={
            'hashFolio': hashFolio,
        }
        )
    dump = json.dumps(response.content)
    
    ObjDatosAlerta = json.load(response.content)
    return ObjDatosAlerta

objDatosAlerta = ObjDatosAlerta.__init__()

st.title("Validador de Alerta")


if(st.query_params.__contains__("foliohash")):
    obtenerDatosAlerta(st.query_params["foliohash"])
    st.write("Alerta")

    if(objDatosAlerta != ObjDatosAlerta.__init__()):
        st.write(objDatosAlerta.modeloPrecaptura.id)

else:
    st.write("Pon un folio no seas wey")