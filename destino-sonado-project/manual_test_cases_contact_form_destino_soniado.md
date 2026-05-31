# 🧪 Casos de Prueba y Reporte de Defectos (Bugs)

Este documento contiene la especificación formal de los **20 casos de prueba** diseñados para el Formulario de Contacto de la plataforma "Destino Soñado", junto con el reporte detallado de los defectos identificados durante la ejecución.

---

## 📊 Matriz de Diseño y Ejecución de Casos de Prueba

| ID | Título del Caso de Prueba | Precondiciones | Pasos de Ejecución | Resultado Esperado | Estado (Status) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **CP-001** | Envío exitoso con datos válidos | Usuario en sección Contacto. | Completar todos los campos con datos válidos. Cargar imagen formato .jpg. Hacer clic en "Enviar". | Formulario enviado con éxito. Mensaje de confirmación visible. | **PASSED** |
| **CP-002** | Campo Nombre vacío | Usuario en sección Contacto. | Dejar "Nombre" vacío. Completar el resto. Hacer clic en "Enviar". | El sistema bloquea el envío y solicita completar el campo obligatorio. | **FAILED** |
| **CP-003** | Campo Nombre con espacios en blanco | Usuario en sección Contacto. | Ingresar solo espacios en blanco en "Nombre". Completar el resto. Enviar. | El sistema reconoce la ausencia de texto real y solicita corregir el campo. | **FAILED** |
| **CP-004** | Campo Email vacío | Usuario en sección Contacto. | Dejar "Email" vacío. Completar el resto. Hacer clic en "Enviar". | Bloqueo del envío y alerta de campo obligatorio. | **FAILED** |
| **CP-005** | Correo sin símbolo arroba (@) | Usuario en sección Contacto. | Ingresar "usuario-gmail.com" en Email. Completar el resto. Enviar. | Alerta visual indicando formato de correo electrónico inválido. | **PASSED** |
| **CP-006** | Correo sin dominio válido | Usuario en sección Contacto. | Ingresar "usuario@com" en Email. Completar el resto. Enviar. | Alerta indicando que el correo electrónico no es válido. | **PASSED** |
| **CP-007** | Campo Teléfono vacío | Usuario en sección Contacto. | Dejar "Teléfono" vacío. Completar el resto. Enviar. | Bloqueo del envío y solicitud de campo obligatorio. | **FAILED** |
| **CP-008** | Teléfono con caracteres alfabéticos | Usuario en sección Contacto. | Ingresar letras ("abcdef") en Teléfono. Completar el resto. Enviar. | El sistema rechaza la entrada o alerta que solo se admiten números. | **FAILED** |
| **CP-009** | Selección de Destino por defecto | Usuario en sección Contacto. | No modificar el selector "Destino de preferencia". Completar el resto. Enviar. | El formulario se envía registrando la opción por defecto correctamente. | **PASSED** |
| **CP-010** | Campo Mensaje vacío | Usuario en sección Contacto. | Dejar el cuadro de "Mensaje" vacío. Completar el resto. Enviar. | Bloqueo del envío por falta de contenido obligatorio. | **FAILED** |
| **CP-011** | Fecha de Salida vacía | Usuario en sección Contacto. | No seleccionar "Fecha de Salida". Completar el resto. Enviar. | Alerta de campo obligatorio, impidiendo el envío. | **FAILED** |
| **CP-012** | Fecha de Regreso vacía | Usuario en sección Contacto. | No seleccionar "Fecha de Regreso". Completar el resto. Enviar. | Alerta de campo obligatorio, impidiendo el envío. | **FAILED** |
| **CP-013** | Fecha de Salida en el pasado | Usuario en sección Contacto. | Seleccionar una fecha anterior al día de hoy en Salida. Completar el resto. Enviar. | El sistema rechaza la fecha por inconsistencia temporal comercial. | **FAILED** |
| **CP-014** | Fecha de Regreso anterior a Salida | Usuario en sección Contacto. | Salida: 15/06/2026. Regreso: 10/06/2026. Completar el resto. Enviar. | El sistema bloquea el envío por inconsistencia lógica de fechas. | **FAILED** |
| **CP-015** | Adjuntar archivo permitido (.png) | Usuario en sección Contacto. | Adjuntar archivo "dni.png". Completar el resto. Enviar. | Envío exitoso. Archivo procesado correctamente. | **PASSED** |
| **CP-016** | Adjuntar archivo no permitido (.pdf) | Usuario en sección Contacto. | Adjuntar archivo "documento.pdf". Completar el resto. Enviar. | El sistema rechaza el archivo mostrando los formatos permitidos. | **FAILED** |
| **CP-017** | Adjuntar archivo que supera peso máximo | Usuario en sección Contacto. | Adjuntar imagen de 25MB. Completar el resto. Enviar. | Alerta de límite de tamaño excedido (Max 5MB). | **PASSED** |
| **CP-018** | Consentimiento de términos desmarcado | Usuario en sección Contacto. | Desmarcar casilla de "Acepto términos y condiciones". Enviar. | Bloqueo del envío hasta que la casilla sea aceptada. | **PASSED** |
| **CP-019** | Comportamiento del botón Reset | Usuario en sección Contacto. | Completar todos los campos del formulario. Hacer clic en "Limpiar". | Todos los campos vuelven a su estado vacío o inicial. | **PASSED** |
| **CP-020** | Envío múltiple (Spam Control) | Usuario en sección Contacto. | Hacer clic en "Enviar" reiteradas veces de forma consecutiva. | El sistema procesa un solo envío o bloquea temporalmente por spam. | **PASSED** |

---

## 🐛 Reporte de Defectos (Bug Log)

A continuación se detallan los 11 fallos detectados durante la ejecución de las pruebas, ordenados por nivel de severidad para el negocio.

| ID Bug | Caso Asociado | Defecto Encontrado / Comportamiento Observado | Severidad | Prioridad |
| :--- | :--- | :--- | :--- | :--- |
| **BUG-001** | CP-003 | **Bypass de validación mediante espacios en blanco:** Permite enviar el formulario si el campo "Nombre" solo contiene espacios. | **Alta** | Alta |
| **BUG-002** | CP-013 | **Inconsistencia de fecha pasada:** El selector permite agendar viajes con fechas de salida anteriores al día de la fecha. | **Alta** | Alta |
| **BUG-003** | CP-014 | **Inconsistencia cronológica:** Permite establecer una fecha de regreso que es anterior a la fecha de partida elegida. | **Alta** | Alta |
| **BUG-004** | CP-016 | **Falta de filtro en tipo de adjunto:** El sistema acepta archivos `.pdf` y ejecutables en un campo destinado solo a imágenes. | **Alta** | Media |
| **BUG-005** | CP-002 | **Ausencia de alerta en Nombre vacío:** El formulario se envía directamente a Formspree ignorando la falta de datos. | **Media** | Alta |
| **BUG-006** | CP-004 | **Ausencia de alerta en Email vacío:** No existe validación de campo requerido para el correo del cliente. | **Media** | Alta |
| **BUG-007** | CP-007 | **Ausencia de alerta en Teléfono vacío:** Permite el envío sin datos numéricos de contacto directo. | **Media** | Media |
| **BUG-008** | CP-008 | **Falta de sanitización en Teléfono:** El campo de teléfono acepta letras y caracteres especiales sin restricción. | **Media** | Media |
| **BUG-009** | CP-010 | **Ausencia de alerta en Mensaje vacío:** Se procesan consultas comerciales sin cuerpo de texto o pregunta. | **Media** | Baja |
| **BUG-010** | CP-011 | **Fechas obligatorias ausentes:** Permite el envío del formulario sin haber seleccionado ninguna fecha de salida. | **Media** | Alta |
| **BUG-011** | CP-012 | **Fechas obligatorias ausentes:** Permite el envío del formulario sin haber seleccionado ninguna fecha de regreso. | **Media** | Alta |
