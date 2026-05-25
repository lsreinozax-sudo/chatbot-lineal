ROUTES = [


    ("registros de nomina", "knowledge.seccion_registros_nomina_th.talento_humano_registros_nomina", "registros_nomina_pantalla_inicial", [
        "crear registro nomina", "tabla registros nomina"
    ]),
    ("crear registro nomina", "knowledge.seccion_registros_nomina_th.talento_humano_registros_nomina", "registros_nomina_crear_formulario_campos", [
        "registros de nomina", "parametros nomina", "botones formulario nomina", "campo obligatorio nomina"
    ]),
    ("parametros nomina", "knowledge.seccion_registros_nomina_th.talento_humano_registros_nomina", "registros_nomina_parametros_informacion_general", [
        "crear registro nomina", "botones formulario nomina"
    ]),
    ("campo obligatorio nomina", "knowledge.seccion_registros_nomina_th.talento_humano_registros_nomina", "registros_nomina_campo_obligatorio", [
        "crear registro nomina", "guardar registro nomina"
    ]),
    ("botones formulario nomina", "knowledge.seccion_registros_nomina_th.talento_humano_registros_nomina", "registros_nomina_botones_formulario", [
        "crear registro nomina", "guardar registro nomina"
    ]),
    ("guardar registro nomina", "knowledge.seccion_registros_nomina_th.talento_humano_registros_nomina", "registros_nomina_guardar_exito", [
        "botones formulario nomina", "notificaciones ejecucion nomina", "acciones registro nomina"
    ]),
    ("notificaciones ejecucion nomina", "knowledge.seccion_registros_nomina_th.talento_humano_registros_nomina", "registros_nomina_notificaciones_ejecucion", [
        "guardar registro nomina", "flujo exito nomina"
    ]),
    ("flujo exito nomina", "knowledge.seccion_registros_nomina_th.talento_humano_registros_nomina", "registros_nomina_flujo_exito", [
        "notificaciones ejecucion nomina", "generar archivo xlsx", "generar reporte presupuestario", "solicitar disponibilidad", "cerrar registro nomina"
    ]),
    ("generar archivo xlsx", "knowledge.seccion_registros_nomina_th.talento_humano_registros_nomina", "registros_nomina_generar_archivo_xlsx", [
        "flujo exito nomina", "hojas adicionales xlsx", "modificar registro nomina"
    ]),
    ("hojas adicionales xlsx", "knowledge.seccion_registros_nomina_th.talento_humano_registros_nomina", "registros_nomina_archivo_xlsx_hojas_adicionales", [
        "generar archivo xlsx"
    ]),
    ("generar reporte presupuestario", "knowledge.seccion_registros_nomina_th.talento_humano_registros_nomina", "registros_nomina_generar_reporte_presupuestario", [
        "flujo exito nomina", "modificar registro nomina"
    ]),
    ("modificar registro nomina", "knowledge.seccion_registros_nomina_th.talento_humano_registros_nomina", "registros_nomina_modificar_registro", [
        "generar archivo xlsx", "generar reporte presupuestario", "acciones registro nomina"
    ]),
    ("solicitar disponibilidad", "knowledge.seccion_registros_nomina_th.talento_humano_registros_nomina", "registros_nomina_solicitar_disponibilidad", [
        "flujo exito nomina", "completar disponibilidad presupuesto"
    ]),
    ("completar disponibilidad presupuesto", "knowledge.seccion_registros_nomina_th.talento_humano_registros_nomina", "registros_nomina_completar_disponibilidad_presupuesto", [
        "solicitar disponibilidad", "aprobar registro nomina"
    ]),
    ("aprobar registro nomina", "knowledge.seccion_registros_nomina_th.talento_humano_registros_nomina", "registros_nomina_aprobar_registro", [
        "completar disponibilidad presupuesto", "cerrar registro nomina"
    ]),
    ("cerrar registro nomina", "knowledge.seccion_registros_nomina_th.talento_humano_registros_nomina", "registros_nomina_cerrar_registro", [
        "aprobar registro nomina", "apertura siguiente periodo", "no modificable cerrado", "cierre con orden pago", "cierre sin orden pago"
    ]),
    ("apertura siguiente periodo", "knowledge.seccion_registros_nomina_th.talento_humano_registros_nomina", "registros_nomina_apertura_siguiente_periodo", [
        "cerrar registro nomina"
    ]),
    ("no modificable cerrado", "knowledge.seccion_registros_nomina_th.talento_humano_registros_nomina", "registros_nomina_no_modificable_cerrado", [
        "cerrar registro nomina"
    ]),
    ("cierre con orden pago", "knowledge.seccion_registros_nomina_th.talento_humano_registros_nomina", "registros_nomina_cierre_con_orden_pago", [
        "cerrar registro nomina", "cierre sin orden pago"
    ]),
    ("cierre sin orden pago", "knowledge.seccion_registros_nomina_th.talento_humano_registros_nomina", "registros_nomina_cierre_sin_orden_pago", [
        "cerrar registro nomina", "cierre con orden pago"
    ]),
    ("enviar recibos", "knowledge.seccion_registros_nomina_th.talento_humano_registros_nomina", "registros_nomina_enviar_recibos", [
        "acciones registro nomina", "cerrar registro nomina"
    ]),
    ("acciones registro nomina", "knowledge.seccion_registros_nomina_th.talento_humano_registros_nomina", "registros_nomina_guardar_exito", [
        "guardar registro nomina", "generar archivo xlsx", "generar reporte presupuestario", "modificar registro nomina", "solicitar disponibilidad", "aprobar registro nomina", "cerrar registro nomina", "enviar recibos"
    ]),
    ("tabla registros nomina", "knowledge.seccion_registros_nomina_th.talento_humano_registros_nomina", "registros_nomina_pantalla_inicial", [
        "registros de nomina", "crear registro nomina"
    ]),
]