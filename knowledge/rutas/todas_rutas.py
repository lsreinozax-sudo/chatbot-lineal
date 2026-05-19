"""
Archivo central que combina TODAS las rutas del chatbot.
Solo hay que editar este archivo para añadir/quitar módulos.
"""

# Importar cada módulo con alias único
from knowledge.rutas.mapeo_kavac import ROUTES as KAVAC_ROUTES
from knowledge.rutas.aplicacion_base.mapeo_aplicacion_base import ROUTES as APP_BASE_ROUTES
from knowledge.rutas.aplicacion_base.Barra_Superior.mapeo_BS import ROUTES as BS_ROUTES
from knowledge.rutas.aplicacion_base.Ciudades.mapeo_ciudades import ROUTES as CIUDADES_ROUTES
from knowledge.rutas.aplicacion_base.Conf_Organizacion.mapeo_conf_organizacion import ROUTES as CONF_ROUTES
from knowledge.rutas.aplicacion_base.Deducciones.mapeo_deducciones import ROUTES as DEDUCCIONES_ROUTES
from knowledge.rutas.aplicacion_base.Economicos.mapeo_economicos import ROUTES as ECONOMICOS_ROUTES
from knowledge.rutas.aplicacion_base.Estados.mapeo_estados import ROUTES as ESTADOS_ROUTES
from knowledge.rutas.aplicacion_base.Generos.mapeo_generos import ROUTES as GENEROS_ROUTES
from knowledge.rutas.aplicacion_base.Impuestos.mapeo_impuestos import ROUTES as IMPUESTOS_ROUTES
from knowledge.rutas.aplicacion_base.Monedas.mapeo_monedas import ROUTES as MONEDAS_ROUTES
from knowledge.rutas.aplicacion_base.Municipios.mapeo_municipios import ROUTES as MUNICIPIOS_ROUTES
from knowledge.rutas.aplicacion_base.Organizaciones.mapeo_organizaciones import ROUTES as ORG_ROUTES
from knowledge.rutas.aplicacion_base.Paises.mapeo_paises import ROUTES as PAISES_ROUTES
from knowledge.rutas.aplicacion_base.Parroquias.mapeo_parroquias import ROUTES as PARROQUIAS_ROUTES
from knowledge.rutas.aplicacion_base.Profesion.mapeo_profesion import ROUTES as PROFESION_ROUTES
from knowledge.rutas.aplicacion_base.Sedes.mapeo_sedes import ROUTES as SEDES_ROUTES
from knowledge.rutas.aplicacion_base.Tipos_de_Cambio.mapeo_tipos_de_cambio import ROUTES as TDC_ROUTES
from knowledge.rutas.aplicacion_base.Unidades_Medida.mapeo_unidades_medida import ROUTES as UM_ROUTES
from knowledge.rutas.aplicacion_base.Unidades_o_dependencias.mapeo_unidades_o_dependencias import ROUTES as UOD_ROUTES
from knowledge.rutas.aplicacion_base.Unidades_Tributarias.mapeo_unidades_tributarias import ROUTES as UT_ROUTES
from knowledge.rutas.aplicacion_base.Usuario.mapeo_usuario import ROUTES as USUARIO_ROUTES
from knowledge.rutas.bien_finanzas.Conf_Finanzas.mapeo_conf_finanzas import ROUTES as CONF_FINANZAS_ROUTES
from knowledge.rutas.bien_finanzas.Finanzas_Banco.mapeo_finanzas_banco import ROUTES as FINANZAS_BANCO_ROUTES
from knowledge.rutas.bien_finanzas.Finanzas_Reporte.mapeo_finanzas_reporte import ROUTES as FINANZAS_REPORTE_ROUTES
from knowledge.rutas.bien_finanzas.Gestion_Pagos.mapeo_gestion_pagos import ROUTES as GESTION_PAGOS_ROUTES

# Combinar TODAS las rutas
ALL_ROUTES = (
    KAVAC_ROUTES +
    APP_BASE_ROUTES +
    BS_ROUTES +
    CIUDADES_ROUTES +
    CONF_ROUTES +
    DEDUCCIONES_ROUTES +
    ECONOMICOS_ROUTES +
    ESTADOS_ROUTES +
    GENEROS_ROUTES +
    IMPUESTOS_ROUTES +
    MONEDAS_ROUTES +
    MUNICIPIOS_ROUTES +
    ORG_ROUTES +
    PAISES_ROUTES +
    PARROQUIAS_ROUTES +
    PROFESION_ROUTES +
    SEDES_ROUTES +
    TDC_ROUTES +
    UM_ROUTES +
    UT_ROUTES +
    UOD_ROUTES+
    USUARIO_ROUTES +
    CONF_FINANZAS_ROUTES +
    FINANZAS_BANCO_ROUTES +
    FINANZAS_REPORTE_ROUTES +
    GESTION_PAGOS_ROUTES
)
