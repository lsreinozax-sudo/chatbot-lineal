ROUTES = [
    # (keyword, modulo, funcion, sugerencias)
    
    # === Reportes de Talento Humano ===
    ("informacion general reportes", "knowledge.talento_humano.Reportes.reportes", "informacion_general_reportes", [
        "reporte trabajadores", "solicitudes de vacaciones", "reporte conceptos"
    ]),
    
    ("solicitudes de vacaciones", "knowledge.talento_humano.Reportes.reportes", "reporte_solicitudes_vacaciones", [
        "personal disfrute vacaciones", "reporte detallado trabajadores", "hoja de tiempo"
    ]),
    
    ("reporte detallado trabajadores", "knowledge.talento_humano.Reportes.reportes", "reporte_detallado_trabajadores", [
        "reporte trabajadores", "carga familiar", "hoja de tiempo"
    ]),
    
    ("reporte trabajadores", "knowledge.talento_humano.Reportes.reportes", "reporte_trabajadores_con_filtros", [
        "reporte detallado trabajadores", "trabajadores por nomina", "informacion general reportes"
    ]),
    
    ("personal disfrute vacaciones", "knowledge.talento_humano.Reportes.reportes", "reporte_personal_disfrute_vacaciones", [
        "solicitudes de vacaciones", "reporte detallado trabajadores", "hoja de tiempo"
    ]),
    
    ("reporte conceptos", "knowledge.talento_humano.Reportes.reportes", "reporte_conceptos", [
        "relacion conceptos", "recibos de pago", "trabajadores por nomina"
    ]),
    
    ("relacion conceptos", "knowledge.talento_humano.Reportes.reportes", "reporte_relacion_conceptos", [
        "reporte conceptos", "trabajadores por nomina", "recibos de pago"
    ]),
    
    ("trabajadores por nomina", "knowledge.talento_humano.Reportes.reportes", "reporte_trabajadores_por_nomina", [
        "recibos de pago", "reporte conceptos", "reporte trabajadores"
    ]),
    
    ("hoja de tiempo", "knowledge.talento_humano.Reportes.reportes", "reporte_hoja_de_tiempo", [
        "reporte detallado trabajadores", "solicitudes de vacaciones", "personal disfrute vacaciones"
    ]),
    
    ("carga familiar", "knowledge.talento_humano.Reportes.reportes", "reporte_carga_familiar", [
        "reporte detallado trabajadores", "reporte trabajadores"
    ]),
    
    ("recibos de pago", "knowledge.talento_humano.Reportes.reportes", "reporte_recibos_de_pago", [
        "trabajadores por nomina", "reporte conceptos", "relacion conceptos"
    ]),
]