# 🔍 Análisis Exploratorio y Matriz de Riesgos

## 1️⃣ Información General del Sitio Bajo Prueba (SUT)
*   **Nombre del sitio:** Destino soñado[cite: 1, 2]
*   **URL:** [cac-tpfinal-turismo-completo.netlify.app](https://cac-tpfinal-turismo-completo.netlify.app/)[cite: 1, 7]
*   **Tipo de aplicación:** Multi-página tradicional[cite: 1, 2].
*   **Objetivo del sitio:** Plataforma informativa y comercial para una empresa de turismo[cite: 1, 2].
*   **Navegador utilizado:** Google Chrome[cite: 1, 2, 7].

---

## 2️⃣ Mapa Funcional del Sistema
A través del reconocimiento del sitio, se relevaron las siguientes secciones y comportamientos[cite: 1, 6]:

*   **Home:** Página informativa estática con acceso a la navegación principal y espíritu de la empresa[cite: 1, 2].
*   **Galería:** Catálogo interactivo con tarjetas de destinos turísticos[cite: 1, 2].
*   **Sucursales:** Ubicación geográfica de puntos físicos mediante mapas, datos de contacto y material audiovisual[cite: 1, 2].
*   **Experiencias:** Paquetes turísticos organizados por categorías (culturales, gastronómicas, etc.) mediante tarjetas[cite: 1, 2].
*   **Contacto:** Formulario de registro, consultas y carga de archivos[cite: 1, 7].
*   **Links útiles:** Blog externo de viajeros. Es la única sección interna que fuerza la apertura en una pestaña nueva[cite: 1, 2].
*   **Clientes:** Módulo CRUD (Create, Read, Update, Delete) para la gestión de usuarios[cite: 1, 2].

### Componentes Globales (Persistentes)
*   **Navbar:** Menú de navegación superior adaptativo con efectos *hover* al posar el cursor[cite: 1, 2].
*   **Footer:** Sección inferior que incluye derechos de autor, enlaces a redes sociales y botón dinámico de "Volver arriba"[cite: 1, 2, 6].
*   **Logo de Empresa:** Identificador visual presente en todo el sitio (actualmente sin comportamiento de redirección al Home)[cite: 1, 2, 6].

---

## 3️⃣ Análisis Técnico Superficial e Integraciones
*   **Comportamiento de Rutas:** La aplicación realiza recargas completas de página al navegar y modifica las URLs de forma síncrona, permitiendo el acceso manual a las rutas[cite: 1, 2].
*   **Integración de Terceros:** El formulario de contacto delega el procesamiento de datos al servicio externo **Formspree**[cite: 1, 2, 7]. El sistema maneja mensajes básicos de éxito o fallo provistos por la API de dicha integración[cite: 2].

---

## 4️⃣ Matriz de Escenarios Críticos y Riesgos Identificados

| Escenario Crítico | Descripción del Riesgo | Impacto | Probabilidad |
| :--- | :--- | :--- | :--- |
| **Falla en Servicio Formspree** | Caída o interrupción de la API externa durante el envío de consultas[cite: 1, 2]. | **Alto:** Pérdida de leads y consultas de clientes sin aviso claro de error[cite: 1, 2]. | Media |
| **CRUD de Clientes Inseguro** | El módulo de clientes permite la eliminación de registros de forma directa sin solicitar una ventana modal de confirmación[cite: 2]. | **Alto:** Pérdida accidental o irreversible de datos críticos de la base de datos[cite: 2]. | Alta |
| **Responsive Defectuoso** | Desaparición de la barra de menú e inconsistencia en visualización de tarjetas en dispositivos móviles[cite: 1, 2]. | **Medio:** Frustración del usuario y abandono temprano del flujo de navegación[cite: 1, 2]. | Alta |
| **Enlaces Rotos/Genéricos** | Enlaces a redes sociales en el pie de página apuntan a rutas genéricas en lugar de los perfiles de la empresa[cite: 2, 6]. | **Bajo:** Pérdida de engagement y canales alternativos de contacto[cite: 2]. | Alta[cite: 1] |
| **Validación Débil en Formulario** | Ausencia de reglas de negocio del lado del cliente (client-side validation) para el filtrado de entradas inválidas[cite: 1, 2]. | **Medio:** Corrupción y baja calidad de los datos recolectados en el backend[cite: 1, 2]. | Alta |
