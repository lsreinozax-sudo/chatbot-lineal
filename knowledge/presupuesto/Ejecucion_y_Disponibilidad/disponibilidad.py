def disponibilidad_presupuestaria():
    return """En el submódulo Disponibilidad Presupuestaria, los registros provienen de compras o Talento Humano. El sistema muestra filtros y una tabla con: Código del requerimiento, Descripción, Moneda, Estatus y Acción.

Para gestionarla, se presiona Completar solicitud presupuestaria. El formulario varía según el origen:
• Talento Humano: Muestra Código, Nombre, Periodo y Tipo de pago.
• Compras: Muestra Fecha, Descripción, y detalles técnicos del requerimiento (cantidad, precio, IVA).

En ambos casos, en la sección Cuentas presupuestarias de gastos, se pulsa "Agregar cuenta presupuestaria", se selecciona la Acción Especifica, la Cuenta y el Monto, y se agrega. Para solicitudes de Compras, tras agregar las cuentas, se debe pulsar "Hay Disponibilidad" (cambia el estatus a Por aprobar) o "No hay Disponibilidad" (cambia a No disponible).

Posteriormente, las disponibilidades "Por aprobar" deben validarse con el botón Aprobar disponibilidad presupuestaria, cambiando el estatus a "Aprobado(A)". Los registros permiten ser visualizados, impresos (PDF), modificados (solo si no están aprobados) o eliminados."""