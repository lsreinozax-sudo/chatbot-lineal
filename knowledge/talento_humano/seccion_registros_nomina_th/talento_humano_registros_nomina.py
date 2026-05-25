def registros_nomina_pantalla_inicial():
    return "Pulsamos la opción registros de nómina, y enseguida el sistema muestra una pantalla denominada “Registros de nómina”, que contiene una tabla con las siguientes columnas: Código, Fecha de generación, Nombre, Periodo de pago, Tipo de nómina y Acción. Y el sistema también muestra los botones “Ir atrás” y “Crear nuevo registro”."

def registros_nomina_crear_formulario_campos():
    return "Pulsamos sobre el botón “Crear nuevo registro”, y el sistema presenta un formulario con los siguientes campos: -Fecha de generación donde este campo es de tipo fecha, -Nombre, -Tipo de pago que lista los tipos de pago registrados previamente en la configuración, aquellos nombres que se muestren bloqueados es que ya poseen un registro de nómina que aún no se ha cerrado, -Periodo de pago que muestra la fecha de inicio del periodo, una vez se haya seleccionado el tipo de pago, -Conceptos que muestra los conceptos asociados al tipo de pago que se haya seleccionado. Además, nos permite agregar o quitar algún concepto en caso de requerirlo."

def registros_nomina_parametros_informacion_general():
    return "Este formulario, también muestra Parámetros de Nómina e Información general, como: Cantidad de lunes de mes, fecha del primer lunes de mes, Inicio de mes, Día de semana de inicio de mes."

def registros_nomina_campo_obligatorio():
    return "Es importante mencionar que los campos en los que se detalla un asterisco rojo, son de tipo obligatorio y omitirlo, generará una alerta indicando que debe ingresar el mismo."

def registros_nomina_botones_formulario():
    return "Este formulario también, presenta los botones: - “Borrar datos del formulario” que nos permite limpiar el formulario, - “Cancelar y Regresar” que nos permite salir del formulario - Y “Guardar” que realiza la acción de almacenar los datos que se ingresan."

def registros_nomina_guardar_exito():
    return "Ingresamos la información solicitada y pulsamos guardar, para que el sistema almacene la información. El sistema al realizar el registro muestra el mensaje: “Registro almacenado con éxito”, y lo enlista en la tabla que contiene las columnas anteriormente mencionadas y en la columna acción se muestran los botones:: Generar archivo .xlsx, Generar reporte presupuestario del registro, Modificar registro, Solicitar disponibilidad presupuestaria, Aprobar registro, Cerrar registro y enviar recibos."

def registros_nomina_notificaciones_ejecucion():
    return "Para saber si la nómina se ejecutó con éxito o no, el sistema muestra en las notificaciones del sistema el mensaje “Nómina ejecutada con éxito” o el mensaje de que ocurrió un error durante la ejecución."

def registros_nomina_flujo_exito():
    return "Si la nómina se ejecutó con éxito, podemos proseguir a generar los diferentes reportes asociados, solicitar disponibilidad, y una vez que se esté seguro que son los cálculos que corresponden se puede cerrar el registro de nómina."

def registros_nomina_generar_archivo_xlsx():
    return "Para generar el reporte de los cálculos de nómina presionamos la opción “Generar archivo .xlsx”, y enseguida el sistema genera un archivo de hoja de cálculo que muestra la siguiente información: i) Sección encabezado: que muestra el Nombre de la institución, Nombre del registro de nómina y Fecha de generación. ii) Sección de cálculos, con las columnas: Trabajadores, Cédula de identidad, Grado de instrucción, Cargo, Fecha de ingreso, Total años de servicios, y los Conceptos calculados, bien sean los asociados a las asignaciones, deducciones, aportes patronales y demás conceptos que se hayan configurado previamente en el formulario de tipos de nómina."

def registros_nomina_archivo_xlsx_hojas_adicionales():
    return "Este archivo muestra también una hoja con los conceptos utilizados en el registro de nómina. Y una hoja para cada tabulador que incide en los conceptos calculados."

def registros_nomina_generar_reporte_presupuestario():
    return "Para generar el reporte asociado a la afectación presupuestaria del registro de nómina, pulsamos la opción “Generar reporte presupuestario del registro”, luego el sistema genera un archivo que muestra la siguiente información: Nombre del tipo de nómina y la Sección de afectación presupuestaria que cuenta con las columnas partida, denominación y monto total de los conceptos por partida presupuestaria."

def registros_nomina_modificar_registro():
    return "En caso de que se requiera modificar la información ingresada previamente, pulsamos la opción modificar registro para el registro de nómina de interés, y se edita la información que se requiera, presionamos guardar y el sistema muestra el mensaje: “Registro actualizado con éxito”. Una vez que modifiquemos el registro de nómina, el sistema actualiza los cálculos del archivo .xlsx y en el reporte pdf."

def registros_nomina_solicitar_disponibilidad():
    return "Para solicitar la disponibilidad presupuestaria del registro de nómina, presionamos la opción “Solicitar disponibilidad presupuestaria”, y el sistema muestra el formulario de “Enviar notificación”, con los campos: - Usuario, que muestra la lista de usuarios registrados en el sistema y seleccionamos a quien va dirigida la solicitud - Y Mensaje, donde se puede redactar un mensaje para el destinatario, también se muestran los botones “Cerrar” y “Enviar”. Ingresamos los datos solicitados y pulsamos enviar, para lo que el sistema envía la notificación de solicitud de disponibilidad presupuestaria al correo del usuario seleccionado previamente."

def registros_nomina_completar_disponibilidad_presupuesto():
    return "Procedemos a irnos al módulo de Presupuesto y seleccionamos la opción de “Disponibilidad Presupuestaria”, el sistema nos abre la ventana de disponibilidad en donde nos dirigimos a la columna de acción y presionamos el botón “completar solicitud presupuestaria”. Posteriormente el sistema nos presenta una tabla de registros que en la parte posterior contiene los botones “Hay disponibilidad” y “No hay Disponibilidad”, procedemos a pulsar el botón de “Hay Disponibilidad”. El sistema procede a mostrarnos una ventana con un enlistado donde aparece la columna “Acción”, procedemos a seleccionar el botón de “Aprobar disponibilidad presupuestaria”, al hacerlo el sistema nos muestra un mensaje de “Aprobar Disponibilidad Presupuestaria” donde sale el código de requerimiento seleccionado, pulsamos el botón de “Si”, nos aparece un mensaje de confirmación y seleccionamos “Confirmar”"

def registros_nomina_aprobar_registro():
    return "Una vez aprobada la disponibilidad presupuestaria, regresamos al módulo de talento humano, sección Registro de Nomina, y apreciaremos que se habilita el botón Aprobar registro en donde confirmamos nuestra solicitud al sistema."

def registros_nomina_cerrar_registro():
    return "Al aprobar el registro, el sistema habilita el botón Cerrar registro, con el cual podemos cerrar el registro de nómina, para ello, pulsamos sobre el mismo, y el sistema cierra el registro de nómina y genera de forma automática los asientos contables, compromisos, órdenes de pago y la emisión de pago de nómina."

def registros_nomina_apertura_siguiente_periodo():
    return "Una vez se cierre el periodo de nómina, el sistema apertura el siguiente periodo asociado al tipo de nómina."

def registros_nomina_no_modificable_cerrado():
    return "Una vez se cierre el registro de nómina este no puede ser modificado."

def registros_nomina_cierre_con_orden_pago():
    return "Si en la configuración del tipo de nómina se activó el botón orden de pago, el sistema al cerrar el registro genera lo que se indica a continuación: I. Asiento contable de orden de pago de nómina. II. Asiento contable de emisión de pago de nómina. III. Asiento contable de órdenes de pago para cada beneficiario del pago de aportes y deducciones. IV. Orden de pago de nómina, de pago de aportes y deducciones por cada beneficiario. V. Emisión de pago de nómina. VI. Compromiso de pago de nómina, de pago de aportes y deducciones por cada beneficiario."

def registros_nomina_cierre_sin_orden_pago():
    return "Si en la configuración del tipo de nómina no se activó el botón “orden de pago”, el sistema al cerrar el registro genera lo que se indica a continuación: I. Asiento contable de órdenes de pago para cada beneficiario del pago de aportes y de deducciones. II. Orden de pago de aportes y deducciones por cada beneficiario. III. Compromiso de pago de nómina, de pago de aportes y de deducciones por cada beneficiario."

def registros_nomina_enviar_recibos():
    return "Para realizar el envío de los recibos de pagos asociados al registro de nómina, presionamos la opción “Enviar recibo”, el sistema nos muestra el mensaje “Los recibos se están enviando”, y envía el recibo al correo de cada trabajador. El sistema envía el recibo de pago al correo institucional, de no existir correo institucional asociado al trabajador el sistema debe enviar el recibo de pago al correo personal."

