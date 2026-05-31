# 🚀 QA Practice – API Testing con Postman (JSONPlaceholder)

Este módulo recopila el diseño de pruebas automatizadas sobre servicios de Backend (APIs) utilizando **Postman**, aplicando scripts de validación en JavaScript para asegurar la integridad de las respuestas, la estructura de los datos y el manejo correcto de errores.

---

## 📋 Estrategia de Pruebas y Cobertura

Las pruebas se ejecutaron sobre la API pública de **JSONPlaceholder**. Adicionalmente, se realizó una prueba exploratoria sobre *Reqres*, la cual fue descartada debido a cambios en sus políticas de autenticación (requerimiento de API Key) que impedían flujos libres de automatización.

Se validaron múltiples métodos HTTP bajo dos enfoques principales:
1. **Casos Positivos (Happy Path):** Respuestas correctas del servidor, presencia de propiedades clave y tipos de datos válidos.
2. **Casos Negativos (Edge Cases):** Manejo de recursos inexistentes y verificación de códigos de estado de error controlados.

---

## 🛠️ Detalle de los Scripts de Prueba (JavaScript - PM API)

### 1. Endpoint: `GET /posts` (Listado Completo)
Validación orientada a asegurar que el servidor devuelva la colección completa de publicaciones y que ningún elemento contenga información rota o ausente.

```javascript
let respuesta = pm.response.json();

// Validación del código de estado HTTP
pm.test("Status es 200", function () {
    pm.response.to.have.status(200);
});

// Verificación de la estructura del objeto receptor
pm.test("La respuesta es una lista", function () {
    pm.expect(respuesta).to.be.an("array");
});

pm.test("La lista no está vacía", function () {
    pm.expect(respuesta.length).to.be.above(0);
});

// Bucle de integridad: Valida que CADA post posea un ID y un título válido
respuesta.forEach(function(post) {
    pm.expect(post.id).to.exist;
});

pm.test("Todos los posts tienen title no vacío", function () {
    respuesta.forEach(function(post) {
        pm.expect(post.title).to.not.be.empty;
    });
});

let respuesta = pm.response.json();

pm.test("Status es 200", function () {
    pm.response.to.have.status(200);
});

pm.test("El id devuelto es 1", function () {
    pm.expect(respuesta.id).to.eql(1);
});

pm.test("El cuerpo (body) de la publicación no está vacío", function () {
    pm.expect(respuesta.body).to.not.be.empty;
});

pm.test("Status es 404", function () {
    pm.response.to.have.status(404);
});

pm.test("La respuesta del cuerpo está vacía", function () {
    let respuesta = pm.response.json();
    pm.expect(Object.keys(respuesta).length).to.eql(0);
});

