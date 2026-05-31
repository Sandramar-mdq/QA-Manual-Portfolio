# 🖼️ Casos de Prueba Funcionales - Imágenes Rotas (Broken Images)

* **Sitio Bajo Prueba (SUT):** [the-internet.herokuapp.com/broken_images](https://the-internet.herokuapp.com/broken_images)
* **Módulo:** Galería de Imágenes / Renderizado de Contenido
* **Tipo de Prueba:** Pruebas Manuales / Validación de Recursos Visuales

---

## 📊 Matriz de Diseño de Casos de Prueba

| ID | Módulo | Caso de Prueba | Precondiciones | Pasos | Resultado Esperado | Estado |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **IMG_01** | Imágenes Rotas | Validar carga exitosa de imagen válida (Avatar 3). | - Conexión a internet estable.<br>- Acceso a la ruta `/broken_images`. | 1. Ingresar a la URL del módulo.<br>2. Inspeccionar visualmente la tercera imagen de la galería. | La tercera imagen (avatar) se renderiza por completo en la pantalla, con sus dimensiones correctas y sin iconos de error. | No ejecutado |
| **IMG_02** | Imágenes Rotas | Validar detección de imagen rota en el renderizado (Avatar 1). | - Conexión a internet estable.<br>- Acceso a la ruta `/broken_images`. | 1. Ingresar a la URL del módulo.<br>2. Observar el primer elemento de la galería. | El sistema no logra cargar el recurso. Se visualiza el icono por defecto de "imagen rota", alterando la experiencia estética. | No ejecutado |
| **IMG_03** | Imágenes Rotas | Validar detección de imagen rota en el renderizado (Avatar 2). | - Conexión a internet estable.<br>- Acceso a la ruta `/broken_images`. | 1. Ingresar a la URL del módulo.<br>2. Observar el segundo elemento de la galería. | El servidor responde con un código de error (ej. 404). En la interfaz se muestra el contenedor vacío o con el icono de error visual. | No ejecutado |
| **IMG_04** | Imágenes Rotas | Verificar la respuesta HTTP de los recursos de las imágenes (Inspección técnica). | - Herramientas de desarrollador (F12) abiertas.<br>- Pestaña "Network" (Red) activa. | 1. Recargar la página `/broken_images`.<br>2. Filtar por elementos tipo "Img".<br>3. Analizar los códigos de estado de cada archivo. | Las imágenes rotas deben registrar estados de error HTTP (como 404 Not Found), confirmando que el origen del fallo es el servidor de origen. | No ejecutado |
