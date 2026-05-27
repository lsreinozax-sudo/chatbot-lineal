ROUTES = [
    # (keyword, modulo, funcion, sugerencias)

    # === REPORTES ===
    ("reporte mayor analitico", "knowledge.presupuesto.Reportes_Presupuesto.reportes", "reporte_mayor_analitico", [
        "reporte disponibilidad presupuestaria", "reporte consolidado", "traspasos"
    ]),
    ("reporte disponibilidad presupuestaria", "knowledge.presupuesto.Reportes_Presupuesto.reportes", "reporte_disponibilidad_presupuestaria", [
        "disponibilidad presupuestaria", "reporte mayor analitico", "reporte presupuesto formulado"
    ]),
    ("reporte presupuesto formulado", "knowledge.presupuesto.Reportes_Presupuesto.reportes", "reporte_presupuesto_formulado", [
        "formulacion de presupuesto", "reporte consolidado"
    ]),
    ("reporte consolidado", "knowledge.presupuesto.Reportes_Presupuesto.reportes", "reporte_consolidado", [
        "reporte mayor analitico", "reporte presupuesto formulado", "reporte compromisos"
    ]),
    ("reporte compromisos", "knowledge.presupuesto.Reportes_Presupuesto.reportes", "reporte_compromisos", [
        "ejecucion compromisos", "reporte consolidado"
    ]),
]