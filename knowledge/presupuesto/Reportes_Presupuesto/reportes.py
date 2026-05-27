def reporte_mayor_analitico():
    return """En el submódulo Reportes -> Mayor Analítico, el sistema permite filtrar por: Tipo de reporte (Detallado o Acumulado), Proyecto o Acción Centralizada (con opción de seleccionar todas sus acciones específicas), Acción Específica, Partida Presupuestaria y periodo (Desde/Hasta).
Se puede "Generar reporte" (envía PDF al correo) o "Exportar reporte" (hoja de cálculo). Incluye banner, QR, detalles fiscales y la tabla con: Fecha, Código, Denominación, Detalle, Asignado, Aumento, Disminución, Modificado, Comprometido, Causado, Pagado y Disponible."""

def reporte_disponibilidad_presupuestaria():
    return """En Reportes -> Disponibilidad Presupuestaria, se filtra por: Todas las acciones/proyectos (switch), Proyecto específico o Acción Centralizada, Acción Específica, Partida y rango de fechas (Desde/Hasta). 
Al presionar "Generar reporte", se crea un documento PDF con banner, QR, detalles institucionales y la tabla: Acción/Proyecto, Acción Especifica, Código, Denominación y Disponibilidad Presupuestaria."""

def reporte_presupuesto_formulado():
    return """En Reportes -> Presupuesto Formulado, los filtros son: Año de Formulación, Proyecto o Acción Centralizada, Acción Específica y periodo (Desde/Hasta).
Al "Generar reporte", entrega un PDF con el presupuesto asignado, Moneda, Total Formulado y una tabla con la distribución: Código, Denominación, Total Año y los meses de Enero a Diciembre."""

def reporte_consolidado():
    return """En Reportes -> Consolidado, los filtros permiten selección múltiple o "Todos" para: Proyecto, Acción Centralizada, Acción Específica, Cuentas (catálogo) y fechas (Desde/Hasta).
Al "Generar reporte", el sistema descarga una hoja de cálculo con la estructura: Código presupuestario del ente, Denominación, Órgano de adscripción, Fecha, Mes, Código/denominación de la categoría, y las columnas con las variaciones mes a mes."""

def reporte_compromisos():
    return """En Reportes -> Compromisos, se puede filtrar por: Todos (switch), Estatus (Pendiente, Aprobado, Causado, Pagado, Anulado), Proyecto o Acción Centralizada, Acción Específica y periodo (Desde/Hasta).
Permite "Generar reporte" (PDF) o "Exportar reporte" (hoja de cálculo). Su estructura detalla: Institución, Año Fiscal y la tabla de registros: Fecha de generación, Código del compromiso, Documento Origen, Código de la acción específica, Descripción, Estatus y Monto."""