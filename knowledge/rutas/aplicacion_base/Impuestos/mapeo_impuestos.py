ROUTES = [
    # (keyword, modulo, funcion, sugerencias)
    
    # === IMPUESTOS ===

    ("que muestra la pantalla de impuestos", "knowledge.aplicacion_base.Impuestos.impuestos", "que_muestra_la_pantalla_de_impuestos", [
    "que campos tiene la tabla de impuestos", "que funcionalidad tiene la tabla de impuestos", "que sucede al guardar en impuestos"
    ]),
    ("que campos tiene la tabla de impuestos", "knowledge.aplicacion_base.Impuestos.impuestos", "que_campos_tiene_la_tabla_de_impuestos", [
    "que muestra la pantalla de impuestos", "que funcionalidad tiene la tabla de impuestos"
    ]),
    ("que funcionalidad tiene la tabla de impuestos", "knowledge.aplicacion_base.Impuestos.impuestos", "que_funcionalidad_tiene_la_tabla_de_impuestos", [
    "que campos tiene la tabla de impuestos", "que sucede al guardar en impuestos"
    ]),
    ("que sucede al guardar en impuestos", "knowledge.aplicacion_base.Impuestos.impuestos", "que_sucede_al_guardar_en_impuestos", [
    "que boton cierra la ventana en impuestos", "que boton restablece el formulario en impuestos", "como se edita un registro en impuestos"
    ]),
    ("que boton cierra la ventana en impuestos", "knowledge.aplicacion_base.Impuestos.impuestos", "que_boton_cierra_la_ventana_en_impuestos", [
    "que sucede al guardar en impuestos", "que boton restablece el formulario en impuestos"
    ]),
    ("que boton restablece el formulario en impuestos", "knowledge.aplicacion_base.Impuestos.impuestos", "que_boton_restablece_el_formulario_en_impuestos", [
    "que sucede al guardar en impuestos", "que boton cierra la ventana en impuestos"
    ]),
    ("como se edita un registro en impuestos", "knowledge.aplicacion_base.Impuestos.impuestos", "como_se_edita_un_registro_en_impuestos", [
    "que mensaje muestra al actualizar en impuestos", "como se elimina un registro en impuestos"
    ]),
    ("que mensaje muestra al actualizar en impuestos", "knowledge.aplicacion_base.Impuestos.impuestos", "que_mensaje_muestra_al_actualizar_en_impuestos", [
    "como se edita un registro en impuestos", "como se elimina un registro en impuestos"
    ]),
    ("como se elimina un registro en impuestos", "knowledge.aplicacion_base.Impuestos.impuestos", "como_se_elimina_un_registro_en_impuestos", [
    "como se edita un registro en impuestos", "que mensaje muestra al actualizar en impuestos"
    ]),
    ("impuestos", "knowledge.aplicacion_base.Impuestos.impuestos", "que_muestra_la_pantalla_de_impuestos", [
    "que campos tiene la tabla de impuestos", "que funcionalidad tiene la tabla de impuestos", "que sucede al guardar en impuestos", "como se edita un registro en impuestos", "como se elimina un registro en impuestos"
    ]),
]