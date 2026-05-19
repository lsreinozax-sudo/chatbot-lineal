def movimientos_bancarios_filtros_busqueda():
    return "Código y Fecha de Pago."

def movimientos_bancarios_tabla_columnas():
    return "Fecha de pago, Código, Documento de Referencia, Tipo de Transacción, Concepto, Monto, Estatus (Aprobado(a), Anulado o Pendiente), Y por ultimo la columna Acción junto con los botones: Ver detalles, Modificar registro. Y Eliminar Registro (Estos botones se visualizan o no según el estatus de la emisión de pago)"

def crear_movimiento_bancario_campos():
    return "Institución, Fecha de Pago, Tipo de Transacción(El sistema muestra las opciones Nota de Crédito y Nota de Débito), Nro de Cuenta(El sistema muestra la listas de cuentas bancarias previamente registradas. Al seleccionar una, el sistema presenta los campo Banco y Tipo de cuenta, asociados a la selección), Tipo de moneda (ya configurada en la aplicación base), Nro. Documento Origen, Concepto"

def movimiento_datos_contables_seccion():
    return "La sección Datos Contables se activa si en el campo Tipo de Transacción seleccionamos la opción Nota de Crédito. En esta sección el sistema solicita ingresar la siguiente información: Código de Cuenta – Denominación(El sistema muestra un campo de selección con las cuentas contables previamente cargadas en el módulo de Contabilidad), Debe y Haber(En estos campos agregamos el monto de afectación del asiento contable), Acción que muestra los botones: Vaciar Valores (Limpia el formulario), Eliminar(Elimina la cuenta)"

def movimiento_botones_formulario():
    return "“Borrar”, que permite limpiar los datos del formulario, “Cancelar”, permite cerrar el formulario, Y “Guardar” -que almacena los datos que se ingresan-"

def movimiento_guardar_exito():
    return "Si omitimos un campo obligatorio, marcado con un asterisco rojo, aparece el mensaje “El campo X es obligatorio”. Al guardar, debemos visualizar el mensaje: “Registro almacenado con éxito”."

def movimiento_aprobar_registro():
    return "Los movimientos bancarios cuyo estatus es Pendiente, deben aprobarse para que el sistema genere automáticamente el movimiento bancario. Para esto pulsamos el botón Aprobar registro ubicado en la columna Acción y el sistema muestra una ventana con dos opciones Cerrar y Aceptar. Si pulsamos Cerrar el sistema no ejecuta ninguna acción y si pulsamos Aceptar muestra el mensaje: “¿Está seguro? Una vez aprobado el registro no se podrá modificar ni eliminar.” con las opciones “No” o “Si”. Al pulsar “Sí”, el sistema aprueba el movimiento bancario con éxito. Posteriormente se visualiza en la tabla de registros que el movimiento bancario fue aprobado y su estatus se muestra Pagado."

def movimiento_ver_registro_detalle():
    return "Datos del movimiento bancario, tales como: Institución, Fecha de pago, Tipo de moneda, Tipo de transacción, Nro de Cuenta, banco, tipo de cuenta, Documento de referencia, concepto, monto, tipo de moneda. Y una tabla de los Datos del asiento contable, con sus respectivas cuentas por el Debe y por el Haber."

def movimiento_modificar_registro():
    return "Si pulsamos el botón Modificar registro ubicado en la columna Acción, para un registro de interés, el sistema nos muestra que la información fue cargada en forma de edición en la parte superior de la ventana. Actualizamos aquellos Campos que sean de interés y pulsamos el botón guardar. El sistema muestra el mensaje “Registro actualizado con éxito”. Solo pueden modificarse aquellos movimientos cuyo estatus sea “Pendiente”."

def movimiento_eliminar_registro():
    return "Para eliminar un registro, pulse el botón Eliminar registro” El sistema muestra el mensaje: ¿Está seguro de eliminar este registro?, junto con las opciones: “Cancelar” y “Confirmar”. Si el usuario pulsa la opción “Confirmar”, el sistema muestra el mensaje “Registro eliminado con éxito”. Si se pulsa la opción “Cancelar”, el sistema no ejecuta ninguna acción."

def conciliacion_bancaria_tabla_columnas():
    return "Código, Banco, Saldo en Sistema, Saldo en Banco, Inicio de Periodo, Fin de Periodo, Estatus, Y por ultimo la columna Acción junto con los botones: Aprobar registro, Ver detalles, Imprimir registro, Modificar registro. Y Eliminar Registro"

def crear_conciliacion_bancaria_campos():
    return "Institución, Nro de Cuenta(El sistema muestra la listas de cuentas bancarias previamente registradas. Al seleccionar una, el sistema presenta los campo Banco y Tipo de cuenta, asociados a la selección), Tipo de moneda (ya configurada en la aplicación base), Mes(Para esto el sistema muestra los meses en el campo de selección), Año(Para esto el sistema muestra los años en los que se han ejecutado o realizado registros)"

def conciliacion_seccion_ejemplo_carga():
    return "Botones para realizar la carga y descarga de archivo: Botón Importar, este botón permite cargar un archivo de hoja de cálculo. Botón Exportar, este botón permite descargar un archivo de hoja de cálculo. Seguidamente el sistema presenta una tabla denominada Formato del archivo, con las columnas Fecha, Descripción, Referencia Bancaria, Débito, Crédito y Saldo."

def conciliacion_exportar_archivo():
    return "Presionamos el botón Exportar, seguidamente el sistema genera un archivo en hoja de calculo, el cual nos permite ingresar los movimientos del banco. Este archivo contiene las columnas Fecha, Descripción, Referencia Bancaria, Débito, Crédito y Saldo."

def conciliacion_importar_archivo():
    return "Una vez tengamos la información cargada en el archivo pulsamos el botón “Importar”, y seleccionamos el archivo con los movimientos bancarios. Al cargar el archivo, el sistema presenta el botón “Buscar”, el cual permite comparar los registros del archivo cargado con los generados en el sistema. Al pulsar el botón “Buscar”, el sistema presenta el botón Sincronizar movimientos automáticamente y los campos de selección Movimientos en el sistema y Movimientos bancarios."

def conciliacion_automatica():
    return "Si generamos la conciliación bancaria de forma automática, presionamos el botón “Sincronizar movimientos automáticamente”. Seguidamente el sistema presenta una tabla formada por dos columnas, Sistema y Banco, la cual muestra los movimientos cargados en el sistema y el archivo. Además presenta el botón Eliminar para cada registro o movimiento."

def conciliacion_manual():
    return "Si deseamos generar la conciliación de forma manual, seleccionamos el registro, en el campo denominado “Movimientos en el sistema”. Al realizarlo, el sistema activa el campo Movimientos Bancarios para seleccionar el registro asociado al movimiento. Una vez ingresada esta información , pulsamos el botón “Agregar registro”. Seguidamente el sistema presenta una tabla formada por dos columnas, Sistema y Banco, la cual muestra los movimientos cargados en el sistema y el archivo. Además presenta el botón Eliminar para cada registro o movimiento."

def conciliacion_botones_formulario():
    return "“Borrar”, que permite limpiar los datos del formulario, “Cancelar”, permite cerrar el formulario, Y “Guardar” -que almacena los datos que se ingresan-"

def conciliacion_guardar_exito():
    return "Si omitimos un campo obligatorio, marcado con un asterisco rojo, aparece el mensaje “El campo X es obligatorio”. Al guardar, debemos visualizar el mensaje: “Registro almacenado con éxito”."

def conciliacion_aprobar_registro():
    return "Las conciliaciones bancarias cuyo estatus es Pendiente, deben aprobarse para que el sistema genere automáticamente la conciliación bancaria. Para esto pulsamos el botón Aprobar registro ubicado en la columna Acción y el sistema muestra una ventana con dos opciones Cerrar y Aceptar. Si pulsamos Cerrar el sistema no ejecuta ninguna acción y si pulsamos Aceptar muestra el mensaje: “¿Está seguro? Una vez aprobado el registro no se podrá modificar ni eliminar.” con las opciones “No” o “Si”. Al pulsar “Sí”, el sistema aprueba la conciliación bancaria con éxito. Posteriormente se visualiza en la tabla de registros que la conciliación bancaria fue aprobada y su estatus se muestra Aprobado."

def conciliacion_ver_registro_detalle():
    return "Datos de la conciliación bancaria, tales como: Código, Periodo, Estatus, Tipo de moneda, Saldo en Banco, Saldo en sistema, Institución, Banco, Nro. de Cuenta y la tabla de registros Fecha, Código del movimiento, Concepto en sistema, Concepto Bancario, Débito, y Crédito."

def conciliacion_imprimir_registro():
    return "Si pulsamos el botón Imprimir registro, el sistema descarga un archivo en formato .pdf"

def conciliacion_modificar_registro():
    return "Si pulsamos el botón Modificar registro ubicado en la columna Acción, para un registro de interés, el sistema muestra la información que fue cargada en forma de edición en la parte superior de la ventana. Actualizamos aquellos campos que sean de interés y pulsamos el botón guardar. El sistema muestra el mensaje “Registro actualizado con éxito”. Solo pueden modificarse aquellas conciliaciones bancarias cuyo estatus sea “Pendiente”."

def conciliacion_eliminar_registro():
    return "Para eliminar un registro, pulse el botón Eliminar registro” El sistema muestra el mensaje: ¿Está seguro de eliminar este registro?, junto con las opciones: “Cancelar” y “Confirmar”. Si el usuario pulsa la opción “Confirmar”, el sistema muestra el mensaje “Registro eliminado con éxito”. Si se pulsa la opción “Cancelar”, el sistema no ejecuta ninguna acción."
