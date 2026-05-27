ROUTES = [
    # (keyword, modulo, funcion, sugerencias)
    
    # === CONFIGURACIÓN ===
    ("introduccion presupuesto", "knowledge.presupuesto.Conf_Presupuesto.introduccion_y_formatos", "introduccion_modulo_presupuesto", [
        "formatos de codigos", "fuentes de financiamiento", "proyectos"
    ]),
    ("formatos de codigos", "knowledge.presupuesto.Conf_Presupuesto.introduccion_y_formatos", "formatos_de_codigos", [
        "introduccion presupuesto", "fuentes de financiamiento", "categoria de cuentas"
    ]),
    ("fuentes de financiamiento", "knowledge.presupuesto.Conf_Presupuesto.registros_comunes", "fuentes_de_financiamiento", [
        "tipos de financiamiento", "categoria de cuentas", "formatos de codigos"
    ]),
    ("tipos de financiamiento", "knowledge.presupuesto.Conf_Presupuesto.registros_comunes", "tipos_de_financiamiento", [
        "fuentes de financiamiento", "categoria de cuentas"
    ]),
    ("categoria de cuentas", "knowledge.presupuesto.Conf_Presupuesto.registros_comunes", "categoria_de_cuentas", [
        "fuentes de financiamiento", "tipos de financiamiento", "proyectos"
    ]),
    ("proyectos", "knowledge.presupuesto.Conf_Presupuesto.proyectos_y_acciones", "proyectos", [
        "acciones centralizadas", "acciones especificas", "formulacion de presupuesto"
    ]),
    ("acciones centralizadas", "knowledge.presupuesto.Conf_Presupuesto.proyectos_y_acciones", "acciones_centralizadas", [
        "proyectos", "acciones especificas"
    ]),
    ("acciones especificas", "knowledge.presupuesto.Conf_Presupuesto.proyectos_y_acciones", "acciones_especificas", [
        "proyectos", "acciones centralizadas", "formulacion de presupuesto"
    ]),
]