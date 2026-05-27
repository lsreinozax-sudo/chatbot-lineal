"""Expediente del ERP KAVAC del bien de talento humano"""

# ==========================================
# REQUISITOS Y ACCESO GENERAL
# ==========================================

def requisitos_previos_expediente():
    return "Para registrar expedientes, el usuario debe poseer los permisos requeridos y haber realizado registros previos en las funcionalidades de registros comunes (como países, estados, municipios y parroquias) en la configuración general del sistema."

def como_acceder_al_submodulo_expediente():
    return "Se ingresa con credenciales de administrador, se dirige al módulo de talento humano y se pulsa sobre el submódulo 'expediente'. Esto desplegará las opciones: Datos Personales, Profesionales, Socioeconómicos, Laborales, Financieros y Contables."

def como_importar_registros_masivos():
    return "Se recomienda primero exportar el archivo actual del sistema (el cual llegará al correo del usuario). Luego, se edita esa copia agregando los registros necesarios manteniendo las columnas por defecto, y finalmente se sube mediante el botón 'Importar registros'."

def acciones_generales_formulario():
    return "Los formularios cuentan con tres botones: 'Borrar datos del formulario' para limpiar, 'Cancelar y Regresar' para salir sin cambios, y 'Guardar' para almacenar la información."

# ==========================================
# 1. DATOS PERSONALES
# ==========================================

def que_son_datos_personales():
    return "Es la primera sección del expediente donde se registra la información básica, de salud, de contacto y de residencia del trabajador."

def campos_crear_datos_personales():
    return """Para crear un nuevo registro de datos personales se solicitan los siguientes campos:
- Nombres y Apellidos.
- Nacionalidad, Cédula de Identidad, Pasaporte y RIF.
- Correo Electrónico, Fecha de Nacimiento y Género.
- Nombres, apellidos y teléfono de una persona de contacto.
- Datos de salud: Discapacidad, Tipo de Sangre, Seguro Social e Historial Médico.
- Licencia de conducir (y su grado).
- Dirección de habitación (País, Estado, Municipio, Parroquia y Dirección exacta).
- Talla de uniforme (camisa, pantalón, calzado).
- Números telefónicos (móvil, teléfono, fax, código de área y extensión)."""

def opciones_gestion_datos_personales():
    return "En la tabla principal de Datos Personales, se pueden visualizar las columnas principales del trabajador y ejecutar las acciones de: Ver Registro, Modificar Registro y Eliminar Registro."

# ==========================================
# 2. DATOS PROFESIONALES
# ==========================================

def que_son_datos_profesionales():
    return "Es la sección dedicada a registrar el nivel educativo, idiomas, capacitaciones y reconocimientos del trabajador."

def campos_crear_datos_profesionales():
    return """Para crear un registro de datos profesionales se solicitan:
- Trabajador (previamente registrado en Datos Personales).
- Grado de Instrucción.
- Estudios Universitarios: Nombre de la universidad, año de graduación, tipo de estudio y profesión.
- Estudios en proceso: Si es estudiante, tipo de estudio, programa de estudio y horario de clases (permite adjuntar archivos .odt, .pdf).
- Detalles de Idiomas: Idioma y nivel.
- Capacitación y Reconocimientos: Nombre del curso/reconocimiento y sus respectivos soportes adjuntos (.png, .jpg, .pdf, .odt)."""

def opciones_gestion_datos_profesionales():
    return "Permite visualizar el grado de instrucción y profesión, así como Ver, Modificar o Eliminar el registro profesional de un trabajador."

# ==========================================
# 3. DATOS SOCIOECONÓMICOS
# ==========================================

def que_son_datos_socioeconomicos():
    return "Sección orientada a registrar el estado civil del trabajador y la información detallada de su carga familiar."

def campos_crear_datos_socioeconomicos():
    return """Al crear un registro socioeconómico se requiere:
- Trabajador (previamente registrado).
- Estado Civil.
- Carga Familiar: Parentesco, nombres, apellidos, fecha de nacimiento, edad, cédula, género, dirección y si posee discapacidad.
- Si el parentesco es Hijo(a), se solicita el nivel de escolaridad y si posee una beca (indicando el tipo de beca y centro de estudio)."""

def opciones_gestion_datos_socioeconomicos():
    return "Desde la tabla principal se puede Ver, Modificar o Eliminar el estado civil y los integrantes de la carga familiar del trabajador."

# ==========================================
# 4. DATOS LABORALES
# ==========================================

def que_son_datos_laborales():
    return "Sección donde se detalla la situación contractual, el cargo, el departamento y la experiencia laboral previa del trabajador en la institución."

def campos_crear_datos_laborales():
    return """Los campos requeridos para los datos laborales son:
- Trabajador.
- Estado de actividad (si está inactivo, solicita fecha de ingreso, egreso, tipo de inactividad y si libera el cargo).
- Correo Institucional.
- Tipo de cargo y Cargo.
- Coordinador, Tipo de Personal y Tipo de contrato.
- Organización, Departamento, Palabras definidas y Descripción de Funciones.
- Trabajos Anteriores: Organización, teléfono, sector, cargo, tipo de personal, fecha de inicio y cese.
(El sistema calcula automáticamente la antigüedad y total de años de servicio)."""

def opciones_gestion_datos_laborales():
    return "Permite Ver, Modificar o Eliminar el estatus activo, el cargo, la antigüedad y las funciones específicas asociadas al trabajador."

# ==========================================
# 5. DATOS FINANCIEROS
# ==========================================

def que_son_datos_financieros():
    return "Sección utilizada para registrar la información bancaria del trabajador requerida para los procesos de nómina."

def campos_crear_datos_financieros():
    return """Para registrar datos financieros se necesita:
- Trabajador.
- Banco (previamente configurado en finanzas).
- Tipo de Cuenta.
- Número de Cuenta."""

def opciones_gestion_datos_financieros():
    return "Desde esta vista se puede Ver, Modificar o Eliminar la información de la cuenta bancaria del empleado."

# ==========================================
# 6. DATOS CONTABLES
# ==========================================

def que_son_datos_contables():
    return "Sección donde se asocia al trabajador con las cuentas contables o patrimoniales correspondientes."

def campos_crear_datos_contables():
    return """Para crear un registro contable se solicita:
- Trabajador.
- Cuenta contable (previamente registrada en la configuración de contabilidad). Permite agregar múltiples cuentas asociadas a un mismo empleado mediante el botón (+)."""

def opciones_gestion_datos_contables():
    return "Permite Ver o Modificar la cuenta contable del trabajador. El botón de eliminar se encuentra inhabilitado por defecto en esta sección."