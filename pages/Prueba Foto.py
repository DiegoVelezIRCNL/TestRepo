import datetime
import json
from time import strftime
import requests
import streamlit as st
import dateutil.parser

from models.models import ObjDatosAlerta

# Obtener archivo
def obtenerDatosAlerta(hashFolio):
    objDatosAlerta: ObjDatosAlerta = None
    url = "https://sopaqa.ircnl.gob.mx/serviciosmiportal/api/InformativoAlertas/ObtenerDatos_Alerta"
    response = requests.get(
        url, 
        params={
            'hashFolio': hashFolio,
        }
        )
    if(response.status_code == 200):
        objDatosAlerta = response.json()
    else:
        objDatosAlerta = None
    return objDatosAlerta

objDatosAlerta: ObjDatosAlerta = None

st.title("Validador de Alerta")


if(st.query_params.__contains__("foliohash")):
    objDatosAlerta = obtenerDatosAlerta(st.query_params["foliohash"])
    
    if(objDatosAlerta != None):

        fechaInicio = dateutil.parser.isoparse(objDatosAlerta["modeloAlertaCompleta"]["fechaRegistro"])

        st.header("Datos de la Alerta Completa:")
        
        st.write("Folio Alerta Inmobiliaria: ", objDatosAlerta["modeloAlertaCompleta"]["folioAlertaInmobiliaria"])
        st.write("Folio Alerta Catastral: ", objDatosAlerta["modeloAlertaCompleta"]["folioAlertaCatastral"])
        st.write("Folio Alerta Foranea: ", objDatosAlerta["modeloAlertaCompleta"]["folioAlertaForanea"])
        st.write("Fecha Inicio: ", fechaInicio)
        st.write("Aprobado por: ", objDatosAlerta["modeloPrecaptura"]["usuarioAprobacion"])

        st.header("Datos de la Precaptura:") 
        st.write("Folio Precaptura: ", objDatosAlerta["modeloPrecaptura"]["id"]) 
        st.write("Correo Primario: ", objDatosAlerta["modeloPrecaptura"]["datos_solicitante_correoPrimario"])
        st.write("Correo Secundario: ", objDatosAlerta["modeloPrecaptura"]["datos_solicitante_correoSecundario"])
        st.write("Correo Registrante: ", objDatosAlerta["modeloPrecaptura"]["correo_misi_registrante"])
        st.write("Teléfono: ", objDatosAlerta["modeloPrecaptura"]["datos_solicitante_numeroCelular"])
          
else:
    st.write("Indica un folio")