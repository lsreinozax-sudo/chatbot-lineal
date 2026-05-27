ROUTES = [
    # (keyword, modulo, funcion, sugerencias)

    # === REQUISITOS Y ACCESO GENERAL ===
    ("requisitos expediente", "knowledge.talento_humano.Expediente.expediente", "requisitos_previos_expediente", [
        "acceder a expediente", "importar registros expediente", "acciones formulario"
    ]),
    ("acceder a expediente", "knowledge.talento_humano.Expediente.expediente", "como_acceder_al_submodulo_expediente", [
        "requisitos expediente", "que son datos personales", "importar registros expediente"
    ]),
    ("importar registros expediente", "knowledge.talento_humano.Expediente.expediente", "como_importar_registros_masivos", [
        "requisitos expediente", "acciones formulario"
    ]),
    ("acciones formulario", "knowledge.talento_humano.Expediente.expediente", "acciones_generales_formulario", [
        "importar registros expediente", "campos datos personales"
    ]),

    # === DATOS PERSONALES ===
    ("que son datos personales", "knowledge.talento_humano.Expediente.expediente", "que_son_datos_personales", [
        "campos datos personales", "gestionar datos personales", "que son datos profesionales"
    ]),
    ("campos datos personales", "knowledge.talento_humano.Expediente.expediente", "campos_crear_datos_personales", [
        "que son datos personales", "gestionar datos personales", "acciones formulario"
    ]),
    ("gestionar datos personales", "knowledge.talento_humano.Expediente.expediente", "opciones_gestion_datos_personales", [
        "que son datos personales", "campos datos personales"
    ]),

    # === DATOS PROFESIONALES ===
    ("que son datos profesionales", "knowledge.talento_humano.Expediente.expediente", "que_son_datos_profesionales", [
        "campos datos profesionales", "gestionar datos profesionales", "que son datos socioeconomicos"
    ]),
    ("campos datos profesionales", "knowledge.talento_humano.Expediente.expediente", "campos_crear_datos_profesionales", [
        "que son datos profesionales", "gestionar datos profesionales", "acciones formulario"
    ]),
    ("gestionar datos profesionales", "knowledge.talento_humano.Expediente.expediente", "opciones_gestion_datos_profesionales", [
        "que son datos profesionales", "campos datos profesionales"
    ]),

    # === DATOS SOCIOECONÓMICOS ===
    ("que son datos socioeconomicos", "knowledge.talento_humano.Expediente.expediente", "que_son_datos_socioeconomicos", [
        "campos datos socioeconomicos", "gestionar datos socioeconomicos", "que son datos laborales"
    ]),
    ("campos datos socioeconomicos", "knowledge.talento_humano.Expediente.expediente", "campos_crear_datos_socioeconomicos", [
        "que son datos socioeconomicos", "gestionar datos socioeconomicos", "acciones formulario"
    ]),
    ("gestionar datos socioeconomicos", "knowledge.talento_humano.Expediente.expediente", "opciones_gestion_datos_socioeconomicos", [
        "que son datos socioeconomicos", "campos datos socioeconomicos"
    ]),

    # === DATOS LABORALES ===
    ("que son datos laborales", "knowledge.talento_humano.Expediente.expediente", "que_son_datos_laborales", [
        "campos datos laborales", "gestionar datos laborales", "que son datos financieros"
    ]),
    ("campos datos laborales", "knowledge.talento_humano.Expediente.expediente", "campos_crear_datos_laborales", [
        "que son datos laborales", "gestionar datos laborales", "acciones formulario"
    ]),
    ("gestionar datos laborales", "knowledge.talento_humano.Expediente.expediente", "opciones_gestion_datos_laborales", [
        "que son datos laborales", "campos datos laborales"
    ]),

    # === DATOS FINANCIEROS ===
    ("que son datos financieros", "knowledge.talento_humano.Expediente.expediente", "que_son_datos_financieros", [
        "campos datos financieros", "gestionar datos financieros", "que son datos contables"
    ]),
    ("campos datos financieros", "knowledge.talento_humano.Expediente.expediente", "campos_crear_datos_financieros", [
        "que son datos financieros", "gestionar datos financieros", "acciones formulario"
    ]),
    ("gestionar datos financieros", "knowledge.talento_humano.Expediente.expediente", "opciones_gestion_datos_financieros", [
        "que son datos financieros", "campos datos financieros"
    ]),

    # === DATOS CONTABLES ===
    ("que son datos contables", "knowledge.talento_humano.Expediente.expediente", "que_son_datos_contables", [
        "campos datos contables", "gestionar datos contables", "requisitos expediente"
    ]),
    ("campos datos contables", "knowledge.talento_humano.Expediente.expediente", "campos_crear_datos_contables", [
        "que son datos contables", "gestionar datos contables", "acciones formulario"
    ]),
    ("gestionar datos contables", "knowledge.talento_humano.Expediente.expediente", "opciones_gestion_datos_contables", [
        "que son datos contables", "campos datos contables"
    ]),
]