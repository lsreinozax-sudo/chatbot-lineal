ROUTES = [

("pendientes", "knowledge.ari_txt_hoja_tiempo_th.Pendientes.pendientes", "pendientes_descripcion", [
"submenu hoja tiempo", "pantalla inicial pendientes"
]),
("pantalla inicial pendientes", "knowledge.ari_txt_hoja_tiempo_th.Pendientes.pendientes", "pendientes_pantalla_inicial", [
"pendientes", "crear pendientes"
]),
("crear pendientes", "knowledge.ari_txt_hoja_tiempo_th.Pendientes.pendientes", "pendientes_crear_formulario_campos", [
"pantalla inicial pendientes", "tabla parametros pendientes"
]),
("tabla parametros pendientes", "knowledge.ari_txt_hoja_tiempo_th.Pendientes.pendientes", "pendientes_tabla_parametros", [
"crear pendientes", "boton observacion pendientes", "boton conceptos pendientes"
]),
("boton observacion pendientes", "knowledge.ari_txt_hoja_tiempo_th.Pendientes.pendientes", "pendientes_boton_observacion", [
"tabla parametros pendientes", "boton conceptos pendientes"
]),
("boton conceptos pendientes", "knowledge.ari_txt_hoja_tiempo_th.Pendientes.pendientes", "pendientes_boton_conceptos", [
"tabla parametros pendientes", "boton observacion pendientes"
]),
("botones formulario pendientes", "knowledge.ari_txt_hoja_tiempo_th.Pendientes.pendientes", "pendientes_botones_formulario", [
"boton conceptos pendientes", "guardar pendientes"
]),
("guardar pendientes", "knowledge.ari_txt_hoja_tiempo_th.Pendientes.pendientes", "pendientes_guardar_exito", [
"botones formulario pendientes", "ver pendientes"
]),
("ver pendientes", "knowledge.ari_txt_hoja_tiempo_th.Pendientes.pendientes", "pendientes_ver_registro", [
"guardar pendientes", "aprobar pendientes"
]),
("aprobar pendientes", "knowledge.ari_txt_hoja_tiempo_th.Pendientes.pendientes", "pendientes_aprobar_registro", [
"ver pendientes", "confirmar pendientes", "rechazar pendientes"
]),
("confirmar pendientes", "knowledge.ari_txt_hoja_tiempo_th.Pendientes.pendientes", "pendientes_confirmar_registro", [
"aprobar pendientes", "rechazar pendientes"
]),
("rechazar pendientes", "knowledge.ari_txt_hoja_tiempo_th.Pendientes.pendientes", "pendientes_rechazar_registro", [
"aprobar pendientes", "confirmar pendientes"
]),
("modificar pendientes", "knowledge.ari_txt_hoja_tiempo_th.Pendientes.pendientes", "pendientes_modificar_registro", [
"guardar pendientes", "eliminar pendientes"
]),
("eliminar pendientes", "knowledge.ari_txt_hoja_tiempo_th.Pendientes.pendientes", "pendientes_eliminar_registro", [
"modificar pendientes"
]),
("modificar registro ari", "knowledge.ari_txt_hoja_tiempo_th.Pendientes.pendientes", "registro_ari_guardar_exito", [
"guardar registro ari", "eliminar registro ari"
]),
("eliminar registro ari", "knowledge.ari_txt_hoja_tiempo_th.Pendientes.pendientes", "registro_ari_guardar_exito", [
"modificar registro ari"
]),
]