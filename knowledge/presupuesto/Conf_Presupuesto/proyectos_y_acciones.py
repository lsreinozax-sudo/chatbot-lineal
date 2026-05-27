def proyectos():
    return """Si ingresamos a Proyectos dentro de Configuración, el sistema muestra el campo Buscar y un listado en tabla con las columnas: Código, Proyectos, Activo y Acción (Ver detalles, Modificar, Eliminar).

Para crear un nuevo proyecto, presionamos Crear nuevo registro. El formulario solicita: Institución, Dependencia (registradas en Aplicación Base), Responsable (del módulo de Talento Humano), Cargo de Responsable (auto-completado), Código, Nombre, Fecha de Inicio, Fecha de Finalización, Activo (switch) y Descripción. Cuenta con los botones Borrar, Cancelar y Guardar.

La información registrada se visualiza en la tabla de listado. El botón Ver registro muestra información detallada, Modificar registro permite la edición y Eliminar registro borra la entrada previa confirmación."""

def acciones_centralizadas():
    return """Si ingresamos a Acciones Centralizadas, el sistema muestra el campo Buscar y un listado en tabla con: Código, Acción Centralizada, Activa y Acción.

Para crear una nueva, presionamos Crear nuevo registro. Solicitudes del formulario: Institución, Dependencia, Responsable, Cargo de Responsable, Código de la acción centralizada, Nombre, Fecha de inicio, Fecha de finalización, Activo (switch) y Descripción. Cuenta con los botones Borrar, Cancelar y Guardar.

El registro se lista en la tabla principal y cuenta con las opciones de Ver registro, Modificar registro y Eliminar registro, funcionando bajo la misma lógica estándar del sistema."""

def acciones_especificas():
    return """Al ingresar a Acciones Especificas, el sistema muestra el campo Buscar y una tabla con: Código, Acción Especifica, Proyecto/Acción Centralizada, Activa y Acción.

Para crear, presionamos Crear nuevo registro. El formulario solicita:
• Proyecto (switch para desplegar lista) o Acción Centralizada (switch para desplegar lista). Nota: El registro se hace por una u otra opción.
• Fecha de inicio y Fecha de finalización.
• Código, Nombre, Activo (switch) y Descripción.

Cuenta con botones Borrar, Cancelar y Guardar. Se aplican las mismas funcionalidades de Ver, Modificar y Eliminar registro desde la columna Acción de la tabla."""