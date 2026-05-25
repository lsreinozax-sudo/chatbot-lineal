def pendientes_descripcion():
    return "Esta funcionalidad permite ingresar aquellos parámetros no relacionados o que se pagaron de más en periodos anteriores."

def pendientes_pantalla_inicial():
    return "Para ellos, presionamos la opción Pendientes, y enseguida el sistema muestra una pantalla denominada “Hoja de tiempo pendiente”, que contiene una tabla con las siguientes columnas: Periodo, Código, Supervisor, Aprobador, Estatus y Acción. También, como se puede detallar, el sistema muestra los botones “Ir atrás” y “Crear nuevo registro”."

def pendientes_crear_formulario_campos():
    return "Al presionar el botón “Crear nuevo registro”, el sistema nos presenta un formulario con los siguientes campos: Desde y Hasta donde ambos campos son de tipo fecha, Código de grupo de supervisados que lista los códigos de los grupos supervisados registrados previamente, Parámetros de la hoja de tiempo que enlista los código de las hojas de tiempo previamente configuradas, Supervisor donde este campo es generado por el sistema una vez se indique el código del grupo de supervisados al igual que el campo Aprobador."

def pendientes_tabla_parametros():
    return "Una vez que indicamos información en los campos Código de grupo de supervisados y en el campo Parámetros de la hoja de tiempo, el sistema muestra una tabla con las columnas: N°, Ficha, Nombre, y las columnas asociadas a los diferentes parámetros configurados previamente en parámetros globales, y a su vez por cada tipo de parámetro de tiempo el sistema debe mostrar una columna de subtotal, y la columna de Total la cual muestra la sumatoria de los subtotales, adicionalmente presenta las columnas observación y conceptos, para estas dos columnas el sistema presenta el botón más(+) asociados a cada trabajador."

def pendientes_boton_observacion():
    return "Si pulsamos el botón + de la columna observación para un determinado trabajador, el sistema muestra una ventana que contiene el campo observaciones para ingresar información relacionada a los parámetros que se ingresan. Si pulsamos el botón + de la columna observaciones, el sistema presenta una ventana donde podemos redactar acerca de la información requerida, además presenta los botones Cerrar, Limpiar y Agregar"

def pendientes_boton_conceptos():
    return "Si pulsamos el botón + de la columna conceptos, el sistema presenta una ventana donde solicita que se ingrese el tipo de pago y los conceptos que alimentaran los parámetros que se ingresen, los conceptos ingresados serán mostrados por el sistema al momento de procesar la nómina en una sección denominada pendientes."

def pendientes_botones_formulario():
    return "Este formulario también, presenta los botones cancelar y regresar que permite salir del formulario, borrar datos del formulario permite limpiar el formulario y guardar que realiza la acción de almacenar los datos que se ingresan."

def pendientes_guardar_exito():
    return "Al ya haber ingresado la información solicitada, pulsamos guardar, para que el sistema almacene la información. El sistema al realizar el registro muestra el mensaje: “Registro almacenado con éxito”, y lo enlista en la tabla anteriormente mencionada, donde la columna Acción, contiene los botones para Ver registro, Aprobar registro, Confirmar registro, Rechazar registro, Modificar registro y Eliminar registro. Una vez se ingrese un registro de hoja de tiempo de pendientes este toma el estatus elaborado."

def pendientes_ver_registro():
    return "Para visualizar la información previamente ingresada, pulsamos el botón de “Ver registro”, para un esquema de guardias de interés, y seguidamente el sistema muestra una ventana denominada “Información Detallada de la Hoja de Tiempo Pendiente” que contiene información relevante de la hoja de tiempo, tal como: Desde, Hasta, Código grupo de supervisados, Supervisor, Aprobador, Estatus, Observaciones y la tabla de Registros que muestra la lista de trabajadores con los respectivos valores ingresados para cada parámetro de tiempo. Para cerrar esta ventana pulsamos sobre el icono X o sobre el botón cerrar."

def pendientes_aprobar_registro():
    return "Para aprobar un registro de hoja de tiempo pendiente, pulsamos el botón Aprobar para un registro de interés, enseguida el sistema muestra el mensaje ¿Está seguro? Una vez aprobado el registro no se podrá eliminar, junto con las opciones: “No” y “Si”. Si pulsamos sobre Si el sistema muestra el mensaje de notificación “Hoja de tiempo pendiente aprobada correctamente”, y el estatus del registro cambia a aprobado, se desactiva el botón eliminar, además el sistema notifica vía correo al supervisor correspondiente que el registro fue aprobado y activa los botones “Confirmar registro” y “Rechazar. Si pulsamos No, el sistema no ejecuta ninguna acción."

def pendientes_confirmar_registro():
    return "Para confirmar un registro de hoja de tiempo pendiente se requiere que este posea el estatus aprobado, seguidamente pulsamos la opción confirmar para un registro de interés, y el sistema muestra el siguiente mensaje ¿Está seguro? Una vez confirmado el registro no se podrá modificar, junto con las opciones: “Si” y “No”. En caso de que pulsemos Si, el sistema muestra el mensaje “Hoja de tiempo pendiente confirmada correctamente”, y cambia el estatus del registro a “Cerrado (a). Una vez confirmado un registro de hoja de tiempo pendiente, el sistema bloquea el botón Modificar. En caso de que pulsemos la opción No, el sistema no realiza ninguna acción."

def pendientes_rechazar_registro():
    return "Para rechazar un registro de hoja de tiempo pendiente se requiere que este posea el estatus aprobado, entonces pulsamos el botón Rechazar para un registro de interés, luego el sistema muestra una ventana denominada ¿Rechazar hoja de tiempo?, donde solicita que se ingrese información en el campo observaciones junto con las opciones: “Si” y “No”. Ingresamos la información solicitada y pulsamos Si, automáticamente el sistema cambia el estatus del registro a rechazado(a). Si pulsamos No, el sistema no ejecuta ninguna acción."

def pendientes_modificar_registro():
    return "En caso de que se requiera modificar la información ingresada previamente, pulsamos el botón Modificar para el registro de hoja de tiempo de interés, y editamos la información que se requiera, presionamos guardar y el sistema muestra el mensaje: “Registro actualizado con éxito”."

def pendientes_eliminar_registro():
    return "En caso de que se requiera eliminar el registro previamente ingresado, pulsamos la opción eliminar registro para el registro de interés, El sistema muestra el siguiente mensaje: ¿Está seguro de eliminar este registro?, junto con las opciones: “Cancelar” y “Confirmar”. Si pulsamos la opción “Confirmar”. El sistema muestra el mensaje “Registro eliminado con éxito”. Si, presionamos la opción “Cancelar”, el sistema no ejecuta ninguna acción."