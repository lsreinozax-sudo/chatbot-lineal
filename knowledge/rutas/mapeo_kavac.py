"""Mapeo de palabras clave → funciones de conocimiento"""

ROUTES = [
    # (keyword, modulo, funcion, sugerencias)
    
    # === KAVAC ===
    ("quien desarrollo kavac", "knowledge.Kavac.kavac", "quien_lo_desarrollo", [
        "que es kavac", "objetivo kavac", "modulos"
    ]),
    ("que es kavac", "knowledge.Kavac.kavac", "que_es_kavac", [
        "quien desarrollo kavac", "objetivo kavac", "modulos", "instituciones kavac"
    ]),
    ("objetivo kavac", "knowledge.Kavac.kavac", "objetivo", [
        "que es kavac", "quien desarrollo kavac", "modulos"
    ]),
    ("instituciones kavac", "knowledge.Kavac.kavac", "que_instituciones_lo_usan", [
        "que es kavac", "modulos"
    ]),
    ("kavac", "knowledge.Kavac.kavac", "que_es_kavac", [
        "quien desarrollo kavac", "objetivo kavac", "modulos", "instituciones kavac"
    ]),
]