def periodo_activo_pantalla_inicial():
    return "Pulsamos la opción periodo activo, y enseguida el sistema muestra una pantalla denominada “Hoja de tiempo”, que contiene una tabla con las siguientes columnas: Periodo, Código, Supervisor, Aprobador, Estatus y Acción que contiene las opciones de Ver, Aprobar, Confirmar, Rechazar Modificar y Eliminar Registro. Además se muestran los botones para “Ir atrás” y “Crear nuevo registro”."

def periodo_activo_crear_formulario_campos():
    return "Pulsamos el botón “Crear nuevo registro” y el sistema presenta un formulario con los siguientes campos: Desde y Hasta, Código de grupo de supervisados, el cual enlista los códigos de los grupos supervisados que han sido registrados previamente, Parámetros de la hoja de tiempo que enlista los códigos de las hojas de tiempo previamente configuradas."

def periodo_activo_botones_formulario():
    return "Este formulario también, presenta los botones: Cancelar y regresar, que permite salir del formulario, Borrar datos del formulario que permite limpiar el formulario, Y guardar que realiza la acción de almacenar los datos que se ingresan."

def periodo_activo_campos_generados():
    return "Al llenar los campos, el sistema procede a mostrarnos estos nuevos: Supervisor, este campo es generado por el sistema una vez que se indique el código del grupo de supervisados. Aprobador, que es un campo generado por el sistema una vez se indique el código del grupo de supervisados."

def periodo_activo_tabla_parametros():
    return "Una vez que el usuario indique información en los campos Código de grupo de supervisados y en el campo Parámetros de la hoja de tiempo, el sistema muestra una tabla con las columnas: N°, Ficha, Nombre, y las columnas asociadas a los diferentes parámetros configurados previamente en parámetros globales como Turno Tarde Y Turno Noche, y a su vez por cada tipo de parámetro de tiempo el sistema debe mostrar una columna de subtotal, y la columna de total la cual muestra la sumatoria de los subtotales."

def periodo_activo_campo_obligatorio():
    return "Es importante mencionar que los campos en los que se detalla un asterisco rojo, son de tipo obligatorio y omitirlo, generará una alerta indicando que debe ingresar el mismo."

def periodo_activo_guardar_exito():
    return "Luego, ingresamos la información solicitada y pulsamos guardar para que el sistema almacene la información. El sistema al realizar el registro nos muestra el mensaje: “Registro almacenado con éxito”, y lo enlista en la tabla anteriormente mencionada, donde la columna Acción contiene los botones para Ver registro, Aprobar registro, Confirmar registro, Rechazar registro, Modificar registro y Eliminar registro."

def periodo_activo_importar_exportar():
    return "A la vez podemos Importar y Exportar los archivos necesarios."

def periodo_activo_alimentacion_esquema_guardias():
    return "Es importante precisar que el registro de hoja de tiempo en la opción periodo activo, se puede alimentar del esquema de guardias siempre que correspondan con el periodo de la hoja de tiempo en periodo activo, tomando el ingreso de parámetros de manera automática de los valores del esquema de guardias."

def periodo_activo_estatus_elaborado():
    return "Una vez ingresado un registro de hoja de tiempo, este toma el estatus Elaborado."

def periodo_activo_carga_masiva():
    return "Esta funcionalidad como se puede detallar también cuenta con carga masiva, para esto se recomienda descargar el archivo a fin de obtener la estructura del mismo, realizar las cargas de información en este, para posteriormente realizar el proceso de importación de data."

def periodo_activo_ver_registro():
    return "Para visualizar la información previamente ingresada, pulsamos el botón “Ver registro”, para una hoja de tiempo de interés, y seguidamente el sistema muestra una ventana denominada “Información Detallada de la Hoja de Tiempo” que contiene información relevante de la hoja de tiempo, tal como: Desde, Hasta, Código grupo de supervisados, Supervisor, Aprobador, Estatus, Observaciones y la tabla de Registros que muestra la lista de trabajadores con los respectivos valores ingresados en donde se enlista en un formulario que tiene: N°, Ficha, Nombre, Turno tarde, Turno Noche, Subtotal- guardias para cada parámetro de tiempo. Para cerrar esta ventana pulsamos sobre el icono X o el botón “Cerrar”."

def periodo_activo_aprobar_registro():
    return "Para aprobar un registro de hoja de tiempo, pulsamos sobre el botón Aprobar para un registro de interés, enseguida el sistema muestra el siguiente mensaje ¿Está seguro? Una vez aprobado el registro no se podrá eliminar, junto con las opciones: “No” y “Si”. Si presionamos la opción No, el sistema no ejecuta ninguna acción. En caso de que seleccionemos la opción Si, el sistema muestra el mensaje de notificación “Hoja de tiempo aprobada correctamente”, y el estatus del registro cambia a aprobado, se desactiva el botón eliminar y el sistema notifica vía correo al supervisor correspondiente que el registro fue aprobado y se activan los botones “Confirmar registro” y “Rechazar registro”."

def periodo_activo_rechazar_registro():
    return "Para rechazar un registro de hoja de tiempo se requiere que este posea el estatus aprobado, entonces el pulsamos el botón Rechazar para un registro de interés, luego el sistema muestra una ventana denominada ¿Rechazar hoja de tiempo?, donde solicita que se ingrese información en el campo observaciones junto con las opciones: “Si” y “No”. Ingresamos la información solicitada y pulsamos Si, y el sistema cambia el estatus del registro a rechazado(a). En caso de que de que pulsemos No, el sistema no ejecuta ninguna acción."

def periodo_activo_confirmar_registro():
    return "Para confirmar un registro de hoja de tiempo se requiere que este posea el estatus aprobado, así al pulsar la opción confirmar para un registro de interés, el sistema muestra el siguiente mensaje ¿Está seguro? Una vez confirmado el registro no se podrá modificar, junto con las opciones: “Si” y “No”. En caso de que presionemos la opción Si, el sistema muestra el mensaje “Hoja de tiempo confirmada correctamente”, y cambia el estatus del registro a “Cerrado (a). Una vez confirmado un registro de hoja de tiempo en periodo activo, el sistema bloquea el botón Modificar. En caso de que pulsemos la opción No, el sistema no realiza ninguna acción."

def periodo_activo_modificar_registro():
    return "En caso de que se requiera modificar la información ingresada previamente, presionamos sobre la opción modificar registro para el registro de hoja de tiempo de interés, y se edita la información que se requiera, seguidamente ya pulsamos guardar y el sistema muestra el mensaje: “Registro actualizado con éxito”."

def periodo_activo_eliminar_registro():
    return "En caso de que se requiera eliminar el registro previamente ingresado, pulsamos el botón de eliminar registro para el registro de interés, y el sistema muestra el siguiente mensaje: ¿Está seguro de eliminar este registro?, junto con las opciones: “Cancelar” y “Confirmar”. Si presionamos la opción “Confirmar”, el sistema muestra el mensaje “Registro eliminado con éxito”. Si, presionamos la opción “Cancelar”, el sistema no ejecuta ninguna acción."
