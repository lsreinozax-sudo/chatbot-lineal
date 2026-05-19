ROUTES = [
    # (keyword, modulo, funcion, sugerencias)
    
    # === PARAMETROS GENERALES ===
    ("parametros generales", "knowledge.aplicacion_base.aplicacionbase", "conf_parametros_generales", [
        "registros comunes base", "que se puede ver en la opcion de roles permisos", "que muestra la pantalla modulos"
    ]),
    ("registros comunes base", "knowledge.aplicacion_base.aplicacionbase", "registros_comunes", [
        "estatus de documentos", "estatus civil", "parametros generales"
    ]),
    ("estatus de documentos", "knowledge.aplicacion_base.aplicacionbase", "registros_comunes_estatus_documentos", [
        "modificar el registro","eliminar","registros comunes base"
    ]),
    ("estatus civil", "knowledge.aplicacion_base.aplicacionbase", "registros_comunes_estatus_civil", [
        "modificar el registro","eliminar","registros comunes base"
    ]),
    ("modificar el registro", "knowledge.aplicacion_base.aplicacionbase", "registros_comunes_mod_registro", [
        "estatus de documentos","estatus civil","registros comunes base"
    ]),
    ("eliminar el registro", "knowledge.aplicacion_base.aplicacionbase", "registros_comunes_estatus_eliminar_registro", [
        "estatus de documentos","estatus civil","registros comunes base"
    ]),
    ("que muestra la pantalla modulos", "knowledge.aplicacion_base.aplicacionbase", "que_muestra_la_pantalla_de_modulos", [
        "parametros generales"
    ]),
    ("que se puede ver en la opcion de roles permisos", "knowledge.aplicacion_base.aplicacionbase", "que_se_puede_ver_en_la_opcion_de_roles_permisos", [
        "parametros generales"
    ]),
]