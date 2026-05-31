# 🧪 Casos de Prueba Funcionales - Módulo de Registro

*   **Sitio Bajo Prueba (SUT):** [the-internet.herokuapp.com](https://the-internet.herokuapp.com/) (Entorno de prácticas QA)
*   **Módulo:** Registro de Nuevos Usuarios (`/register`)
*   **Tipo de Prueba:** Pruebas Manuales Funcionales / Caja Negra

---

## 📊 Matriz de Diseño de Casos de Prueba

| ID | Módulo | Caso de Prueba | Precondiciones | Pasos | Resultado Esperado | Estado |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **REG_01** | Registro de usuario | Validar obligatoriedad del nombre de usuario. | - App activa.<br>- Acceso a la página de registro.<br>- Nombre no registrado previamente. | 1. Acceder a la página.<br>2. Dejar vacío el nombre de usuario.<br>3. Completar los demás campos.<br>4. Hacer clic en "Registrarse". | El sistema muestra un mensaje advirtiendo que el campo es obligatorio e invita a completarlo para finalizar. | No ejecutado |
| **REG_02** | Registro de usuario | Validar registro de usuario con email inválido. | - App activa.<br>- Acceso a la página de registro.<br>- Email no registrado aún. | 1. Acceder a la página.<br>2. Completar campos válidos excepto email.<br>3. Ingresar email sin formato válido (ej. sin @ o sin dominio).<br>4. Hacer clic en "Registrarse". | El sistema muestra un mensaje indicando formato inválido y bloquea el envío mientras persista el error. | No ejecutado |
| **REG_03** | Registro de usuario | Validar registro de usuario con email repetido. | - App activa.<br>- Acceso a la página de registro.<br>- El email ya existe en el sistema. | 1. Acceder a la página.<br>2. Completar campos con datos válidos.<br>3. Ingresar el correo ya existente.<br>4. Hacer clic en "Registrarse". | Al presionar el botón, aparece un mensaje advirtiendo que el correo ya está registrado y se deniega la operación. | No ejecutado |
| **REG_04** | Registro de usuario | Validar registro de usuario con contraseña corta. | - App activa.<br>- Acceso a la página de registro.<br>- Restricción: entre 8 y 15 caracteres. | 1. Acceder a la página.<br>2. Completar campos válidos excepto contraseña.<br>3. Ingresar contraseña de menos de 8 caracteres.<br>4. Hacer clic en "Registrarse". | Debajo del campo se visualiza un texto explicativo. El sistema rechaza el registro por no cumplir el mínimo. | No ejecutado |
| **REG_05** | Registro de usuario | Validar registro de usuario con contraseña con espacios en blanco. | - App activa.<br>- Acceso a la página de registro.<br>- Restricción: no se permiten espacios. | 1. Acceder a la página.<br>2. Completar campos válidos.<br>3. Ingresar contraseña que contenga espacios en blanco.<br>4. Hacer clic en "Registrarse". | Debajo del campo se visualiza un texto de advertencia. El sistema muestra un mensaje de error y no procesa el registro. | No ejecutado |
