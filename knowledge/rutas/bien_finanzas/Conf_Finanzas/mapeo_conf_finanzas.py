ROUTES = [

("configuracion finanzas", "knowledge.bien_finanzas.Conf_Finanzas.conf_finanzas", "que_secciones_tiene_configuracion", [
"formato codigos", "que opciones tiene registro comunes en finanza"
]),
("formato codigos", "knowledge.bien_finanzas.Conf_Finanzas.conf_finanzas", "formato_codigos", [
"configuracion finanzas", "formatos codigos ingresar"
]),
("formatos codigos ingresar", "knowledge.bien_finanzas.Conf_Finanzas.conf_finanzas", "que_formatos_codigos_se_deben_ingresar", [
"formato codigos", "generacion automatica codigos"
]),
("generacion automatica codigos", "knowledge.bien_finanzas.Conf_Finanzas.conf_finanzas", "generacion_automatica_codigos", [
"formatos codigos ingresar", "ejemplo generacion codigo"
]),
("ejemplo generacion codigo", "knowledge.bien_finanzas.Conf_Finanzas.conf_finanzas", "ejemplo_generacion_codigo", [
"generacion automatica codigos", "guardar formatos codigos"
]),
("guardar formatos codigos", "knowledge.bien_finanzas.Conf_Finanzas.conf_finanzas", "guardar_formatos_codigos", [
"ejemplo generacion codigo", "que opciones tiene registro comunes en finanza"
]),
("que opciones tiene registro comunes en finanza", "knowledge.bien_finanzas.Conf_Finanzas.conf_finanzas", "que_opciones_tiene_registros_comunes", [
"configuracion finanzas", "bancos", "agencias bancarias", "tipos de cuenta", "cuentas bancarias", "formas de pago", "bancos tabla columnas"
]),
("bancos tabla columnas", "knowledge.bien_finanzas.Conf_Finanzas.conf_finanzas", "formulario_bancos_tabla_columnas", [
"que opciones tiene registro comunes en finanza",  "bancos botones", "bancos modificar", "bancos eliminar"
]),
("bancos", "knowledge.bien_finanzas.Conf_Finanzas.conf_finanzas", "bancos", [
"que opciones tiene registro comunes en finanza",  "bancos botones", "bancos modificar", "bancos eliminar", "bancos tabla columnas"
]),
("bancos botones", "knowledge.bien_finanzas.Conf_Finanzas.conf_finanzas", "formulario_botones_bancos", [
 "bancos guardar exito"
]),
("bancos campo obligatorio", "knowledge.bien_finanzas.Conf_Finanzas.conf_finanzas", "registro_formulario_manual_campos_bancos", [
 "bancos guardar exito"
]),
("bancos guardar exito", "knowledge.bien_finanzas.Conf_Finanzas.conf_finanzas", "formulario_bancos_guardar_exito", [
"bancos botones", "bancos modificar", "bancos eliminar"
]),
("bancos modificar", "knowledge.bien_finanzas.Conf_Finanzas.conf_finanzas", "formulario_bancos_modificar_registro", [
"bancos", "bancos eliminar", "bancos tabla columnas"
]),
("bancos eliminar", "knowledge.bien_finanzas.Conf_Finanzas.conf_finanzas", "formulario_bancos_eliminar_registro", [
"bancos", "bancos modificar", "bancos tabla columnas"
]),
("agencias bancarias", "knowledge.bien_finanzas.Conf_Finanzas.conf_finanzas", "formulario_agencias_bancarias_campos", [
"que opciones tiene registro comunes en finanza", "agencias numeros telefonicos", "agencias botones", "agencias modificar", "agencias eliminar"
]),
("agencias numeros telefonicos", "knowledge.bien_finanzas.Conf_Finanzas.conf_finanzas", "formulario_agencias_bancarias_numeros_telefonicos", [
"agencias bancarias", "agencias botones"
]),
("agencias botones", "knowledge.bien_finanzas.Conf_Finanzas.conf_finanzas", "formulario_agencias_bancarias_botones", [
"agencias bancarias", "agencias guardar exito"
]),
("agencias campo obligatorio", "knowledge.bien_finanzas.Conf_Finanzas.conf_finanzas", "formulario_agencias_campo_obligatorio_omitido", [
"agencias bancarias", "agencias guardar exito"
]),
("agencias guardar exito", "knowledge.bien_finanzas.Conf_Finanzas.conf_finanzas", "formulario_agencias_guardar_exito", [
"agencias botones", "agencias tabla columnas"
]),
("agencias tabla columnas", "knowledge.bien_finanzas.Conf_Finanzas.conf_finanzas", "formulario_agencias_tabla_columnas", [
"agencias guardar exito", "agencias modificar", "agencias eliminar"
]),
("agencias modificar", "knowledge.bien_finanzas.Conf_Finanzas.conf_finanzas", "formulario_agencias_modificar_registro", [
"agencias tabla columnas", "agencias eliminar"
]),
("agencias eliminar", "knowledge.bien_finanzas.Conf_Finanzas.conf_finanzas", "formulario_agencias_eliminar_registro", [
"agencias tabla columnas", "agencias modificar"
]),
("tipos de cuenta", "knowledge.bien_finanzas.Conf_Finanzas.conf_finanzas", "formulario_tipos_cuenta_campos", [
"que opciones tiene registro comunes en finanza", "tipos cuenta botones", "tipos cuenta modificar", "tipos cuenta eliminar"
]),
("tipos cuenta botones", "knowledge.bien_finanzas.Conf_Finanzas.conf_finanzas", "formulario_tipos_cuenta_botones", [
"tipos de cuenta", "tipos cuenta guardar exito"
]),
("tipos cuenta campo obligatorio", "knowledge.bien_finanzas.Conf_Finanzas.conf_finanzas", "formulario_tipos_cuenta_campo_obligatorio_omitido", [
"tipos de cuenta", "tipos cuenta guardar exito"
]),
("tipos cuenta guardar exito", "knowledge.bien_finanzas.Conf_Finanzas.conf_finanzas", "formulario_tipos_cuenta_guardar_exito", [
"tipos cuenta botones", "tipos cuenta tabla columnas"
]),
("tipos cuenta tabla columnas", "knowledge.bien_finanzas.Conf_Finanzas.conf_finanzas", "formulario_tipos_cuenta_tabla_columnas", [
"tipos cuenta guardar exito", "tipos cuenta modificar", "tipos cuenta eliminar"
]),
("tipos cuenta modificar", "knowledge.bien_finanzas.Conf_Finanzas.conf_finanzas", "formulario_tipos_cuenta_modificar_registro", [
"tipos cuenta tabla columnas", "tipos cuenta eliminar"
]),
("tipos cuenta eliminar", "knowledge.bien_finanzas.Conf_Finanzas.conf_finanzas", "formulario_tipos_cuenta_eliminar_registro", [
"tipos cuenta tabla columnas", "tipos cuenta modificar"
]),
("cuentas bancarias", "knowledge.bien_finanzas.Conf_Finanzas.conf_finanzas", "formulario_cuentas_bancarias_campos", [
"que opciones tiene registro comunes en finanza", "cuentas bancarias botones", "cuentas bancarias modificar", "cuentas bancarias eliminar"
]),
("cuentas bancarias botones", "knowledge.bien_finanzas.Conf_Finanzas.conf_finanzas", "formulario_cuentas_bancarias_botones", [
"cuentas bancarias", "cuentas bancarias guardar exito"
]),
("cuentas bancarias campo obligatorio", "knowledge.bien_finanzas.Conf_Finanzas.conf_finanzas", "formulario_cuentas_bancarias_campo_obligatorio_omitido", [
"cuentas bancarias", "cuentas bancarias guardar exito"
]),
("cuentas bancarias guardar exito", "knowledge.bien_finanzas.Conf_Finanzas.conf_finanzas", "formulario_cuentas_bancarias_guardar_exito", [
"cuentas bancarias botones", "cuentas bancarias tabla columnas"
]),
("cuentas bancarias tabla columnas", "knowledge.bien_finanzas.Conf_Finanzas.conf_finanzas", "formulario_cuentas_bancarias_tabla_columnas", [
"cuentas bancarias guardar exito", "cuentas bancarias modificar", "cuentas bancarias eliminar"
]),
("cuentas bancarias modificar", "knowledge.bien_finanzas.Conf_Finanzas.conf_finanzas", "formulario_cuentas_bancarias_modificar_registro", [
"cuentas bancarias tabla columnas", "cuentas bancarias eliminar"
]),
("cuentas bancarias eliminar", "knowledge.bien_finanzas.Conf_Finanzas.conf_finanzas", "formulario_cuentas_bancarias_eliminar_registro", [
"cuentas bancarias tabla columnas", "cuentas bancarias modificar"
]),
("formas de pago", "knowledge.bien_finanzas.Conf_Finanzas.conf_finanzas", "formulario_formas_pago_campos", [
"que opciones tiene registro comunes en finanza", "formas pago botones", "formas pago modificar", "formas pago eliminar"
]),
("formas pago botones", "knowledge.bien_finanzas.Conf_Finanzas.conf_finanzas", "formulario_formas_pago_botones", [
"formas de pago", "formas pago guardar exito"
]),
("formas pago campo obligatorio", "knowledge.bien_finanzas.Conf_Finanzas.conf_finanzas", "formulario_formas_pago_campo_obligatorio_omitido", [
"formas de pago", "formas pago guardar exito"
]),
("formas pago guardar exito", "knowledge.bien_finanzas.Conf_Finanzas.conf_finanzas", "formulario_formas_pago_guardar_exito", [
"formas pago botones", "formas pago tabla columnas"
]),
("formas pago tabla columnas", "knowledge.bien_finanzas.Conf_Finanzas.conf_finanzas", "formulario_formas_pago_tabla_columnas", [
"formas pago guardar exito", "formas pago modificar", "formas pago eliminar"
]),
("formas pago modificar", "knowledge.bien_finanzas.Conf_Finanzas.conf_finanzas", "formulario_formas_pago_modificar_registro", [
"formas pago tabla columnas", "formas pago eliminar"
]),
("formas pago eliminar", "knowledge.bien_finanzas.Conf_Finanzas.conf_finanzas", "formulario_formas_pago_eliminar_registro", [
"formas pago tabla columnas", "formas pago modificar"
])
]