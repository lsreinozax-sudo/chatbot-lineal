def hoja_tiempo_introduccion():
    return "Se describen los pasos requeridos para realizar el proceso de registro en la funcionalidad de hoja de tiempo del módulo de talento humano."

def hoja_tiempo_descripcion_funcionalidad():
    return "Esta Funcionalidad nos permite que se indica como supervisor de un determinado grupo de supervisados, registrar la cantidad de parámetros o variables que alimentan el procesamiento de nómina como hora extras, turnos diurnos, turnos nocturnos, entre otros, que efectivamente ha cumplido el grupo de supervisados."

def hoja_tiempo_roles_usuarios():
    return "Es importante precisar que los usuarios indicados como supervisores y aprobadores solo pueden ver la información asociada a su grupo de supervisados. El usuario con rol de talento humano puede consultar la información de todos los grupos de supervisados. Cada registro y cada aprobación es notificada por el sistema a los correos de usuarios que correspondan. El sistema cuenta con dos niveles de aprobación en los registros que se realicen, esto mediante las operaciones de Aprobar y Confirmar."

def hoja_tiempo_requisitos():
    return "Para esto es necesario poseer los permisos requeridos para acceder a esta funcionalidad. También, se requiere que previamente se hayan realizado registros de información en las funcionalidades de parámetros globales, grupo de supervisados parámetros de hoja de tiempo, y en caso de que la organización requiera que la carga de hoja de tiempo en periodo activo se realice mediante el esquema de guardias, es necesario que se realice dicho proceso."

def hoja_tiempo_requisitos_procesamiento_nomina():
    return "Para que posteriormente el procesamiento de nómina se alimente de los parámetros cargados en la hoja de tiempo, se requiere que los registros asociados a estas posean el mismo periodo de la nómina a ejecutar, el estatus de estos registros debe ser “Cerrado”, y en la configuración del módulo, específicamente en el formulario de parámetros de hoja de tiempo debe estar asociada la nómina en cuestión."

def hoja_tiempo_acceso():
    return "Para ilustrar el proceso de registro, ingresamos al sistema con las credenciales de acceso suministradas por el administrador del sistema, luego nos dirigimos al panel lateral izquierdo y pulsamos sobre el módulo de talento humano y el sistema nos muestra los submódulos: Configuración, ajustes en tablas salariales, expediente, esquema de guardias, hoja de tiempo, registros de nómina, registro ari, archivo txt de nómina, solicitudes y reportes."

def hoja_tiempo_submenu():
    return "Luego pulsamos sobre Hoja de tiempo, y el sistema nos presenta a su vez las opciones: periodo activo y pendientes."