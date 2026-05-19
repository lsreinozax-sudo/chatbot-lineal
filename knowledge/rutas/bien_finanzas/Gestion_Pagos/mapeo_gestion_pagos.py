ROUTES = [

    ("gestion de pagos", "knowledge.bien_finanzas.Gestion_Pagos.gestion_pagos", "submenu_gestion_pagos", [
        "ordenes de pago", "emision de pago"
    ]),
    ("ordenes de pago", "knowledge.bien_finanzas.Gestion_Pagos.gestion_pagos", "ordenes_filtros_busqueda", [
        "gestion de pagos", "ordenes tabla columnas", "crear orden pago"
    ]),
    ("ordenes tabla columnas", "knowledge.bien_finanzas.Gestion_Pagos.gestion_pagos", "ordenes_tabla_columnas", [
        "ordenes de pago", "crear orden pago", "orden ver registro", "orden aprobar", "orden modificar", "orden anular"
    ]),
    ("crear orden pago", "knowledge.bien_finanzas.Gestion_Pagos.gestion_pagos", "crear_orden_pago_secciones", [
        "ordenes de pago", "orden datos orden", "orden datos proveedor", "orden retenciones", "orden datos contables"
    ]),
    ("orden datos orden", "knowledge.bien_finanzas.Gestion_Pagos.gestion_pagos", "orden_seccion_datos_orden_campos", [
        "crear orden pago", "orden datos proveedor"
    ]),
    ("orden datos proveedor", "knowledge.bien_finanzas.Gestion_Pagos.gestion_pagos", "orden_seccion_datos_proveedor_campos", [
        "orden datos orden", "orden retenciones"
    ]),
    ("orden retenciones", "knowledge.bien_finanzas.Gestion_Pagos.gestion_pagos", "orden_retenciones_campos_adicionales", [
        "orden datos proveedor", "orden datos contables"
    ]),
    ("orden datos contables", "knowledge.bien_finanzas.Gestion_Pagos.gestion_pagos", "orden_seccion_datos_contables", [
        "orden retenciones", "orden botones"
    ]),
    ("orden botones", "knowledge.bien_finanzas.Gestion_Pagos.gestion_pagos", "orden_botones_formulario", [
        "orden datos contables", "orden guardar comprobante"
    ]),
    ("orden guardar comprobante", "knowledge.bien_finanzas.Gestion_Pagos.gestion_pagos", "orden_guardar_mensaje_comprobante", [
        "orden botones", "orden guardar exito"
    ]),
    ("orden guardar exito", "knowledge.bien_finanzas.Gestion_Pagos.gestion_pagos", "orden_guardar_exito", [
        "orden guardar comprobante", "orden ver registro"
    ]),
    ("orden ver registro", "knowledge.bien_finanzas.Gestion_Pagos.gestion_pagos", "orden_ver_registro_detalle", [
        "ordenes tabla columnas", "orden aprobar"
    ]),
    ("orden aprobar", "knowledge.bien_finanzas.Gestion_Pagos.gestion_pagos", "orden_aprobar_registro", [
        "orden ver registro", "orden modificar"
    ]),
    ("orden modificar", "knowledge.bien_finanzas.Gestion_Pagos.gestion_pagos", "orden_modificar_registro", [
        "orden aprobar", "orden anular"
    ]),
    ("orden anular", "knowledge.bien_finanzas.Gestion_Pagos.gestion_pagos", "orden_anular_registro_campos", [
        "orden modificar", "orden anular sin remision", "orden anular con remision"
    ]),
    ("orden anular sin remision", "knowledge.bien_finanzas.Gestion_Pagos.gestion_pagos", "orden_anular_sin_remision_mensaje", [
        "orden anular", "orden anular guardar"
    ]),
    ("orden anular con remision", "knowledge.bien_finanzas.Gestion_Pagos.gestion_pagos", "orden_anular_con_remision_mensaje", [
        "orden anular", "orden anular guardar"
    ]),
    ("orden anular guardar", "knowledge.bien_finanzas.Gestion_Pagos.gestion_pagos", "orden_anular_guardar", [
        "orden anular sin remision", "orden anular con remision"
    ]),
    ("emision de pago", "knowledge.bien_finanzas.Gestion_Pagos.gestion_pagos", "emision_pago_filtros_busqueda", [
        "gestion de pagos", "emision tabla columnas", "crear emision pago"
    ]),
    ("emision tabla columnas", "knowledge.bien_finanzas.Gestion_Pagos.gestion_pagos", "emision_pago_tabla_columnas", [
        "emision de pago", "crear emision pago", "emision aprobar", "emision ver registro", "emision imprimir", "emision modificar"
    ]),
    ("crear emision pago", "knowledge.bien_finanzas.Gestion_Pagos.gestion_pagos", "crear_emision_pago_campos", [
        "emision de pago", "emision campos automaticos", "emision agregar retencion"
    ]),
    ("emision campos automaticos", "knowledge.bien_finanzas.Gestion_Pagos.gestion_pagos", "emision_campos_automaticos", [
        "crear emision pago", "emision agregar retencion"
    ]),
    ("emision agregar retencion", "knowledge.bien_finanzas.Gestion_Pagos.gestion_pagos", "emision_agregar_retencion", [
        "emision campos automaticos", "emision tabla retenciones"
    ]),
    ("emision tabla retenciones", "knowledge.bien_finanzas.Gestion_Pagos.gestion_pagos", "emision_tabla_retenciones_columnas", [
        "emision agregar retencion", "emision datos bancarios"
    ]),
    ("emision datos bancarios", "knowledge.bien_finanzas.Gestion_Pagos.gestion_pagos", "emision_datos_bancarios_campos", [
        "emision tabla retenciones", "emision datos contables"
    ]),
    ("emision datos contables", "knowledge.bien_finanzas.Gestion_Pagos.gestion_pagos", "emision_datos_contables", [
        "emision datos bancarios", "emision botones"
    ]),
    ("emision botones", "knowledge.bien_finanzas.Gestion_Pagos.gestion_pagos", "emision_botones_formulario", [
        "emision datos contables", "emision guardar exito"
    ]),
    ("emision guardar exito", "knowledge.bien_finanzas.Gestion_Pagos.gestion_pagos", "emision_guardar_exito", [
        "emision botones", "emision aprobar"
    ]),
    ("emision aprobar", "knowledge.bien_finanzas.Gestion_Pagos.gestion_pagos", "emision_aprobar_registro_campos", [
        "emision guardar exito", "emision aprobar confirmacion"
    ]),
    ("emision aprobar confirmacion", "knowledge.bien_finanzas.Gestion_Pagos.gestion_pagos", "emision_aprobar_confirmacion", [
        "emision aprobar", "emision ver registro"
    ]),
    ("emision ver registro", "knowledge.bien_finanzas.Gestion_Pagos.gestion_pagos", "emision_ver_registro_detalle", [
        "emision aprobar confirmacion", "emision imprimir", "emision modificar"
    ]),
    ("emision imprimir", "knowledge.bien_finanzas.Gestion_Pagos.gestion_pagos", "emision_imprimir_registro", [
        "emision ver registro", "emision modificar"
    ]),
    ("emision modificar", "knowledge.bien_finanzas.Gestion_Pagos.gestion_pagos", "emision_modificar_registro", [
        "emision ver registro", "emision anular"
    ]),
    ("emision anular", "knowledge.bien_finanzas.Gestion_Pagos.gestion_pagos", "emision_anular_registro_campos", [
        "emision modificar", "emision anular sin remision", "emision anular con remision"
    ]),
    ("emision anular sin remision", "knowledge.bien_finanzas.Gestion_Pagos.gestion_pagos", "emision_anular_sin_remision_mensaje", [
        "emision anular", "emision anular campos adicionales"
    ]),
    ("emision anular con remision", "knowledge.bien_finanzas.Gestion_Pagos.gestion_pagos", "emision_anular_con_remision_mensaje", [
        "emision anular", "emision anular campos adicionales"
    ]),
    ("emision anular campos adicionales", "knowledge.bien_finanzas.Gestion_Pagos.gestion_pagos", "emision_anular_campos_adicionales", [
        "emision anular sin remision", "emision anular con remision"
    ]),
    ("emision generar comprobante retencion", "knowledge.bien_finanzas.Gestion_Pagos.gestion_pagos", "emision_generar_comprobante_retencion", [
        "emision tabla columnas", "emision reporte retencion estructura"
    ]),
    ("emision reporte retencion estructura", "knowledge.bien_finanzas.Gestion_Pagos.gestion_pagos", "emision_reporte_retencion_estructura", [
        "emision generar comprobante retencion"
    ]),
]