ROUTES = [

("archivo txt nomina", "knowledge.ari_txt_hoja_tiempo_th.Archivo_Txt.archivo_txt", "archivo_txt_introduccion", [
"requisitos archivo txt", "acceso archivo txt"
]),
("requisitos archivo txt", "knowledge.ari_txt_hoja_tiempo_th.Archivo_Txt.archivo_txt", "archivo_txt_requisitos", [
"archivo txt nomina", "generar archivo txt"
]),
("acceso archivo txt", "knowledge.ari_txt_hoja_tiempo_th.Archivo_Txt.archivo_txt", "archivo_txt_acceso", [
"archivo txt nomina", "generar archivo txt"
]),
("generar archivo txt", "knowledge.ari_txt_hoja_tiempo_th.Archivo_Txt.archivo_txt", "archivo_txt_generar_formulario_campos", [
"acceso archivo txt", "campo obligatorio txt", "generar exito txt"
]),
("campo obligatorio txt", "knowledge.ari_txt_hoja_tiempo_th.Archivo_Txt.archivo_txt", "archivo_txt_campo_obligatorio", [
"generar archivo txt", "generar exito txt"
]),
("generar exito txt", "knowledge.ari_txt_hoja_tiempo_th.Archivo_Txt.archivo_txt", "archivo_txt_generar_exito", [
"generar archivo txt", "campo obligatorio txt"
]),
]