

def submenu_gestion_pagos():
    return "Al seleccionarlo, se despliega un sub-menú donde se ven las opciones: Órdenes y Emisiones de pago."

def ordenes_filtros_busqueda():
    return "Código, Fecha de solicitud, Monto, y los botones Borrar (para limpiar los filtros) y Buscar."

def ordenes_tabla_columnas():
    return "Código de la orden de pago, Fecha de solicitud, Proveedor o Beneficiario, Concepto, Monto, Estatus, Y la columna Acción junto con las opciones: Ver registro, Aprobar registro, Imprimir registro, Modificar registro, Y Anular registro"

def crear_orden_pago_secciones():
    return "Para crear una nueva orden de pago se debe pulsar el botón Crear nuevo registro. El sistema muestra una pantalla con un formulario con 4 secciones:"

def orden_seccion_datos_orden_campos():
    return "Institución, Fecha de la orden de pago, Tipo de orden (El sistema cuenta las opciones Presupuestario y No Presupuestario), Tipo de documento (El sistema muestra la información de acuerdo a la selección del campo anterior. Sí la selección es Presupuestario, el sistema muestra las opciones: Compromiso presupuestario, Orden de Compra/Servicio y Otro. Sí la selección es No presupuestario, el sistema muestra Manual y Retenciones), Nro. de documento de origen (El sistema muestra los registros asociados a los parámetros previamente registrados)"

def orden_seccion_datos_proveedor_campos():
    return "Nombre o Razón Social del beneficiario (previamente registrados en el módulo de compras), Monto. El sistema carga automáticamente estos campos al seleccionar el número de documento origen. Luego tenemos el campo Concepto. Y el campo Observación"

def orden_retenciones_campos_adicionales():
    return "Nota: Si el registro de la Orden de Pago, en el tipo de Orden es No presupuestario, y el tipo de Documento indica Retenciones, el sistema presenta los campos de selección Mes y Periodo."

def orden_seccion_datos_contables():
    return "Finalmente, en la sección de Datos Contables, los campos se cargan automáticamente con la información ingresada en las secciones anteriores."

def orden_botones_formulario():
    return "“Borrar”, que permite limpiar los datos del formulario, “Cancelar”, permite cerrar el formulario, Y “Guardar” -que almacena los datos que se ingresan-"

def orden_guardar_mensaje_comprobante():
    return "Si guardamos el registro, el sistema nos muestra un mensaje de si deseamos generar un comprobante con la información suministrada."

def orden_guardar_exito():
    return "Si omitimos un campo obligatorio, marcado con un asterisco rojo, aparece el mensaje “El campo X es obligatorio”. Al guardar, debemos visualizar el mensaje: “Registro almacenado con éxito”."

def orden_ver_registro_detalle():
    return "Datos de la orden, tales como: Institución, Fecha, Tipo de orden, Tipo de Documento, Número de Documento de Origen. Datos del proveedor o beneficiario, tales como: Nombre o Razón Social, Monto, Concepto y Observación. Y finalmente una tabla de los Datos contables, con la selección del “Código de cuenta – denominación” con sus respectivas cuentas por el Debe y por el Haber."

def orden_aprobar_registro():
    return "Las Ordenes de pago muestran el estatus Pendiente hasta ser aprobadas, para lo cual presionamos el botón Aprobar registro ubicado en la columna Acción. El sistema nos muestra una ventana con el siguiente mensaje: “¿Está seguro? Una vez aprobado el registro no se podrá modificar ni eliminar”. Si pulsamos No el sistema no ejecuta ninguna opción y si pulsamos Sí el sistema muestra el mensaje que fue aprobado con éxito."

def orden_modificar_registro():
    return "Si pulsamos el botón Modificar registro ubicado en la columna Acción, para un registro de interés, el sistema nos muestra la información que fue cargada en forma de edición en la parte superior de la ventana. Actualizamos aquellos Campos que sean de interés y pulsamos el botón guardar. El sistema muestra el mensaje “Registro actualizado con éxito”. Solo pueden modificarse aquellas órdenes cuyo estatus sea “Pendiente”."

def orden_anular_registro_campos():
    return "Código de la Orden de Pagina, El campo Anulación, que cuenta con las opciones Sin remisión o Con remisión, Descripcion, Fecha de anulación, Descripcion del motivo de anulación."

def orden_anular_sin_remision_mensaje():
    return "Si seleccionamos la opción Sin remisión, se muestra el siguiente mensaje: “¿Está seguro? Una vez anulada esta Orden de pago, todo el proceso se anulará hasta el compromiso”. Seguidamente presenta las opciones Cancelar y Continuar."

def orden_anular_con_remision_mensaje():
    return "Si seleccionamos la opción Con remisión, se muestra el siguiente mensaje: “¿Está seguro? Una vez anulada esta Orden de pago, el estado del registro cambiará a 'Anulado' y se podrá generar una nueva 'Orden de pago'”. Seguidamente presenta las opciones Cancelar y Continuar."

def orden_anular_guardar():
    return "Una vez registrada la información se muestran las opciones Cerrar y Guardar. Si pulsamos Cerrar el sistema no ejecuta ninguna acción. Si pulsamos Guardar el sistema muestra el mensaje “Registro anulado”. Una vez anulado este registro, el compromiso asociado a esta orden de pago se libera."

def emision_pago_filtros_busqueda():
    return "Código, Fecha de solicitud, y los botones Borrar (para limpiar los filtros) y Buscar."

def emision_pago_tabla_columnas():
    return "Código, Fecha de pago, Proveedor o beneficiario, Concepto, Estatus (Pagado, Anulado o Pendiente), Y por ultimo la columna Acción junto con los botones: Aprobar registro, Ver detalles, Generar comprobante de retención, Imprimir registro, Y Modificar registro. (Estos botones se visualizan o no según el estatus de la emisión de pago)"

def crear_emision_pago_campos():
    return "Fecha de la emisión de pago (la fecha que se ingrese debe ser igual o posterior a la fecha de la orden de pago que vamos a emitir), ¿Pago Parcial? (con las opciones Sí y No), Proveedor o Beneficiarios (previamente registrados en el módulo de compras), Tipo de moneda (ya configurada en la aplicación base), Número de Documento (Corresponde a las ordenes de pago registradas y aprobadas, según el proveedor o beneficiario que acabamos de seleccionar)."

def emision_campos_automaticos():
    return "Cuando pulsamos la opción de nuestra preferencia, se activan automáticamente los campos: Monto de la orden, Monto del pago (subtotal), Retenciones, Total a pagar, Tipo de Retencion, Numero de Factura, Y Numero de Referencia Bancaria"

def emision_agregar_retencion():
    return "El campo Tipo de retención se utiliza en caso de que la emisión posea una retención. Seleccionamos las retenciones de interés a partir de las opciones que despliega este campo. Luego pulsamos el botón Agregar retención, identificado con un signo más (+). El sistema muestra una ventana que nos permite agregar la base imponible y automáticamente el sistema calcula el monto de la retención. Al ejecutar este proceso, el sistema agrega el monto calculado en el campo Retenciones. Esta ventana cuenta con dos opciones Cerrar y Agregar. Si pulsamos Cerrar el sistema no ejecuta ninguna acción en la emisión de pago, pero si pulsamos Agregar registra el porcentaje de esta retención y el campo Nro. de retención se carga automáticamente."

def emision_tabla_retenciones_columnas():
    return "Tipo de retención, Base imponible, Monto y Acción."

def emision_datos_bancarios_campos():
    return "Método de pago, Banco y Número de cuenta (previamente cargados en la configuración de Finanzas), Finalmente, el campo Observaciones."

def emision_datos_contables():
    return "En esta pantalla también visualizamos los Datos contables con sus respectivas cuentas por el Debe y por el Haber."

def emision_botones_formulario():
    return "“Borrar”, que permite limpiar los datos del formulario, “Cancelar”, permite cerrar el formulario, Y “Guardar” -que almacena los datos que se ingresan-"

def emision_guardar_exito():
    return "Si omitimos un campo obligatorio, marcado con un asterisco rojo, aparece el mensaje “El campo X es obligatorio”. Al guardar, debemos visualizar el mensaje: “Registro almacenado con éxito”."

def emision_aprobar_registro_campos():
    return "Código de la emisión de pago, el cual se encuentra bloqueado. Este es el código de la emisión que seleccionamos. El campo Fecha de aprobación, la cual puede ser igual o posterior a la emisión de pago."

def emision_aprobar_confirmacion():
    return "Además se cuenta con dos opciones Cerrar y Aceptar. Si pulsamos Cerrar el sistema no ejecuta ninguna acción y si pulsamos Aceptar muestra el mensaje: “¿Está seguro? Una vez aprobado el registro no se podrá modificar ni eliminar.” con las opciones “No” o “Si”. Al pulsar “Sí”, el sistema aprueba la emisión de pago con éxito. Posteriormente se visualiza en la tabla de registros que la emisión de pago fue aprobada y su estatus se muestra Pagado."

def emision_ver_registro_detalle():
    return "Datos de la emisión, tales como: Institución, Fecha, Tipo de moneda, Número de Referencia y Codigo Ordenes de Pago, Datos de la Factura como el Numero, Datos del proveedor o beneficiario, tales como: Nombre o Razón Social, Pago parcial, Monto, Retenciones y Monto a pagar, Datos bancarios, tales como: Método de pago, Banco, Número de Cuenta, Observación y Numero de referencia bancaria. En caso de tener el estatus de Anulada, se visualiza la Descripción del motivo de anulación. Y una tabla de los Datos contables, con sus respectivas cuentas por el Debe y por el Haber."

def emision_imprimir_registro():
    return "Si pulsamos el botón Imprimir registro, el sistema descarga un archivo en formato .pdf"

def emision_modificar_registro():
    return "Si pulsamos el botón Modificar registro ubicado en la columna Acción, para un registro de interés, el sistema nos muestra que la información que fue cargada en forma de edición en la parte superior de la ventana. Actualizamos aquellos Campos que sean de interés y pulsamos el botón guardar. El sistema muestra el mensaje “Registro actualizado con éxito”. Solo pueden modificarse aquellas órdenes cuyo estatus sea “Pendiente”."

def emision_anular_registro_campos():
    return "Código de la emisión de pago (este campo esta bloqueado, muestra la emisión de pago que seleccionamos para anular), El campo Anulación, el cual cuenta con las opciones “Sin remisión” y “Con remisión”."

def emision_a_sin_remision_mensaje():
    return "Al seleccionar la opción Sin remisión, el sistema despliega el mensaje ¿Está seguro? Una vez anulada esta Emisión de pago, todo el proceso se anulará hasta el compromiso.” Presenta las opciones Cancelar, para abortar el proceso, y Continuar, proceder con la anulación."

def emision_anular_con_remision_mensaje():
    return "Al seleccionar la opción Con remisión, el sistema despliega el mensaje “¿Está seguro? Una vez anulada esta Emisión de pago, el estado del registro cambiará a 'Anulado' y se podrá generar una nueva 'Emisión de pago'”. Presenta las opciones Cancelar, para abortar el proceso, y Continuar, para proceder con la anulación."

def emision_anular_campos_adicionales():
    return "Observaciones, Fecha de anulación, Y una Descripción del motivo de anulación."

def emision_generar_comprobante_retencion():
    return "Si pulsamos el botón Generar Comprobante de Retenciones de Pago ubicado en la columna Acción, para un registro de interés, el sistema presenta una ventana llamada Reportes de IVA, donde solicita la siguiente información: Retenciones(Presenta un campo de selección, el cual lista las retenciones previamente registradas en el requerimiento y ejecución de pago). Seguidamente el sistema muestra una tabla, donde solicita la siguiente información: Tipo de Alicuota, % Alicuota, Base Imponible, Total compra sin IVA, Impuesto IVA, IVA Retenido, Y por último el campo acción."

def emision_reporte_retencion_estructura():
    return "Logo de la institución u organización, Titulo y Providencia, Nro° de comprobante, Fecha, Nombre o Razón Social del Agente de Retención, R.I.F del Agente de retención, Periodo Fiscal, Dirección Fiscal del agente de retención, Nombre o Razón social de sujeto retenido, R.I.F. Del sujeto retenido. Seguidamente el sistema presenta una tabla, formada por las siguientes columnas: Operación Nro., Fecha de la Factura, Número de la factura, Número de Control, Tipo de transacción, Total Compras con IVA, Compras sin derecho a crédito IVA, Base imponible, % Alicuota, Impuesto IVA, IVA Retenido. Agente de retención(Sello, Fecha y Firma)"