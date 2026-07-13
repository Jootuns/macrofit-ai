# Arquitectura inicial de MacroFit AI

## 1. Objetivo

Este documento describe la arquitectura inicial prevista para MacroFit AI.

La arquitectura podrá evolucionar conforme avance el proyecto, pero servirá como referencia para separar correctamente las responsabilidades de cada parte de la aplicación.

## 2. Visión general

MacroFit AI estará dividida inicialmente en tres componentes principales:

1. Aplicación móvil.
2. Backend y API REST.
3. Base de datos.

En versiones posteriores se incorporarán servicios externos de inteligencia artificial y fuentes de precios de supermercados.

## 3. Flujo general

El flujo principal será:

```text
Aplicación móvil → API REST → Backend → Base de datos
```

La aplicación móvil no accederá directamente a la base de datos.

Toda consulta o modificación de información deberá pasar por el backend.

## 4. Aplicación móvil

### Tecnologías previstas

- React Native.
- Expo.
- TypeScript.

### Responsabilidades

La aplicación móvil se encargará de:

- Mostrar la interfaz al usuario.
- Recoger los datos introducidos.
- Enviar solicitudes a la API.
- Mostrar las respuestas del backend.
- Gestionar la navegación entre pantallas.
- Mostrar estados de carga y mensajes de error.
- Almacenar de forma segura la información necesaria para mantener la sesión.

La aplicación móvil no deberá:

- Contener contraseñas de bases de datos.
- Contener claves privadas de servicios externos.
- Calcular información crítica que pueda manipularse fácilmente.
- Acceder directamente a PostgreSQL.

## 5. Backend

### Tecnologías previstas

- Python.
- FastAPI.
- SQLAlchemy.
- Alembic.
- Pydantic.

### Responsabilidades

El backend se encargará de:

- Recibir las solicitudes de la aplicación móvil.
- Validar los datos recibidos.
- Aplicar las reglas de negocio.
- Calcular calorías y macronutrientes.
- Gestionar usuarios y sesiones.
- Consultar y modificar la base de datos.
- Crear planes nutricionales.
- Generar listas de la compra.
- Gestionar rutinas y registros de progreso.
- Comunicarse con servicios externos.
- Devolver respuestas estructuradas a la aplicación.

## 6. API REST

La aplicación móvil y el backend se comunicarán mediante una API REST utilizando HTTP.

Las operaciones principales serán:

- `GET`: obtener información.
- `POST`: crear información.
- `PUT` o `PATCH