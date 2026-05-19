"""Aplicación base del ERP KAVAC sobre monedas"""

def que_muestra_la_pantalla_de_monedas():
    return "Al pulsar el icono monedas, el sistema nos presenta una pantalla que muestra los campos: País, Nombre, Nombre en Plural, Símbolo, Decimales, y a la vez el switch Por defecto que permite que todos los ingresos en el sistema se muestren con el símbolo de la moneda seleccionada por defecto en donde al menos una moneda debe ser seleccionada, ademas presenta los botones Cerrar, Cancelar y Guardar."

def que_campos_tiene_la_tabla_de_monedas():
    return "También nos muestra una tabla de registros con los campos: país, símbolo, nombre, por defecto y acción, que a su vez presenta los botones Modificar y Eliminar."

def que_funcionalidad_tiene_la_tabla_de_monedas():
    return "Esta tabla presenta un campo de búsqueda, el cual nos permite filtrar los registros."

def que_sucede_al_guardar_en_monedas():
    return "Seguidamente, el sistema muestra que el registro se almaceno con éxito, y lo lista en la tabla de registros."

def que_boton_cierra_la_ventana_en_monedas():
    return "Si se desea cerrar la ventana se pulsa cerrar."

def que_boton_restablece_el_formulario_en_monedas():
    return "Si se requiere restablecer los campos del formulario se pulsa el botón Cancelar."

def como_se_edita_un_registro_en_monedas():
    return "Para editar un registro presionamos el botón modificar para un registro de interés, inmediatamente el sistema presenta la información ingresada previamente, se modifica la información que se requiera, y se pulsa Guardar."

def que_mensaje_muestra_al_actualizar_en_monedas():
    return "Luego, el sistema muestra un mensaje de que la información se actualizo con éxito, y se actualiza la tabla de registro."

def como_se_elimina_un_registro_en_monedas():
    return "Para eliminar un registro, pulsamos el botón eliminar para un registro de interés, inmediatamente el sistema presenta un mensaje de confirmación, si presionamos la opción Confirmar, el sistema elimina el registro y muestra un mensaje de que el registro se eliminó con éxito."
