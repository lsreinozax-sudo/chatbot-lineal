"""Aplicación base del ERP KAVAC sobre la barra de navegación superior"""

def que_se_presenta_en_la_barra_de_navegacion_superior():
    return "El sistema nos presenta la pantalla principal, donde conseguimos una barra de navegación superior, donde se presenta lo siguiente: 1) Logo del sistema 2) Botón • Si presionamos el botón, el sistema despliega el menú de los módulos a la izquierda del mismo, mostrando los iconos del sistema. 3) Notificaciones 4) Respaldar base de datos 5) Pantalla completa 6) Mi configuración y datos"

def que_se_puede_hacer_en_la_seccion_de_respaldar_base_de_datos():
    return "Esta sección nos permite realizar un respaldo completo de la base de datos del sistema. Presionamos el icono de respaldo de base de datos, el sistema nos presenta una pantalla de administración de respaldos, un campo para la búsqueda de información, y el botón para Nuevo."

def que_sucede_al_presionar_nuevo_respaldo():
    return "Si presionamos Nuevo, el sistema carga en la tabla de registros un respaldo de los datos del sistema."

def que_columnas_tiene_la_tabla_de_respaldos():
    return "La tabla de registros está formada por las siguientes columnas: Archivo (Indica el nombre del archivo el cual está en formato .zip), Tamaño (indica el tamaño del archivo generado), Fecha (Indica la fecha y la hora en la que se generó el archivo de respaldo); seguidamente el sistema presenta tres opciones: Descargar Datos, Restaurar Datos el cual al seleccionarlo nos muestra un mensaje donde menciona que este proceso puede ocasionar pérdida parcial o total de los datos y nos da las opciones de Cancelar y Restaurar, y finalmente esta la opción de Eliminar que permite eliminar el respaldo de base de datos."

def que_permite_la_seccion_pantalla_completa():
    return "Esta sección permite que el sistema se ejecute en pantalla completa."

def que_opciones_despliega_mi_configuracion_y_datos():
    return "Al pulsar esta opción el sistema despliega un menú con las siguientes opciones: 1) Configurar Cuenta 2) Mi Perfil 3) Bloquear Pantalla 4) Ayuda 5) Salir."

def que_permite_configurar_la_seccion_general_de_configurar_cuenta():
    return "La sección General, permite configurar el bloqueo de la pantalla, la cual se realiza mediante un switch y un campo de tiempo de inactividad en minutos, seguidamente de los botones, borrar datos, cancelar y remplazar, y Guardar Registro."

def que_permite_la_seccion_notificaciones_de_configurar_cuenta():
    return "La sección Notificaciones, nos permite activar las notificaciones por defecto del sistema, realizando el proceso mediante switches, que reflejan los procesos."

def que_se_presenta_en_mi_perfil():
    return "En \"Mi Perfil\", el sistema presenta una pantalla la cual nos permite configurar la cuenta de usuario; para esto, se presenta un icono donde se puede cargar la imagen de usuario; seguidamente se presentan 3 secciones: 1) En la sección Perfil, se presentan los campos asociados al usuario a saber: Nombre y Apellido, Cargo, Correo Electrónico, Usuario; además se presentan dos campos de texto, los cuales nos permiten cambiar la contraseña cuando el usuario lo desee y en la parte posterior puede apreciar el nivel de seguridad de la contraseña. 2) En la Sección Actividad, se nos presenta los últimos 20 registros que ha realizado el usuario dentro del sistema. 3) En la Sección Directorio, nos presenta el directorio de usuario dentro del sistema."

def que_sucede_al_seleccionar_bloquear_pantalla():
    return "Bloquear Pantalla: al seleccionar esta opción el sistema nos presenta una ventana emergente, donde muestra el nombre del usuario y solicita ingresar la contraseña para desbloquear la pantalla."

def que_hace_la_opcion_ayuda():
    return "Ayuda: el sistema redirecciona al usuario a otra pestaña presentando el manual de usuario del sistema."

def que_hace_la_opcion_salir():
    return "Salir: el sistema nos presenta una ventana emergente donde se pregunta al usuario si está seguro de salir de la aplicación."