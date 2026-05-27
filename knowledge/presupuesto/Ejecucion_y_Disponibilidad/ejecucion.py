def ejecucion_compromisos():
    return """En el submódulo Ejecución, en la opción Compromisos, se muestran filtros y una tabla con: Fecha, Código, Documento de Origen, Código de Acción Especifica, Descripción, Estatus y Acción.

Para crear uno, se presiona Crear nuevo registro. El formulario pide: Institución, Fecha y Documento de Origen. 
• Si se ingresa un dato manual en Documento Origen, se despliega la sección Beneficiario (Nombre y Cuenta contable que se autocompleta).
• Si se pulsa "Buscar Documento", se abre una ventana para seleccionar un documento previo, cargando sus datos automáticamente.

En Cuentas presupuestarias de gastos, se pulsa Agregar cuenta presupuestaria para añadir Acción Especifica, Cuenta, Concepto, Monto e Impuesto (uno por uno). La sección "Cuentas presupuestarias de impuestos" se autocompleta.

Los compromisos nacen con estatus "Pendiente". Para validarlos, se pulsa Aprobar registro, pasando a "Aprobado(a)". Pueden verse, modificarse (solo pendientes), imprimirse en PDF o anularse (botón Anular registro, indicando motivo de anulación), liberando el compromiso asociado y cambiando el estatus a "Anulado(a)"."""