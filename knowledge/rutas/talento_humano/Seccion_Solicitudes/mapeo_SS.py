ROUTES = [
    # (keyword, modulo, funcion, sugerencias)
    
    # === SOLICITUDES ===
    ("tipos de solicitudes", "knowledge.talento_humano.Seccion_Solicitudes.solicitudes", "que_tipos_de_solicitudes_existen", [
        "quienes pueden gestionar solicitudes", "requisitos previos solicitudes", "menu de solicitudes"
    ]),
    ("quienes pueden gestionar solicitudes", "knowledge.talento_humano.Seccion_Solicitudes.solicitudes", "quienes_pueden_gestionar_solicitudes", [
        "tipos de solicitudes", "requisitos previos solicitudes", "ingresar al modulo talento humano"
    ]),
    ("requisitos previos solicitudes", "knowledge.talento_humano.Seccion_Solicitudes.solicitudes", "cuales_son_los_requisitos_previos", [
        "tipos de solicitudes", "quienes pueden gestionar solicitudes", "ingresar al modulo talento humano"
    ]),
    ("ingresar al modulo talento humano", "knowledge.talento_humano.Seccion_Solicitudes.solicitudes", "como_ingresar_al_modulo_talento_humano", [
        "menu de solicitudes", "tipos de solicitudes", "quienes pueden gestionar solicitudes"
    ]),
    ("menu de solicitudes", "knowledge.talento_humano.Seccion_Solicitudes.solicitudes", "como_acceder_al_menu_de_solicitudes", [
        "tipos de solicitudes", "ingresar al modulo talento humano", "requisitos previos solicitudes"
    ]),

    # ==========================================
    # SOLICITUD DE ARC
    # ==========================================
    ("buscar solicitud arc", "knowledge.talento_humano.Seccion_Solicitudes.solicitudes", "como_buscar_solicitud_arc", [
        "ver detalle arc", "descargar planilla arc"
    ]),
    ("ver detalle arc", "knowledge.talento_humano.Seccion_Solicitudes.solicitudes", "como_ver_detalle_registro_arc", [
        "buscar solicitud arc", "descargar planilla arc"
    ]),
    ("descargar planilla arc", "knowledge.talento_humano.Seccion_Solicitudes.solicitudes", "como_descargar_o_enviar_planilla_arc", [
        "buscar solicitud arc", "ver detalle arc"
    ]),

    # ==========================================
    # SOLICITUD DE VACACIONES
    # ==========================================
    ("pantalla solicitud vacaciones", "knowledge.talento_humano.Seccion_Solicitudes.solicitudes", "que_contiene_pantalla_solicitud_vacaciones", [
        "crear solicitud vacaciones", "importar vacaciones"
    ]),
    ("crear solicitud vacaciones", "knowledge.talento_humano.Seccion_Solicitudes.solicitudes", "como_crear_solicitud_vacaciones", [
        "modificar solicitud vacaciones", "ver detalle vacaciones"
    ]),
    ("importar vacaciones", "knowledge.talento_humano.Seccion_Solicitudes.solicitudes", "como_importar_registros_vacaciones", [
        "crear solicitud vacaciones", "pantalla solicitud vacaciones"
    ]),
    ("ver detalle vacaciones", "knowledge.talento_humano.Seccion_Solicitudes.solicitudes", "como_ver_detalle_solicitud_vacaciones", [
        "modificar solicitud vacaciones", "aprobar solicitud vacaciones"
    ]),
    ("modificar solicitud vacaciones", "knowledge.talento_humano.Seccion_Solicitudes.solicitudes", "como_modificar_solicitud_vacaciones", [
        "crear solicitud vacaciones", "eliminar solicitud vacaciones"
    ]),
    ("aprobar solicitud vacaciones", "knowledge.talento_humano.Seccion_Solicitudes.solicitudes", "como_aprobar_solicitud_vacaciones", [
        "rechazar solicitud vacaciones", "ver detalle vacaciones"
    ]),
    ("rechazar solicitud vacaciones", "knowledge.talento_humano.Seccion_Solicitudes.solicitudes", "como_rechazar_solicitud_vacaciones", [
        "aprobar solicitud vacaciones", "eliminar solicitud vacaciones"
    ]),
    ("eliminar solicitud vacaciones", "knowledge.talento_humano.Seccion_Solicitudes.solicitudes", "como_eliminar_solicitud_vacaciones", [
        "modificar solicitud vacaciones", "crear solicitud vacaciones"
    ]),
    ("suspender vacaciones", "knowledge.talento_humano.Seccion_Solicitudes.solicitudes", "como_suspender_vacaciones", [
        "replanificar vacaciones", "ver detalle vacaciones"
    ]),
    ("replanificar vacaciones", "knowledge.talento_humano.Seccion_Solicitudes.solicitudes", "como_replanificar_vacaciones", [
        "suspender vacaciones", "modificar solicitud vacaciones"
    ]),

    # ==========================================
    # SOLICITUD DE PRESTACIONES
    # ==========================================
    ("requisitos prestaciones", "knowledge.talento_humano.Seccion_Solicitudes.solicitudes", "requisitos_y_pantalla_prestaciones", [
        "crear solicitud prestaciones", "revisar prestaciones"
    ]),
    ("crear solicitud prestaciones", "knowledge.talento_humano.Seccion_Solicitudes.solicitudes", "como_crear_solicitud_prestaciones", [
        "modificar prestaciones", "ver detalle prestaciones"
    ]),
    ("ver detalle prestaciones", "knowledge.talento_humano.Seccion_Solicitudes.solicitudes", "como_ver_detalle_prestaciones", [
        "modificar prestaciones", "revisar prestaciones"
    ]),
    ("modificar prestaciones", "knowledge.talento_humano.Seccion_Solicitudes.solicitudes", "como_modificar_prestaciones", [
        "eliminar prestaciones", "crear solicitud prestaciones"
    ]),
    ("eliminar prestaciones", "knowledge.talento_humano.Seccion_Solicitudes.solicitudes", "como_eliminar_prestaciones", [
        "modificar prestaciones", "revisar prestaciones"
    ]),
    ("revisar prestaciones", "knowledge.talento_humano.Seccion_Solicitudes.solicitudes", "como_revisar_prestaciones", [
        "requisitos prestaciones", "ver detalle prestaciones"
    ]),

    # ==========================================
    # SOLICITUD DE PERMISOS
    # ==========================================
    ("requisitos permisos", "knowledge.talento_humano.Seccion_Solicitudes.solicitudes", "requisitos_y_pantalla_permisos", [
        "crear solicitud permisos", "aprobar permisos"
    ]),
    ("crear solicitud permisos", "knowledge.talento_humano.Seccion_Solicitudes.solicitudes", "como_crear_solicitud_permisos", [
        "modificar permisos", "ver detalle permisos"
    ]),
    ("ver detalle permisos", "knowledge.talento_humano.Seccion_Solicitudes.solicitudes", "como_ver_detalle_permisos", [
        "modificar permisos", "aprobar permisos"
    ]),
    ("modificar permisos", "knowledge.talento_humano.Seccion_Solicitudes.solicitudes", "como_modificar_permisos", [
        "eliminar permisos", "crear solicitud permisos"
    ]),
    ("aprobar permisos", "knowledge.talento_humano.Seccion_Solicitudes.solicitudes", "como_aprobar_permisos", [
        "rechazar permisos", "ver detalle permisos"
    ]),
    ("rechazar permisos", "knowledge.talento_humano.Seccion_Solicitudes.solicitudes", "como_rechazar_permisos", [
        "aprobar permisos", "eliminar permisos"
    ]),
    ("eliminar permisos", "knowledge.talento_humano.Seccion_Solicitudes.solicitudes", "como_eliminar_permisos", [
        "modificar permisos", "crear solicitud permisos"
    ])
]