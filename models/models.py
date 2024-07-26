from datetime import datetime
from typing import Optional

class DatoRegistro:
    def __init__(self, Volumen:str, Libro:str, Inscripcion:str, Seccion:str, Municipio:str, Anio:str):
        self.Volumen = Volumen
        self.Libro = Libro
        self.Inscripcion = Inscripcion
        self.Seccion = Seccion
        self.Municipio = Municipio
        self.Anio = Anio

class ModeloAlertaCompleta:
    def __init__(self):
        self.id_consecutivo: int = 0
        self.FolioSolicitudPrecaptura: Optional[int] = None
        self.FolioAlertaInmobiliaria: Optional[int] = None
        self.FolioAlertaCatastral: Optional[int] = None
        self.FechaRegistro: Optional[datetime] = None
        self.nota_precaptura: Optional[str] = None
        self.idLibro: Optional[str] = None
        self.FolioAlertaForanea: Optional[int] = None
        self.FolioHash: str = ""

class ModeloPrecaptura:
    def __init__(self):
        self.id: str = ""
        self.AlertaInmobiliaria: bool = False
        self.AlertaCatastral: bool = False
        self.registro_inmobiliaria_volumen: Optional[str] = None
        self.registro_inmobiliaria_libro: Optional[str] = None
        self.registro_inmobiliaria_inscripcion: Optional[str] = None
        self.registro_inmobiliaria_municipio: Optional[str] = None
        self.registro_inmobiliaria_seccion: Optional[str] = None
        self.registro_inmobiliaria_anio: str = ""
        self.datos_solicitante_nombres: Optional[str] = None
        self.datos_solicitante_apellidoPaterno: Optional[str] = None
        self.datos_solicitante_apellidoMaterno: Optional[str] = None
        self.datos_solicitante_CURP: Optional[str] = None
        self.datos_solicitante_razonSocial: Optional[str] = None
        self.datos_solicitante_RFC: str = ""
        self.datos_solicitante_correoPrimario: str = ""
        self.datos_solicitante_correoSecundario: Optional[str] = ""
        self.datos_solicitante_numeroCelular: str = ""
        self.registro_catastral_expedienteCatastral: Optional[str] = None
        self.registro_titular_nombre: Optional[str] = None
        self.registro_titular_curp: Optional[str] = None
        self.EstatusSolicitud: str = "EN REVISIÓN"
        self.UsuarioAprobacion: str = "N/A"
        self.datos_notario_correo: Optional[str] = None
        self.pago_referencia: Optional[str] = None
        self.datos_notario_numeroNotaria: int = -1
        self.datos_precaptura_fechaSolicitud: datetime = datetime.now()
        self.estatus_observacion: Optional[str] = ""
        self.registro_catastral_observacion: str = ""
        self.registro_inmobiliaria_observacion: str = ""
        self.referencia_asociada: Optional[str] = ""
        self.id_notario: Optional[int] = None
        self.registro_folioreal: Optional[str] = None
        self.correo_misi_registrante: Optional[str] = None
        self.id_provisional: Optional[str] = None
        self.datosComprador: Optional['DatosComprador_HerenciaAlerta'] = None
        self.tipoPrecaptura: Optional[str] = ""
        self.FolioFisico: Optional[str] = ""

class DatosComprador_HerenciaAlerta:
    def __init__(self):
        self.id: Optional[int] = None
        self.FolioPrecaptura: Optional[str] = None
        self.datos_solicitante_nombres: str = ""
        self.datos_solicitante_apellidoPaterno: str = ""
        self.datos_solicitante_apellidoMaterno: str = ""
        self.datos_solicitante_CURP: str = ""
        self.datos_solicitante_RFC: str = ""
        self.datos_solicitante_correoPrimario: str = ""
        self.datos_solicitante_correoSecundario: str = ""
        self.datos_solicitante_numeroCelular: str = ""
        self.EstatusSolicitud: str = ""
        self.NuevoDato: str = ""
        self.datos_solicitante_razonSocial: Optional[str] = None
        self.datos_copropietarios: bool = False

class ObjDatosAlerta:
    def __init__(self):
        self.modeloPrecaptura: ModeloPrecaptura = None
        self.modeloAlertaCompleta: ModeloAlertaCompleta = None