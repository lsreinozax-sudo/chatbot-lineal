def creditos_adicionales_mejor_vision():
    return """En el submódulo Modificaciones -> Listado de Créditos Adicionales/Mejor Visión, se presenta una tabla con Fecha, Código Acción Especifica, Descripción, Documento, Estatus y Acción.

Para crearlo, el formulario solicita: Fecha, Institución, Moneda, Nro. Documento, Documento (archivo adjunto) y Descripción. En la sección Cuentas Presupuestarias, se agregan cuentas ingresando Acción Especifica, Cuenta y Monto.

Los registros nacen como "Pendiente". Se deben validar con el botón Aprobar registro, pasando a "Aprobado". Cuentan con opciones de Ver, Imprimir (PDF), Modificar y Eliminar."""

def reducciones():
    return """En Modificaciones -> Listado de Reducciones, se muestra la tabla de registros. El proceso de creación es idéntico al de Créditos Adicionales: se llena Fecha, Institución, Moneda, Nro. Documento, archivo adjunto y Descripción.

Se agregan las cuentas presupuestarias de gastos a reducir especificando Acción Especifica, Cuenta y Monto. Requieren ser aprobadas mediante el botón Aprobar registro para hacer efectiva la reducción de los montos, cambiando su estatus a "Aprobado". Permiten las acciones de visualizar, imprimir, modificar y eliminar."""

def traspasos():
    return """En Modificaciones -> Listado de Traspasos, se lista la información en la tabla principal. La creación (Crear nuevo registro) pide: Fecha, Institución, Moneda, Nro. Documento, adjunto y Descripción.

La sección de Cuentas Presupuestarias varía; se divide en dos:
• Cuentas Cedentes (Origen): Se indica Acción Especifica, Cuenta y Monto a debitar.
• Cuentas a Acreditar (Destino): Se indica Acción Especifica y Cuenta que recibirá el monto.

Los traspasos en estatus Pendiente deben ser aprobados para generar la transferencia de montos entre cuentas. Una vez confirmados mediante Aprobar registro, el estatus cambia a Aprobado. Cuentan con las opciones estándar de Acción (Ver, Modificar, Eliminar, Imprimir PDF)."""