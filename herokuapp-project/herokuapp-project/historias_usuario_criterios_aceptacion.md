# 📝 Historias de Usuario y Criterios de Aceptación (Autenticación)

*   **Sitio Bajo Prueba (SUT):** [the-internet.herokuapp.com](https://the-internet.herokuapp.com/)
*   **Módulo:** Control de Acceso (Login / Logout)
*   **Enfoque:** Metodologías Ágiles / Gestión de Requerimientos

---

## 👥 Historia de Usuario (User Story)

### **ID: US_01 - Inicio de Sesión y Cierre de Sistema**
> **Como** usuario registrado de la plataforma,  
> **Quiero** ingresar mis credenciales de acceso (Usuario y Contraseña) y poder cerrar sesión cuando lo requiera,  
> **Para** garantizar que mis datos y mi sesión se mantengan protegidos en entornos seguros.

---

## 📋 Criterios de Aceptación y Escenarios de Prueba

### **Escenario 1: Inicio de Sesión Exitoso**
*   **Dado que:** El usuario se encuentra en la pantalla de Login y posee credenciales válidas y activas en el sistema.
*   **Cuando:** Ingresa su nombre de usuario correcto, su contraseña correcta y hace clic en el botón "Login".
*   **Entonces:** El sistema valida los datos de forma síncrona, otorga el acceso y redirige al usuario a la pantalla de bienvenida/dashboard de la cuenta.

### **Escenario 2: Intento de Acceso con Credenciales Inválidas**
*   **Dado que:** El usuario se encuentra en la pantalla de Login.
*   **Cuando:** Ingresa un usuario o contraseña incorrectos (o inexistentes) y hace clic en "Login".
*   **Entonces:** El sistema deniega el acceso, permanece en la misma pantalla y despliega una alerta visual clara indicando el fallo de autenticación sin revelar cuál de los dos campos fue el incorrecto (por seguridad).

### **Escenario 3: Cierre de Sesión Seguro (Logout)**
*   **Dado que:** El usuario ha iniciado sesión correctamente y se encuentra dentro de su panel privado.
*   **Cuando:** Hace clic en el botón "Logout" o "Cerrar Sesión" ubicado en el menú de usuario.
*   **Entonces:** El sistema destruye los tokens/cookies de la sesión activa, restringe el acceso inmediato a las rutas privadas y redirige al usuario de vuelta a la pantalla de Login pública.
