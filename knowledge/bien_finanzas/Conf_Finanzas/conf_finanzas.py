

def que_secciones_tiene_configuracion():
    return "Al ingresar al sub-módulo de Configuración, el sistema muestra una pantalla que contiene las secciones: Formatos de códigos y Registros comunes."

def bancos():
    return "Al ingresar al formulario Bancos, el sistema muestra una tabla que contempla los registros de los bancos que vienen cargados por defecto."

def formato_codigos():
    return "Tal como se detalla en el texto de guía, se debe seguir el formato: prefijos-dígitos-año y se deben tener activas las mayúsculas."

def que_formatos_codigos_se_deben_ingresar():
    return "Movimiento bancario, Conciliación bancaria, Orden de pago, Ejecución de pagos"

def generacion_automatica_codigos():
    return "Es importante precisar que a partir del formato establecido, el sistema genera de forma automática y secuencial los códigos de estos registros."

def ejemplo_generacion_codigo():
    return "Es decir, que si para el proceso de registro de movimiento bancario se establece el código MOB, seguido de 8 ceros, seguido de 4 letras “Y”, el sistema le asignara el código MOB-1-2024 al primer registro, si se ingresa en dicho año."

def guardar_formatos_codigos():
    return "Luego de ingresar los formatos de códigos solicitados, pulsamos el botón Guardar, y el sistema muestra el mensaje: “Registro almacenado con éxito”. Una vez guardado, el sistema no permite editar la información para ningún tipo de usuario."

def que_opciones_tiene_registros_comunes():
    return "Banco, Agencias bancarias, Tipos de cuenta, Cuentas bancarias y Formas de pago."

def formulario_bancos_tabla_columnas():
    return "Logo, Código, Nombre abreviado, Descripción, Sitio web, Y Acción, donde tenemos los botones Modificar o Eliminar."

def registro_formulario_manual_campos_bancos():
    return "Logo, en el cual pulsamos el recuadro imagen, que levanta una ventana donde podemos buscar el archivo correspondiente, El código del banco, El nombre abreviado, que es el acrónimo del banco, Nombre, Y el sitio web."

def formulario_botones_bancos():
    return "“Cerrar”, que permite salir de esta ventana, “Cancelar”, permite limpiar el formulario, Y “Guardar” -que almacena los datos que se ingresan-"

def formulario_campo_bancos_obligatorio_omitido():
    return "Si omitimos un campo obligatorio, marcado con un asterisco rojo, aparece el mensaje “El campo X es obligatorio”."

def formulario_bancos_guardar_exito():
    return "Al guardar, debemos visualizar el mensaje: “Registro almacenado con éxito” y se lista en la tabla de registros."

def formulario_bancos_modificar_registro():
    return "Si pulsamos el botón Modificar registro ubicado en la columna Acción, para un registro de interés, el sistema nos muestra que la información fue cargada en forma de edición en la parte superior de la ventana. Actualizamos aquellos Campos que sean de interés y pulsamos el botón guardar. El sistema muestra el mensaje “Registro actualizado con éxito”."

def formulario_bancos_eliminar_registro():
    return "Para eliminar un registro, presionamos el botón Eliminar registro” El sistema nos muestra el mensaje: ¿Está seguro de eliminar este registro?, junto con las opciones: “Cancelar” y “Confirmar”. Si presionamos la opción “Confirmar”, el sistema muestra el mensaje “Registro eliminado con éxito”. Si pulsamos la opción “Cancelar”, el sistema no ejecuta ninguna acción."

def formulario_agencias_bancarias_campos():
    return "El switch Sede principal, donde podemos indicar si el banco que estamos registrando es sede principal o no, Los campos País, Estado y Ciudad (previamente ingresados en registros comunes), Banco (ya configurados en el formulario Bancos), Nombre de la agencia, Persona de contacto, Correo del contacto, Y Descripción"

def formulario_agencias_bancarias_numeros_telefonicos():
    return "En la sección Números Telefónicos al pulsar el botón más (+) el sistema solicita indicar si es móvil, teléfono o fax, el código de área, número y extensión. Si volvemos a pulsar el botón más (+), podemos añadir números telefónicos adicionales. También podemos eliminarlos al pulsar el botón menos (-)."

def formulario_agencias_bancarias_botones():
    return "“Cerrar”, que permite salir de esta ventana, “Cancelar”, permite limpiar el formulario, Y “Guardar” -que almacena los datos que se ingresan-"

def formulario_agencias_campo_obligatorio_omitido():
    return "Si omitimos un campo obligatorio, marcado con un asterisco rojo, aparece el mensaje “El campo X es obligatorio”."

def formulario_agencias_guardar_exito():
    return "Al guardar, debemos visualizar el mensaje: “Registro almacenado con éxito”."

def formulario_agencias_tabla_columnas():
    return "Banco, Ciudad, Agencia bancaria, Dirección, Sede principal, Números telefónicos, Y Acción, esta tiene los botones “Modificar” y “Eliminar registro”."

def formulario_agencias_modificar_registro():
    return "Si pulsamos el botón Modificar registro ubicado en la columna Acción, para un registro de interés, el sistema nos muestra que la información fue cargada en forma de edición en la parte superior de la ventana. Actualizamos aquellos Campos que sean de interés y pulsamos el botón guardar. El sistema muestra el mensaje “Registro actualizado con éxito”."

def formulario_agencias_eliminar_registro():
    return "Para eliminar un registro, presionamos el botón Eliminar registro” El sistema nos muestra el mensaje: ¿Está seguro de eliminar este registro?, junto con las opciones: “Cancelar” y “Confirmar”. Si presionamos la opción “Confirmar”, el sistema muestra el mensaje “Registro eliminado con éxito”. Si pulsamos la opción “Cancelar”, el sistema no ejecuta ninguna acción."

def formulario_tipos_cuenta_campos():
    return "el sistema muestra una ventana con los campos: Nombre y Código. Aquí podemos asignar el código asociado a este tipo de cuenta."

def formulario_tipos_cuenta_botones():
    return "“Cerrar”, que permite salir de esta ventana, “Cancelar”, permite limpiar el formulario, Y “Guardar” -que almacena los datos que se ingresan-"

def formulario_tipos_cuenta_campo_obligatorio_omitido():
    return "Si omitimos un campo obligatorio, marcado con un asterisco rojo, aparece el mensaje “El campo X es obligatorio”."

def formulario_tipos_cuenta_guardar_exito():
    return "Al guardar, debemos visualizar el mensaje: “Registro almacenado con éxito”."

def formulario_tipos_cuenta_tabla_columnas():
    return "Nombre, Código, Acción, que contiene los botones “Modificar registro” y “Eliminar”."

def formulario_tipos_cuenta_modificar_registro():
    return "Si pulsamos el botón Modificar registro ubicado en la columna Acción, para un registro de interés, el sistema muestra la información que cargada en forma de edición en la parte superior de la ventana. Actualizamos aquellos Campos que sean de interés y pulsamos el botón guardar. El sistema muestra el mensaje “Registro actualizado con éxito”."

def formulario_tipos_cuenta_eliminar_registro():
    return "Para eliminar un registro, pulse el botón Eliminar registro. El sistema muestra el mensaje: ¿Está seguro de eliminar este registro?, junto con las opciones: “Cancelar” y “Confirmar”. Si el usuario pulsa la opción “Confirmar”, el sistema muestra el mensaje “Registro eliminado con éxito”. Si se pulsa la opción “Cancelar”, el sistema no ejecuta ninguna acción."

def formulario_cuentas_bancarias_campos():
    return "Fecha de apertura, Cuenta contable (previamente registrada en el módulo de contabilidad), Banco (ya configurados en el formulario Bancos), Agencia (ya configurados en el formulario Agencias Bancarias), Tipo de cuenta (que fue configurado en el formulario Tipos de Cuentas), Código cuenta cliente, donde ingresamos el número de cuenta del banco, Y una breve descripción de esta cuenta bancaria."

def formulario_cuentas_bancarias_botones():
    return "“Cerrar”, que permite salir de esta ventana, “Cancelar”, permite limpiar el formulario, Y “Guardar” -que almacena los datos que se ingresan-"

def formulario_cuentas_bancarias_campo_obligatorio_omitido():
    return "Si omitimos un campo obligatorio, marcado con un asterisco rojo, aparece el mensaje “El campo X es obligatorio”."

def formulario_cuentas_bancarias_guardar_exito():
    return "Al guardar, debemos visualizar el mensaje: “Registro almacenado con éxito”."

def formulario_cuentas_bancarias_tabla_columnas():
    return "Banco, Código de cuenta del cliente, Fecha de apertura, Y Acción, con los botones Modificar y Eliminar."

def formulario_cuentas_bancarias_modificar_registro():
    return "Si pulsamos el botón Modificar registro ubicado en la columna Acción, para un registro de interés, el sistema nos muestra que la información fue cargada en forma de edición en la parte superior de la ventana. Actualizamos aquellos Campos que sean de interés y pulsamos el botón guardar. El sistema muestra el mensaje “Registro actualizado con éxito”."

def formulario_cuentas_bancarias_eliminar_registro():
    return "Para eliminar un registro, presionamos el botón Eliminar registro” El sistema nos muestra el mensaje: ¿Está seguro de eliminar este registro?, junto con las opciones: “Cancelar” y “Confirmar”. Si presionamos la opción “Confirmar”, el sistema muestra el mensaje “Registro eliminado con éxito”. Si pulsamos la opción “Cancelar”, el sistema no ejecuta ninguna acción."

def formulario_formas_pago_campos():
    return "Esta tabla cuenta con las columnas: Nombre, Descripción y Acción, con los botones Modificar y Eliminar."

def formulario_formas_pago_botones():
    return "“Cerrar”, que permite salir de esta ventana, “Cancelar”, permite limpiar el formulario, Y “Guardar” -que almacena los datos que se ingresan-"

def formulario_formas_pago_campo_obligatorio_omitido():
    return "Si omitimos un campo obligatorio, marcado con un asterisco rojo, aparece el mensaje “El campo X es obligatorio”."

def formulario_formas_pago_guardar_exito():
    return "Al guardar, debemos visualizar el mensaje: “Registro almacenado con éxito”."

def formulario_formas_pago_tabla_columnas():
    return "Nombre, Descripción y Acción, con los botones Modificar y Eliminar."

def formulario_formas_pago_modificar_registro():
    return "Si pulsamos el botón Modificar registro ubicado en la columna Acción, para un registro de interés, el sistema nos muestra que la información fue cargada en forma de edición en la parte superior de la ventana. Actualizamos aquellos Campos que sean de interés y pulsamos el botón guardar. El sistema muestra el mensaje “Registro actualizado con éxito”."

def formulario_formas_pago_eliminar_registro():
    return "Para eliminar un registro, presionamos el botón Eliminar registro” El sistema nos muestra el mensaje: ¿Está seguro de eliminar este registro?, junto con las opciones: “Cancelar” y “Confirmar”. Si presionamos la opción “Confirmar”, el sistema muestra el mensaje “Registro eliminado con éxito”. Si pulsamos la opción “Cancelar”, el sistema no ejecuta ninguna acción."