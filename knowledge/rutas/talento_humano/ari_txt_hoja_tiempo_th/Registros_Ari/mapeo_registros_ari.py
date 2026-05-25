ROUTES = [

("registro ari", "knowledge.talento_humano.ari_txt_hoja_tiempo_th.Registros_Ari.registros_ari", "registro_ari_pantalla_inicial", [
"crear registro ari", "importar registros ari", "exportar registros ari"
]),
("crear registro ari", "knowledge.talento_humano.ari_txt_hoja_tiempo_th.Registros_Ari.registros_ari", "registro_ari_crear_formulario_campos", [
"registro ari", "campo obligatorio ari", "botones formulario ari"
]),
("campo obligatorio ari", "knowledge.talento_humano.ari_txt_hoja_tiempo_th.Registros_Ari.registros_ari", "registro_ari_campo_obligatorio", [
"crear registro ari", "guardar registro ari"
]),
("botones formulario ari", "knowledge.talento_humano.ari_txt_hoja_tiempo_th.Registros_Ari.registros_ari", "registro_ari_botones_formulario", [
"crear registro ari", "guardar registro ari"
]),
("guardar registro ari", "knowledge.talento_humano.ari_txt_hoja_tiempo_th.Registros_Ari.registros_ari", "registro_ari_guardar_exito", [
"botones formulario ari", "ver registro ari", "modificar registro ari", "eliminar registro ari"
]),
("ver registro ari", "knowledge.talento_humano.ari_txt_hoja_tiempo_th.Registros_Ari.registros_ari", "registro_ari_ver_registro", [
"guardar registro ari"
]),
("importar registros ari", "knowledge.talento_humano.ari_txt_hoja_tiempo_th.Registros_Ari.registros_ari", "registro_ari_carga_masiva", [
"registro ari", "exportar registros ari"
]),
("exportar registros ari", "knowledge.talento_humano.ari_txt_hoja_tiempo_th.Registros_Ari.registros_ari", "registro_ari_carga_masiva", [
"registro ari", "importar registros ari"
]),
("carga masiva ari", "knowledge.talento_humano.ari_txt_hoja_tiempo_th.Registros_Ari.registros_ari", "registro_ari_carga_masiva", [
"importar registros ari", "exportar registros ari"
]),
]