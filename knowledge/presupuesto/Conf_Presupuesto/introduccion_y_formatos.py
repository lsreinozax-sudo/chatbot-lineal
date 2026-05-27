"""Conocimiento básico sobre presupuesto"""

def introduccion_modulo_presupuesto():
    return """El proceso de configuración permite a la organización adaptar el módulo de Presupuesto según sus necesidades y características. 
Para esto es necesario que el usuario posea los permisos requeridos para cada una de las funcionalidades que componen esta sección. También, se requiere que previamente se hayan realizado registros de información en la configuración general del sistema y en el módulo de Talento Humano, dado que este alimenta diferentes formularios de este módulo.

Para acceder, se ingresa al sistema con las credenciales suministradas por el administrador y nos dirigimos al módulo de Presupuesto, el cual despliega un menú con los sub-módulos: Configuración, Clasificador Presupuestario, Formulaciones, Disponibilidad Presupuestaria, Modificaciones, Ejecución y Reportes.

Al ingresar al sub-módulo de Configuración, el sistema muestra una pantalla con las secciones: Formatos de códigos, Registros comunes, Proyectos, Acciones Centralizadas y Acciones Específicas."""

def formatos_de_codigos():
    return """Tal como se detalla en el texto de guía, se debe seguir el formato: prefijos-digitos-año y se deben tener activas las mayúsculas. 
Primero debemos ingresar los formatos de códigos asociados a:
• Formulación
• Compromiso
• Causado
• Pagado
• Traspaso
• Reducción
• Crédito Adicional
• Disponibilidad Presupuestaria Manual

Es importante precisar que a partir del formato establecido, el sistema genera de forma automática y secuencial los códigos de estos registros. Es decir, que si para el proceso de registro de formulación se establece el código FOR, seguido de 8 ceros, seguido de 4 letras “Y”, el sistema le asignara el código FOR-1-2024 al primer registro, si se ingresa en dicho año.

Luego de ingresar los formatos solicitados, pulsamos el botón Guardar, y el sistema muestra el mensaje: “Registro almacenado con éxito”. Una vez guardado, el sistema no permite editar la información para ningún tipo de usuario."""