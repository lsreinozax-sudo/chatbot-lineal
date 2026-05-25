def ajustes_tablas_salariales_descripcion():
    return "Esta funcionalidad le permite al usuario gestionar las actualizaciones de tablas salariales, de acuerdo a un aumento oficial de salarios."

def ajustes_tablas_salariales_requisitos():
    return "Para esto es necesario que el usuario posea los permisos requeridos para acceder a esta funcionalidad. También, se requiere que previamente se hayan realizado registros previos de información en la configuración de los tabuladores salariales."

def ajustes_tablas_salariales_acceso():
    return "Para ilustrar el proceso de ajustes en tablas salariales, ingresamos al sistema con las credenciales de acceso suministradas por el administrador del sistema, luego nos dirigimos al módulo de talento humano, submódulo ajustes en tablas salariales."

def ajustes_tablas_salariales_pantalla_inicial():
    return "Y el sistema nos muestra una pantalla denominada “Ajustes en Tablas Salariales” que contiene una tabla con las siguientes columnas: Fecha de generación, Fecha del aumento, Fecha de culminación, Tipo de aumento, Valor, Tabulador salarial, y Acción. También cuenta con las opciones “Ir atrás”, “Crear nuevo registro”, “Importar registros” y “Presione para descargar el documento con la información de los registros”"

def ajustes_tablas_salariales_crear_formulario_campos():
    return "Al pulsar la opción “Crear nuevo registro”, el sistema muestra un formulario con los siguientes campos: - Fecha de generación que es un campo generado por el sistema, - Fecha del aumento que es un campo de tipo fecha, - Fecha de culminación del aumento que es un campo que puede quedar indefinido hasta la fecha en que se de un nuevo aumento de la tabla salarial. - Tabulador salarial que lista los tabuladores salariales registrados previamente en la configuración de los parámetros generales de nómina - Y Tipo de aumento, con las opciones: porcentual, valor absoluto y diferente: 1. En caso de valor porcentual, el sistema nos solicita que se ingrese el valor del porcentaje de aumento, y el sistema aplica el porcentaje indicado a la tabla salarial seleccionada previamente. 2. En caso de valor absoluto, el sistema nos solicita que se ingrese el valor absoluto del aumento, y el sistema aplica el valor indicado a la tabla salarial seleccionada previamente. 3. En caso de la opción diferente, el sistema activa el botón siguiente, y muestra la tabla salarial seleccionada previamente, para que modifiquemos los valores que se requieran."

def ajustes_tablas_salariales_campo_obligatorio():
    return "Es importante mencionar que los campos en los que se detalla un asterisco rojo, son de tipo obligatorio y omitirlo, generará una alerta indicando que debe ingresar el mismo."

def ajustes_tablas_salariales_botones_formulario():
    return "Este formulario también, presenta los botones: - “Borrar datos del formulario” que nos permite limpiar el formulario, - “Cancelar y Regresar” que permite salir del formulario - Y “Guardar” que realiza la acción de almacenar los datos que se ingresan."

def ajustes_tablas_salariales_guardar_exito():
    return "Ingresamos la información solicitada y pulsamos guardar, para que el sistema almacene la información. El sistema al realizar el registro muestra el mensaje: “Registro almacenado con éxito”, y lo enlista en la tabla que contiene las columnas anteriormente mencionadas y en la columna acción se muestran los botones modificar registró y eliminar registró."

def ajustes_tablas_salariales_modificar_registro():
    return "Para modificar la información previamente ingresada, presionamos el botón “Modificar Registro”, seguidamente el sistema nos muestra la información registrada sobre los ajustes en tablas salariales en forma de edición, junto con los botones “Borrar” “Cancelar y regresar” y “Guardar”. Si modificamos la información de interés, y pulsa el botón “Guardar”, el sistema nos muestra el mensaje: “Registro actualizado con éxito”. Si pulsamos el botón “Borrar”, el sistema borra la información ingresada. Si presionamos el botón “Cancelar y regresar”, el sistema no ejecuta ninguna acción."

def ajustes_tablas_salariales_eliminar_registro():
    return "Para eliminar un registro de ajustes en tablas salariales, presionamos el botón “Eliminar registro”, seguidamente el sistema muestra el siguiente mensaje: ¿Está seguro de eliminar este registro?, junto con las opciones: “Cancelar” y “Confirmar”. Si presionamos la opción “Confirmar”, el sistema muestra el mensaje “Registro eliminado con éxito”. Si, pulsamos la opción “Cancelar”, el sistema no ejecuta ninguna acción."

def ajustes_tablas_salariales_carga_masiva():
    return "El sistema también permite cargar los registros de forma masiva mediante una hoja de cálculo. Para esto, se recomienda primero realizar una Exportación de los registros que se encuentran en el sistema haciendo uso del botón que permite realizar la descarga del archivo. Esto nos permite editar archivo, para agregar tantos registros como requiera, y luego usarlo para realizar una Importación mediante el botón “Importar registros”."


