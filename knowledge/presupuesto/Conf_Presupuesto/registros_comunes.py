def fuentes_de_financiamiento():
    return """En la sección de Registros comunes, al ingresar al formulario Fuentes de Financiamiento, el sistema muestra una tabla que contempla los registros cargados por defecto. Esta tabla contiene las columnas: Nombre y Acción (Editar o Eliminar).
    
En caso de ser necesario, podemos realizar un registro manual ingresando el Nombre. El formulario presenta los botones: “Cerrar” (salir de ventana), “Cancelar” (limpiar formulario) y “Guardar” (almacena datos). Si omitimos un campo obligatorio (* rojo), aparece el mensaje “El campo X es obligatorio”. Al guardar, visualizamos “Registro almacenado con éxito”.

Si pulsamos Modificar registro en la columna Acción, el sistema muestra la información en forma de edición. Actualizamos los campos de interés y guardamos (“Registro actualizado con éxito”). Para eliminar, pulsamos Eliminar registro, confirmamos en el mensaje emergente y el sistema elimina el registro."""

def tipos_de_financiamiento():
    return """Al ingresar al formulario Tipos de Financiamiento, el sistema muestra una tabla que contempla los registros por defecto con las columnas: Fuente de Financiamiento, Tipo de Financiamiento y Acción.

Para un registro manual, el sistema solicita:
• Fuente de financiamiento (campo de selección con las fuentes previamente registradas).
• Tipo de Financiamiento.

El formulario cuenta con los botones “Cerrar”, “Cancelar” y “Guardar”. Se aplican las mismas validaciones de campos obligatorios y los mismos procesos para modificar o eliminar un registro detallados en Fuentes de Financiamiento."""

def categoria_de_cuentas():
    return """Al ingresar al formulario Categoría de Cuentas, el sistema muestra una tabla con las categorías cargadas por defecto, con las columnas: Nombre y Acción.

Para un registro manual, se ingresa el Nombre. El formulario cuenta con los botones “Cerrar”, “Cancelar” y “Guardar”. Posee las mismas validaciones de campos obligatorios y los mismos pasos para Modificar y Eliminar un registro, mostrando los respectivos mensajes de éxito o confirmación."""