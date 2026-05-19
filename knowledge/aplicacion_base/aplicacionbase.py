"""Aplicación base del ERP KAVAC"""

def  conf_parametros_generales():
    return "En la sección Parámetros generales, puedes gestionar las funcionalidades de la aplicación activando o desactivando opciones mediante los interruptores (switches). En donde encontraras:          " \
    "• Notificaciones: Al activarla el sistema habilita las notificaciones." \
    "• Banner en reportes: La aplicación mostrará un banner en cada reporte generado. " \
    "• Firma electrónica: El sistema habilitará la firma electrónica para todos los procesos."

def registros_comunes():
    return "En la sección Registros comunes, es posible configurar los parámetros clave que se aplican en todo el sistema. A continuación, se detallan las funcionalidades que conforman esta sección:"

def registros_comunes_estatus_documentos():
    return"Al pulsar el icono “Estatus de documentos”, el sistema nos presenta una pantalla con una tabla de registros asociados a los estados de los documentos dentro de los procesos del sistema, la cual  está conformada por  los campos: color, nombre, descripción, ejecuta y accion, que a su vez contiene botones de modificar y eliminar. Esta tabla también presenta un campo de búsqueda, el cual permite filtrar los registros."

def registros_comunes_estatus_civil():
    return "Al pulsar el icono Estados civiles, el sistema presenta una pantalla que muestra el campo nombre, junto con los botones Cerrar, Cancelar y Guardar. También muestra una tabla de registros con  los campos: nombre y acción, que a su vez presenta los botones Modificar y Eliminar."

def registros_comunes_mod_registro():
    return "  Para modificar un registro presionamos el botón modificar para un registro de interés, inmediatamente el sistema presenta la información ingresada previamente, se modifica la información que se requiera, y se pulsa Guardar.  Luego, el sistema muestra un mensaje de que la información se actualizo con éxito, y se actualiza la tabla de registro."

def registros_comunes_estatus_eliminar_registro():
    return "Para eliminar un registro, pulsamos el botón eliminar para un registro de interés, inmediatamente el sistema presenta un mensaje de confirmación, si presionamos la opción Confirmar, el sistema elimina el registro y muestra un mensaje de que el registro se eliminó con éxito."


def que_se_puede_ver_en_la_opcion_de_roles_permisos():
    return "En Roles/Permisos: esta opción muestra todos los roles y permisos con los que cuenta la aplicación"

 
def que_muestra_la_pantalla_de_modulos():
    return "Al hacer clic sobre módulos el sistema presenta una pantalla con todos los módulos del sistema donde se nos indica cuales están instalados o desinstalados."

