ROUTES = [
    # (keyword, modulo, funcion, sugerencias)
    
    # === CIUDADES ===
    ("que muestra la pantalla de ciudades", "knowledge.aplicacion_base.Ciudades.ciudades", "que_muestra_la_pantalla_de_ciudades", [
    "que campos tiene la tabla de ciudades", "que funcionalidades tiene la tabla de ciudades", "que sucede al guardar en ciudades"
    ]),
    ("que campos tiene la tabla de ciudades", "knowledge.aplicacion_base.Ciudades.ciudades", "que_campos_tiene_la_tabla_de_ciudades", [
    "que muestra la pantalla de ciudades", "que funcionalidades tiene la tabla de ciudades"
    ]),
    ("que funcionalidades tiene la tabla de ciudades", "knowledge.aplicacion_base.Ciudades.ciudades", "que_funcionalidades_tiene_la_tabla_de_ciudades", [
    "que campos tiene la tabla de ciudades", "que sucede al guardar en ciudades"
    ]),
    ("que sucede al guardar en ciudades", "knowledge.aplicacion_base.Ciudades.ciudades", "que_sucede_al_guardar_en_ciudades", [
    "que boton cierra la ventana en ciudades", "que boton restablece el formulario en ciudades", "como se modifica un registro en ciudades"
    ]),
    ("que boton cierra la ventana en ciudades", "knowledge.aplicacion_base.Ciudades.ciudades", "que_boton_cierra_la_ventana_en_ciudades", [
    "que sucede al guardar en ciudades", "que boton restablece el formulario en ciudades"
    ]),
    ("que boton restablece el formulario en ciudades", "knowledge.aplicacion_base.Ciudades.ciudades", "que_boton_restablece_el_formulario_en_ciudades", [
    "que sucede al guardar en ciudades", "que boton cierra la ventana en ciudades"
    ]),
    ("como se modifica un registro en ciudades", "knowledge.aplicacion_base.Ciudades.ciudades", "como_se_modifica_un_registro_en_ciudades", [
    "que mensaje muestra al actualizar en ciudades", "como se elimina un registro en ciudades"
    ]),
    ("que mensaje muestra al actualizar en ciudades", "knowledge.aplicacion_base.Ciudades.ciudades", "que_mensaje_muestra_al_actualizar_en_ciudades", [
    "como se modifica un registro en ciudades", "como se elimina un registro en ciudades"
    ]),
    ("como se elimina un registro en ciudades", "knowledge.aplicacion_base.Ciudades.ciudades", "como_se_elimina_un_registro_en_ciudades", [
    "como se modifica un registro en ciudades", "que mensaje muestra al actualizar en ciudades"
    ]),
    ("ciudades", "knowledge.aplicacion_base.Ciudades.ciudades", "que_muestra_la_pantalla_de_ciudades", [
    "que campos tiene la tabla de ciudades", "que funcionalidades tiene la tabla de ciudades", "que sucede al guardar en ciudades", "como se modifica un registro en ciudades", "como se elimina un registro en ciudades"
    ]),
]





