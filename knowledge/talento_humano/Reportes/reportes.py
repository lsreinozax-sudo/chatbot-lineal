"""Reportes del ERP KAVAC del bien de talento humano"""

def informacion_general_reportes():
    return ("El módulo de talento humano permite generar diversos reportes accediendo con credenciales "
            "de administrador o rol de talento humano. Las opciones se encuentran en la sección 'Reportes' "
            "e incluyen: solicitudes de vacaciones, reportes de trabajadores, conceptos, nómina, "
            "hojas de tiempo, carga familiar y recibos de pago.")

def reporte_solicitudes_vacaciones():
    return ("Permite consultar las solicitudes de vacaciones filtrando por trabajador. Al buscar un registro, "
            "se visualizan los datos en pantalla y se habilita la opción de generar un archivo .pdf "
            "que detalla el código de solicitud, fechas, datos del trabajador, cargo, períodos y días solicitados.")

def reporte_detallado_trabajadores():
    return ("Busca el expediente específico de un trabajador. Permite ver el detalle en pantalla (fechas, cargo, "
            "funciones, etc.) y generar un reporte en .pdf estructurado en cuatro secciones: Información Personal, "
            "Información Socio-económica, Información Profesional e Información Laboral.")

def reporte_trabajadores_con_filtros():
    return ("A diferencia del reporte detallado, esta opción permite combinar múltiples filtros (Datos personales, "
            "profesionales, socioeconómicos y laborales con rangos mínimos y máximos). Al generar el reporte, "
            "el sistema envía un archivo PDF con las coincidencias directamente al correo del usuario que lo solicita.")

def reporte_personal_disfrute_vacaciones():
    return ("Filtra al personal que se encuentra de vacaciones utilizando rangos de fechas ('Desde' y 'Hasta'). "
            "Muestra una tabla con los resultados (Trabajador, ingreso, años, período) y permite generar "
            "un reporte en formato PDF con dicha información.")

def reporte_conceptos():
    return ("Permite listar los conceptos aplicando filtros como 'Nombre del concepto', 'Tipo de concepto' "
            "y 'Tipo de nómina'. El sistema puede generar el reporte tanto en formato .xlsx (Excel) como en .pdf, "
            "mostrando datos contables, presupuestarios, fórmulas y beneficiarios.")

def reporte_relacion_conceptos():
    return ("Genera un archivo PDF con la relación de conceptos aplicados. Se filtra por Tipo de pago, "
            "Tipo de concepto, Concepto, Trabajador y rango de fechas. El documento detalla cédula, "
            "nombre del trabajador, monto del concepto y período.")

def reporte_trabajadores_por_nomina():
    return ("Muestra un reporte visual a partir de los filtros 'Tipo de nómina' y 'Período'. En lugar de un "
            "documento, el sistema genera en pantalla un gráfico de barras donde el eje X muestra las fechas "
            "de corte y el eje Y la cantidad de trabajadores procesados, incluyendo leyendas interactivas.")

def reporte_hoja_de_tiempo():
    return ("Genera un reporte en PDF de la hoja de tiempo del personal. Utiliza parámetros como fechas, "
            "código de grupo, trabajador y estatus. El documento incluye observaciones y detalla los turnos "
            "(tarde, noche) y los subtotales/totales de guardias por trabajador.")

def reporte_carga_familiar():
    return ("Consulta los familiares de un trabajador específico filtrando por 'Trabajador' y 'Parentesco'. "
            "Genera un PDF que incluye los datos laborales del empleado y una tabla detallada con los nombres, "
            "edades, nivel de escolaridad, becas, y discapacidades de su carga familiar.")

def reporte_recibos_de_pago():
    return ("Lista las nóminas configuradas para envío de recibos y filtra por periodos cerrados y trabajador. "
            "Al generar el reporte, el sistema envía los recibos de pago directamente al correo del solicitante, "
            "detallando la información institucional, datos del trabajador, conceptos y montos aplicados.")