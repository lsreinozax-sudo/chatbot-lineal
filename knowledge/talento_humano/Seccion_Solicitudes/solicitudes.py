"""Seccion de Solicitudes del ERP KAVAC del bien de talento humano"""

def que_tipos_de_solicitudes_existen():
    return "En este apartado se describen los pasos requeridos para realizar solicitudes de ARC, de Vacaciones, de Prestaciones y de Permisos en la funcionalidad de Solicitudes del módulo de talento humano."

def quienes_pueden_gestionar_solicitudes():
    return "Estas funcionalidades pueden ser accedidas por usuarios con los permisos requeridos, o bien, con rol de talento humano o administrador. Un administrador o personal de talento humano puede realizar solicitudes para cualquier trabajador. Por su parte, un usuario estándar con los permisos necesarios solo puede gestionar las solicitudes asociadas a su propio perfil."

def cuales_son_los_requisitos_previos():
    return "Para gestionar una solicitud de vacaciones, de prestaciones sociales o de permiso, es un requisito indispensable que previamente se haya configurado la política que rige dicha solicitud en el sistema."

def como_ingresar_al_modulo_talento_humano():
    return "Para iniciar el proceso, se ingresa al sistema con las credenciales de acceso suministradas por el administrador y nos dirigimos al módulo de talento humano. El sistema desplegará opciones como: Configuración, ajustes en tablas salariales, expediente, esquema de guardias, hoja de tiempo, registros de nómina, registro ari, archivo txt de nómina, solicitudes y reportes."

def como_acceder_al_menu_de_solicitudes():
    return "Al pulsar sobre la opción 'Solicitudes', el sistema habilitará inmediatamente un submenú con las alternativas: Solicitud de ARC, Solicitud de vacaciones, Solicitud de prestaciones y Solicitud de permisos."

# ==========================================
# SOLICITUD DE ARC
# ==========================================

def como_buscar_solicitud_arc():
    return """Para realizar una solicitud de ARC nos dirigimos a esta sección, y enseguida el sistema muestra una pantalla denominada solicitud de comprobante de retenciones acumuladas (ARC), que contiene los campos:
- Periodo fiscal,
- Y Trabajador,

Ingresamos la información solicitada, y pulsamos buscar, y el sistema lista la información en la tabla que contiene las columnas:
- Cédula de identidad,
- Ficha,
- Trabajador,
- Retención acumulada,
- Total remuneración pagadas,
- Y acción, que a su vez cuenta con los botones: ver registro, descargar planilla del registro y enviar planilla del registro."""


def como_ver_detalle_registro_arc():
    return """Si deseamos ver el detalle del registro solo debemos pulsar sobre el botón registro, para lo que el sistema habilita una ventana denominada “Comprobante de retenciones acumuladas ARC”, que muestra las secciones:
- Beneficiario de las remuneraciones, con la información asociada a: apellidos y nombres del trabajador, periodo, número de rif y cédula de identidad.
- Tipo de agente de retención, con el nombre, número de rif y dirección de la dependencia.
- También muestra una tabla con las columnas: mes, remuneraciones pagadas en cuenta, porcentaje de retención, impuesto retenido, remuneraciones pagadas acumuladas e impuesto retenido acumulado.
- Finalmente se puede detallar, el valor del total de remuneraciones pagadas y el trabajador responsable de generar la planilla ARC.

Para salir de la ventana pulse el icono x o pulsamos el botón cerrar."""


def como_descargar_o_enviar_planilla_arc():
    return """Si se requiere descargar la planilla para un trabajador de interés pulsamos el botón descargar planilla del registro.
Si se requiere enviar la planilla para un trabajador de interés presionamos el botón enviar planilla del registro.

En la pantalla también muestra los botones descargar todos los registros y enviar todos los registros."""


# ==========================================
# SOLICITUD DE VACACIONES
# ==========================================

def que_contiene_pantalla_solicitud_vacaciones():
    return """Para realizar una solicitud de vacaciones nos dirigimos a esta sección, y enseguida el sistema muestra una pantalla que contiene las secciones “Solicitudes de vacaciones”, y “Solicitudes de suspensión de vacaciones”.

La sección “Solicitudes de vacaciones” contiene una tabla con las columnas: Código, Fecha de la solicitud, Trabajador, Estatus de la Solicitud, Fecha de reincorporación, Motivo del rechazo y Acción que a su vez cuenta con las opciones: Ver información del registro, Suspender vacaciones, Replanificar vacaciones, Modificar Registro, Eliminar, Aceptar Solicitud y Rechazar Solicitud. También muestra los botones “Ir atrás”, “Crear nuevo registro”, “Importar registros” y “Presione para descargar el documento con la información de los registros”."""


def como_crear_solicitud_vacaciones():
    return """Al pulsar la opción “Crear nuevo registro”, el sistema nos presenta un formulario con los siguientes campos: 
- Fecha de la solicitud.
- Organización que este campo lo solicita el sistema solo cuando el usuario posee rol de administrador o rol de talento humano.
- Trabajador,
- Año del periodo vacacional,
- Fecha de inicio de vacaciones
- Y Fecha de culminación de vacaciones.

Al ingresar el año del periodo vacacional, el sistema genera el campo “Días Solicitados”.
Adicionalmente, el sistema muestra la sección: Información del Trabajador, la cual muestra datos como: Nombres, Apellidos, Fecha de ingreso, Cargo, Dependencia, Días de disfrute según antigüedad y Días pendientes. Es importante mencionar que los campos en los que se detalla un asterisco rojo, son de tipo obligatorio.

Ingresamos la información solicitada y pulsamos guardar registros para que el sistema almacene la información y muestre el mensaje: “Registro almacenado con éxito”."""


def como_importar_registros_vacaciones():
    return """El sistema también permite cargar los registros de forma masiva mediante una hoja de cálculo. Para esto, se recomienda primero realizar una Exportación de los registros que se encuentran en el sistema haciendo uso del botón que permite realizar la descarga del archivo. Esto nos permite editar archivo, para agregar tantos registros como requiera, y luego usarlo para realizar una Importación mediante el botón “Importar registros”."""


def como_ver_detalle_solicitud_vacaciones():
    return """Si deseamos ver el detalle del registro solo debemos pulsar sobre el botón Ver información del registro, para lo que el sistema habilita una ventana denominada “Información de la solicitud de vacaciones registrada”, donde se muestran los campos: Código de la solicitud, Fecha de la solicitud, Trabajador, Año del periodo vacacional, Periodo, Días solicitados y Motivo del Rechazo. Para salir de la ventana pulsamos sobre el icono X o sobre el botón “Cerrar”."""


def como_modificar_solicitud_vacaciones():
    return """En caso de requerir modificar la información registrada es necesario que la solicitud no haya sido aprobada o rechazada, para ello solo presionamos sobre el botón de modificar registro y el sistema muestra el formulario de “Solicitud de vacaciones” en forma de edición. Una vez se haya modificado la información de interés, se debe pulsar sobre el botón guardar para lo que el sistema muestra el mensaje “Registro actualizado con éxito”."""


def como_aprobar_solicitud_vacaciones():
    return """Para aprobar la solicitud registrada, nos dirigimos a la columna de acciones y pulsamos sobre el botón “Aceptar solicitud”, seguidamente el sistema muestra una ventana con la interrogante ¿Seguro que desea aprobar esta solicitud? E indica en un mensaje “Una vez aprobada la operación no se podrán realizar cambios en la misma”. Al pulsar sobre el botón guardar, el sistema muestra un mensaje por pantalla que indica que el registro ha sido actualizado con éxito y actualiza el estatus a aprobado."""


def como_rechazar_solicitud_vacaciones():
    return """En caso de requerir rechazar la solicitud, nos dirigimos a la columna de acciones y pulsamos sobre el botón “Rechazar solicitud”, seguidamente el sistema muestra una ventana con la interrogante ¿Seguro que desea Rechazar esta solicitud? y el campo Motivo del rechazo. Al pulsar sobre el botón guardar, el sistema indica que el registro ha sido actualizado con éxito y cambia el estatus a Rechazado."""


def como_eliminar_solicitud_vacaciones():
    return """Para eliminar el registro de la solicitud es necesario que ésta no haya sido aprobada o rechazada previamente, en este caso nos dirigimos a la columna de acciones y pulsamos sobre el botón “Eliminar registro”, seguidamente el sistema muestra una ventana con la interrogante ¿Eliminar registro? Al pulsar sobre el botón Confirmar, el sistema nos muestra un mensaje que indica que el registro ha sido eliminado con éxito y lo retira de la tabla."""


def como_suspender_vacaciones():
    return """Para realizar la acción de suspender vacaciones, el estatus de la solicitud debe estar aprobado, luego pulsamos sobre el botón asociado, y el sistema nos presenta una ventana con los campos: Fecha de suspensión, Días efectivamente disfrutados, Motivo de suspensión y la opción de adjuntar archivos. Al pulsar guardar, el estatus de la solicitud cambia a suspendido, y el sistema lista la información en la tabla “Solicitudes de suspensión de vacaciones”."""


def como_replanificar_vacaciones():
    return """Para realizar la acción de replanificar vacaciones, el estatus de la solicitud debe estar aprobado, luego pulsamos sobre el botón asociado, y el sistema nos presenta una ventana con información del trabajador y los campos para indicar la nueva Fecha de inicio y culminación de vacaciones. Al pulsar guardar, el estatus de la solicitud cambia a replanificado."""


# ==========================================
# SOLICITUD DE PRESTACIONES
# ==========================================

def requisitos_y_pantalla_prestaciones():
    return """Para gestionar ésta solicitud se requiere que previamente se haya configurado la política de prestaciones. Una vez realizada esta configuración, se pulsa sobre la opción Solicitud de prestaciones, para lo que el sistema muestra una pantalla denominada “Solicitudes de adelanto de Prestaciones”, que contiene una tabla con las columnas correspondientes y las acciones: Ver Información del Registro, Modificar Registro, Eliminar Registro y Revisar Solicitud."""


def como_crear_solicitud_prestaciones():
    return """Al pulsar la opción “Crear nuevo registro”, el sistema nos presenta un formulario con los siguientes campos: Fecha de la solicitud, Trabajador, Monto solicitado, y Motivo de adelanto de prestaciones. Adicionalmente, muestra la Información del Trabajador. Luego de ingresar la información solicitada presionamos sobre el botón guardar, a lo que el sistema muestra el mensaje: “Registro almacenado con éxito” y la solicitud toma el estatus de Pendiente."""


def como_ver_detalle_prestaciones():
    return """Si deseamos ver el detalle del registro solo debemos presionar el botón de Ver información del registro, para lo que el sistema habilita una ventana denominada “Información de la solicitud de adelanto de prestaciones registrada”, donde se muestran los campos: Código de la solicitud, Fecha de la solicitud, Trabajador y monto solicitado."""


def como_modificar_prestaciones():
    return """En caso de requerir modificar la información registrada es necesario que la solicitud no haya sido aprobada o rechazada, para ello pulsamos sobre el botón de modificar registro y el sistema muestra el formulario de edición. Una vez modificada la información, presionamos el botón guardar y el sistema muestra el mensaje “Registro actualizado con éxito”."""


def como_eliminar_prestaciones():
    return """Para eliminar el registro de la solicitud es necesario que ésta no haya sido aprobada o rechazada previamente, pulsamos sobre el botón “Eliminar registro” y confirmamos la acción en la ventana emergente. El sistema indicará que el registro ha sido eliminado con éxito."""


def como_revisar_prestaciones():
    return """Para aprobar o rechazar la solicitud, pulsamos sobre el botón “Revisar solicitud”, el sistema muestra una ventana con los detalles y un selector de estatus (Aprobado o Rechazado). Si se aprueba, se indica la Fecha de aprobación; si se rechaza, se indica el Motivo. Al guardar, el estatus cambia y se bloquean las acciones de edición y eliminación."""


# ==========================================
# SOLICITUD DE PERMISOS
# ==========================================

def requisitos_y_pantalla_permisos():
    return """Para gestionar ésta solicitud se requiere que previamente se haya configurado la política de permisos. Al pulsar sobre la opción Solicitud de permisos, el sistema muestra una tabla con las columnas: Trabajador, Motivo del permiso, Estatus de la solicitud y Acción (Ver, Modificar, Eliminar, Aceptar solicitud y Rechazar solicitud)."""


def como_crear_solicitud_permisos():
    return """Al presionar la opción “Crear nuevo registro”, el sistema nos presenta un formulario con los campos: Fecha de la solicitud, Trabajador, Tipo de permiso, Periodo del permiso (Desde - Hasta), Tiempo de permiso y motivo del permiso. Luego de ingresar la información, presionamos guardar y el sistema indica “Registro almacenado con éxito”, quedando la solicitud en estatus Pendiente."""


def como_ver_detalle_permisos():
    return """Si deseamos ver el detalle del registro solo debemos pulsar sobre el botón de Ver información del registro, que habilita una ventana denominada “Información de la solicitud de permisos” con todos los datos ingresados previamente."""


def como_modificar_permisos():
    return """En caso de modificar la información registrada es necesario que la solicitud no haya sido aprobada o rechazada. Al presionar sobre el botón de modificar registro, el sistema muestra el formulario en formato de edición. Al guardar los cambios, se mostrará el mensaje “Registro actualizado con éxito”."""


def como_aprobar_permisos():
    return """Para aprobar la solicitud registrada, pulsamos sobre el botón “Aceptar solicitud”, seguidamente el sistema muestra un mensaje indicando que el registro ha sido actualizado con éxito, cambia el estatus a aprobado y bloquea las acciones de modificar, eliminar, aprobar o rechazar."""


def como_rechazar_permisos():
    return """Si se requiere Rechazar la solicitud, solo debemos seleccionar el botón de rechazar solicitud, para lo que el sistema responderá indicando que el registro se ha actualizado con éxito, cambiará el estatus a Rechazado y bloqueará las demás acciones."""


def como_eliminar_permisos():
    return """Para eliminar el registro de la solicitud es necesario que ésta no haya sido aprobada o rechazada previamente. Pulsamos sobre el botón “Eliminar registro” y confirmamos en la ventana emergente para que el sistema retire el registro de la tabla."""