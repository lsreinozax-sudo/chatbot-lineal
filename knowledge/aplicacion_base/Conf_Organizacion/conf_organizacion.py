"""Aplicación base del ERP KAVAC sobre la configuracion de las organizaciones"""


def que_datos_basicos_solicita_el_sistema_en_configurar_organizacion():
    return "Datos Básicos, el sistema solicita los datos: RIF: Nombre: Acrónimo (Nombre corto): Razón social: País: Estado: Municipio: Ciudad: Código postal: Fecha de inicio de operaciones: 1 Sectores económicos: Tipo de organización: Dirección fiscal:"

def que_switches_se_presentan_en_configurar_organizacion():
    return "Switch Activa: SI Switch Organización por defecto: Si activamos este botón, el sistema tomara la organización por defecto, y mostrara los datos de esta organización para los reportes que genera el sistema. Switch Agente de retención: al activar este botón, se le estará indicando al sistema que la organización es agente de retención de IVA, y esta configuración afecta los módulos de contabilidad, finanzas y compras."

def que_datos_complementarios_solicita_el_sistema_en_configurar_organizacion():
    return "En la Sección Datos Complementarios, el sistema solicita los datos: Base legal: Forma jurídica: Actividad principal: Misión: Visión: Composición de patrimonio: los campos de esta sección se dejan en blanco dado que no son requeridos."

def que_botones_muestra_al_final_el_formulario_de_configurar_organizacion():
    return "Finalmente, el sistema nos muestra los botones Borrar datos del formulario, Cancelar y regresar, y Guardar registro."

def que_sucede_al_guardar_la_organizacion():
    return "Pulsamos Guardar para que el sistema registre la organización. Seguidamente, el sistema muestra que el registro se almaceno con éxito, y apreciamos una tabla de registros con la información suministrada con los campos: Logo, RIF, Nombre, Activa y Acción, que a su vez nos presenta los botones Ver y Modificar."

def que_funcionalidades_tiene_la_tabla_de_organizaciones():
    return "Esta tabla también cuenta con un paginador, un buscador y un selector de número de registros a mostrar en la tabla."

def como_se_ve_la_informacion_de_una_organizacion():
    return "Si deseamos ver información de una organización, pulsamos el botón Ver para un registro de interés, inmediatamente el sistema presenta una ventana que nos muestra información detallada de la organización registrada previamente."

def como_se_edita_una_organizacion():
    return "Para editar información de una organización, presionamos el botón Modificar registro, inmediatamente el sistema nos presenta la información ingresada previamente, modificamos la información requerida, y presionamos Guardar."

def que_mensaje_muestra_al_actualizar_organizacion():
    return "Luego, el sistema nos muestra un mensaje de que la información se actualizo con éxito, y renueva la tabla de registro."

def que_sucede_al_configurar_la_organizacion():
    return "Una vez configurada la organización podremos ver que el menú principal de la aplicación cambia un poco ya que se activa el menú de cada módulo del sistema y ya estás listo para iniciar tu gestión en el sistema."
