# 🗺️ Portfolio de QA Manual: Proyecto "Destino Soñado"

¡Bienvenido/a a mi portfolio de Testing Manual! En este repositorio presento un análisis de calidad integral de punta a punta realizado sobre la plataforma web de turismo **"Destino Soñado"**, un sitio multi-página tradicional que utiliza servicios externos para la gestión de datos.

El objetivo de este proyecto es demostrar mis habilidades en el relevamiento funcional, análisis de riesgos, diseño/ejecución de casos de prueba y reporte sistemático de defectos (bugs).

---

## 📊 Resumen Ejecutivo del Proyecto

*   **Sitio Bajo Prueba (SUT):** Destino Soñado
*   **URL del Sitio:** [cac-tpfinal-turismo-completo.netlify.app](https://cac-tpfinal-turismo-completo.netlify.app/)
*   **Tipo de Testing:** Manual, Funcional, Caja Negra, Exploratorio.
*   **Entorno de Pruebas:** Windows 11 / Google Chrome.

### 📈 Métricas de Ejecución
*   **Casos de Prueba Diseñados:** 20
*   **Casos Exitosos (Passed):** 9
*   **Casos Fallidos (Failed):** 11
*   **Defectos (Bugs) Reportados:** 11

---

## 📂 Estructura del Proyecto de Pruebas

El análisis y la documentación técnica se encuentran divididos en las siguientes secciones dentro de la carpeta `destino-sonado-project`:

1.  **[Análisis Exploratorio y de Riesgos](destino-sonado-project/analisis_exploratorio_inicial_destino_soniado.md):** Mapa funcional del sistema, comportamiento de componentes globales (Navbar, Footer, Formspree), escenarios críticos potenciales y matriz preliminar de riesgos.
2.  **[Casos de Prueba y Reporte de Defectos](destino-sonado-project/manual_test_cases_contact_form_destino_soniado.md):** Matriz detallada con los 20 escenarios probados en el formulario de contacto (pruebas de límites, campos obligatorios, tipos de datos inválidos y consistencia de fechas) junto a la tabla de bugs encontrados clasificados por severidad.

---

## 🧠 Destacados Técnicos de la Investigación

Durante el ciclo de pruebas logré identificar fallos críticos en la lógica de negocio y validación del lado del cliente (Client-Side), entre los que se destacan:
*   **Bypass de Campos Obligatorios:** El sistema permite el envío del formulario completando el campo "Nombre" únicamente con espacios en blanco (caracteres invisibles).
*   **Inconsistencia Temporal:** Falta de validación en componentes de fecha, permitiendo registrar partidas en fechas pasadas o regresos previos a la salida.
*   **Falta de Sanitización de Datos:** El campo de teléfono admite caracteres alfabéticos y se permiten archivos adjuntos de formatos no permitidos (ej. PDFs en campos destinados a imágenes de DNI).

---

## 🛠️ Habilidades Aplicadas en este Repositorio
*   Diseño de Casos de Prueba (Casos Positivos, Negativos y Extremos).
*   Reporte y Clasificación de Bugs (Severidad y Prioridad).
*   Testing Exploratorio y Mapeo Funcional.
*   Análisis de Riesgos e Impacto en la Experiencia de Usuario (UX).
