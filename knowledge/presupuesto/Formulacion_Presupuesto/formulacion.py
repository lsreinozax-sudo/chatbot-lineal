def formulacion_de_presupuesto():
    return """En el submódulo Formulación de Presupuesto, el sistema muestra filtros (Código, Fecha, Asignado) y botones Borrar/Buscar. Debajo, una tabla lista las formulaciones: Fecha de generación, Código, Año, Acción Especificas, Total Formulado, Asignado y Acción.

Para crear una nueva, se presiona Crear nuevo registro. El formulario pide: Fecha de generación, Ejercicio Fiscal, Institución, Moneda, Fuente de Financiamiento y Tipo de Financiamiento. Luego presenta dos switches (Proyecto o Acción centralizada) para habilitar la Acción Especifica correspondiente.

En la sección Distribución Financiera:
• Buscador de cuentas por código y Botón Buscar / Ver todas.
• Importar: Carga masiva con formato de hoja de cálculo (columnas: Código, Total_Real, Total_Estimado, Total_anho y meses de Ene a Dic). Si se llena Total_anho, el sistema distribuye automáticamente.
• Exportar: Descarga el formato de hoja de cálculo.
• Tabla de carga manual: Permite ingresar montos mes a mes tras activar la cuenta con el icono de ver. El campo Monto se suma automáticamente.

Al guardar, el sistema pregunta si se desea agregar otro registro. Para que la formulación proceda, debe aprobarse en dos niveles: 
1. Botón Visualizar -> activar switch “Asignar presupuesto” -> Confirmar ("Ok").
2. Botón “Confirmar presupuesto” en la columna Acción -> Confirmar.
Al completarse, el estatus Asignado cambia a "Sí".

El registro cuenta con opciones de Ver (que incluye imprimir en PDF y exportar en hoja de cálculo), Modificar (solo si no está confirmado) y Eliminar."""