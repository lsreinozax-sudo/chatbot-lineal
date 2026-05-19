ROUTES = [

    ("movimientos bancarios", "knowledge.bien_finanzas.Finanzas_Banco.finanzas_banco", "movimientos_bancarios_filtros_busqueda", [
        "bancos submenu", "movimientos tabla columnas", "crear movimiento bancario"
    ]),
    ("movimientos tabla columnas", "knowledge.bien_finanzas.Finanzas_Banco.finanzas_banco", "movimientos_bancarios_tabla_columnas", [
        "movimientos bancarios", "crear movimiento bancario", "movimiento ver registro", "movimiento aprobar", "movimiento modificar finanza", "movimiento eliminar"
    ]),
    ("crear movimiento bancario", "knowledge.bien_finanzas.Finanzas_Banco.finanzas_banco", "crear_movimiento_bancario_campos", [
        "movimientos bancarios", "movimiento datos contables"
    ]),
    ("movimiento datos contables", "knowledge.bien_finanzas.Finanzas_Banco.finanzas_banco", "movimiento_datos_contables_seccion", [
        "crear movimiento bancario", "movimiento botones"
    ]),
    ("movimiento botones", "knowledge.bien_finanzas.Finanzas_Banco.finanzas_banco", "movimiento_botones_formulario", [
        "movimiento datos contables", "movimiento guardar exito"
    ]),
    ("movimiento guardar exito", "knowledge.bien_finanzas.Finanzas_Banco.finanzas_banco", "movimiento_guardar_exito", [
        "movimiento botones", "movimiento aprobar"
    ]),
    ("movimiento aprobar", "knowledge.bien_finanzas.Finanzas_Banco.finanzas_banco", "movimiento_aprobar_registro", [
        "movimiento guardar exito", "movimiento ver registro"
    ]),
    ("movimiento ver registro", "knowledge.bien_finanzas.Finanzas_Banco.finanzas_banco", "movimiento_ver_registro_detalle", [
        "movimiento aprobar", "movimiento modificar finanza"
    ]),
    ("movimiento modificar finanza", "knowledge.bien_finanzas.Finanzas_Banco.finanzas_banco", "movimiento_modificar_registro", [
        "movimiento ver registro", "movimiento eliminar"
    ]),
    ("movimiento eliminar finanza", "knowledge.bien_finanzas.Finanzas_Banco.finanzas_banco", "movimiento_eliminar_registro", [
        "movimiento modificar finanza"
    ]),
    ("conciliacion bancaria", "knowledge.bien_finanzas.Finanzas_Banco.finanzas_banco", "conciliacion_bancaria_tabla_columnas", [
        "bancos submenu", "crear conciliacion bancaria", "conciliacion aprobar", "conciliacion ver registro", "conciliacion imprimir", "conciliacion modificar", "conciliacion eliminar"
    ]),
    ("crear conciliacion bancaria", "knowledge.bien_finanzas.Finanzas_Banco.finanzas_banco", "crear_conciliacion_bancaria_campos", [
        "conciliacion bancaria", "conciliacion seccion ejemplo carga"
    ]),
    ("conciliacion seccion ejemplo carga", "knowledge.bien_finanzas.Finanzas_Banco.finanzas_banco", "conciliacion_seccion_ejemplo_carga", [
        "crear conciliacion bancaria", "conciliacion exportar archivo"
    ]),
    ("conciliacion exportar archivo", "knowledge.bien_finanzas.Finanzas_Banco.finanzas_banco", "conciliacion_exportar_archivo", [
        "conciliacion seccion ejemplo carga", "conciliacion importar archivo"
    ]),
    ("conciliacion importar archivo", "knowledge.bien_finanzas.Finanzas_Banco.finanzas_banco", "conciliacion_importar_archivo", [
        "conciliacion exportar archivo", "conciliacion automatica", "conciliacion manual"
    ]),
    ("conciliacion automatica", "knowledge.bien_finanzas.Finanzas_Banco.finanzas_banco", "conciliacion_automatica", [
        "conciliacion importar archivo", "conciliacion botones"
    ]),
    ("conciliacion manual", "knowledge.bien_finanzas.Finanzas_Banco.finanzas_banco", "conciliacion_manual", [
        "conciliacion importar archivo", "conciliacion botones"
    ]),
    ("conciliacion botones", "knowledge.bien_finanzas.Finanzas_Banco.finanzas_banco", "conciliacion_botones_formulario", [
        "conciliacion automatica", "conciliacion manual", "conciliacion guardar exito"
    ]),
    ("conciliacion guardar exito", "knowledge.bien_finanzas.Finanzas_Banco.finanzas_banco", "conciliacion_guardar_exito", [
        "conciliacion botones", "conciliacion aprobar"
    ]),
    ("conciliacion aprobar", "knowledge.bien_finanzas.Finanzas_Banco.finanzas_banco", "conciliacion_aprobar_registro", [
        "conciliacion guardar exito", "conciliacion ver registro"
    ]),
    ("conciliacion ver registro", "knowledge.bien_finanzas.Finanzas_Banco.finanzas_banco", "conciliacion_ver_registro_detalle", [
        "conciliacion aprobar", "conciliacion imprimir", "conciliacion modificar"
    ]),
    ("conciliacion imprimir", "knowledge.bien_finanzas.Finanzas_Banco.finanzas_banco", "conciliacion_imprimir_registro", [
        "conciliacion ver registro"
    ]),
    ("conciliacion modificar", "knowledge.bien_finanzas.Finanzas_Banco.finanzas_banco", "conciliacion_modificar_registro", [
        "conciliacion ver registro", "conciliacion eliminar"
    ]),
    ("conciliacion eliminar", "knowledge.bien_finanzas.Finanzas_Banco.finanzas_banco", "conciliacion_eliminar_registro", [
        "conciliacion modificar"
    ]),
    ]