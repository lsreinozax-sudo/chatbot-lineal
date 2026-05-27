ROUTES = [
    # (keyword, modulo, funcion, sugerencias)
    # === MODIFICACIONES PRESUPUESTARIAS ===
    ("creditos adicionales", "knowledge.presupuesto.Modificaciones.modificaciones_presupuestarias", "creditos_adicionales_mejor_vision", [
        "reducciones", "traspasos", "ejecucion compromisos"
    ]),
    ("reducciones", "knowledge.presupuesto.Modificaciones.modificaciones_presupuestarias", "reducciones", [
        "creditos adicionales", "traspasos"
    ]),
    ("traspasos", "knowledge.presupuesto.Modificaciones.modificaciones_presupuestarias", "traspasos", [
        "creditos adicionales", "reducciones", "reporte mayor analitico"
    ]),
]