# Backlog de MacroFit AI

## Estados

Las tareas podrán encontrarse en uno de estos estados:

- Pendiente
- En progreso
- Terminada
- Bloqueada

## Prioridades

- Alta: necesaria para que el MVP funcione.
- Media: importante, pero no bloquea las funciones esenciales.
- Baja: mejora opcional o correspondiente a una versión posterior.

---

## Fase 0 - Preparación del proyecto

- [x] Instalar Git.
- [x] Instalar Python y pip.
- [x] Instalar Node.js y npm.
- [x] Configurar la identidad de Git.
- [x] Crear el repositorio local.
- [x] Crear el repositorio en GitHub.
- [x] Crear las ramas main y develop.
- [x] Crear README.md y .gitignore.
- [x] Definir el MVP inicial.
- [x] Documentar el primer bloque del proyecto.
- [x] Definir la arquitectura inicial.
- [x] Establecer las convenciones del proyecto.

---

## Fase 1 - Fundamentos del backend

Prioridad: alta.

- [x] Entender qué es un backend.
- [x] Entender qué es una API REST.
- [x] Crear un entorno virtual de Python.
- [x] Instalar FastAPI.
- [x] Instalar el servidor Uvicorn.
- [x] Crear la estructura inicial del backend.
- [x] Crear el primer endpoint.
- [x] Ejecutar la API localmente.
- [x] Consultar la documentación automática de Swagger.
- [x] Separar el backend por capas.
- [x] Crear routers independientes.
- [x] Crear services para la lógica de negocio.
- [x] Crear repositories para acceso a datos.
- [x] Crear schemas para validación de datos.
- [x] Organizar el proyecto mediante paquetes Python (__init__.py).
- [ ] Añadir pruebas básicas.
- [ ] Documentar cómo ejecutar el backend.

---

## Fase 2 - Base de datos

Prioridad: alta.

- [ ] Instalar y configurar PostgreSQL.
- [ ] Diseñar el modelo entidad-relación.
- [ ] Configurar SQLAlchemy.
- [ ] Configurar migraciones con Alembic.
- [ ] Crear la tabla de usuarios.
- [ ] Crear la tabla de perfiles.
- [ ] Crear la tabla de seguimiento de peso.
- [ ] Crear la tabla de objetivos nutricionales.
- [ ] Crear la tabla de alimentos.
- [ ] Crear la tabla de recetas.
- [ ] Crear la tabla de ingredientes de recetas.
- [ ] Crear las tablas de planes nutricionales.
- [ ] Crear las tablas de rutinas deportivas.
- [ ] Añadir datos iniciales para desarrollo.

---

## Fase 3 - Autenticación y usuarios

Prioridad: alta.

- [ ] Crear el registro de usuarios.
- [ ] Crear el flujo de completar perfil tras el registro.
- [ ] Proteger las contraseñas mediante hash.
- [ ] Crear el inicio de sesión.
- [ ] Implementar autenticación mediante JWT.
- [ ] Crear el cierre de sesión.
- [ ] Consultar el perfil.
- [ ] Modificar el perfil.
- [ ] Configurar idioma preferido.
- [ ] Validar los datos enviados por el usuario.
- [ ] Añadir pruebas de autenticación.

---

## Fase 4 - Cálculo nutricional

Prioridad: alta.

- [ ] Definir las fórmulas utilizadas.
- [ ] Calcular el metabolismo basal.
- [ ] Calcular el gasto energético diario.
- [ ] Adaptar las calorías al objetivo.
- [ ] Calcular proteínas, grasas y carbohidratos.
- [ ] Crear los endpoints de cálculo.
- [ ] Guardar los resultados del usuario.
- [ ] Mantener historial de macros generados.
- [ ] Añadir pruebas para las fórmulas.
- [ ] Documentar las decisiones nutricionales.

---

## Fase 5 - Aplicación móvil

Prioridad: alta.

- [ ] Entender los fundamentos de React.
- [ ] Entender TypeScript básico.
- [ ] Crear el proyecto con React Native y Expo.
- [ ] Definir la navegación.
- [ ] Crear la pantalla de bienvenida.
- [ ] Crear las pantallas de registro e inicio de sesión.
- [ ] Crear la pantalla de completar perfil.
- [ ] Crear la pantalla del perfil.
- [ ] Crear la pantalla de macros.
- [ ] Crear soporte multidioma.
- [ ] Conectar la aplicación con la API.
- [ ] Gestionar errores y estados de carga.

---

## Fase 6 - Planificación de comidas

Prioridad: alta.

- [ ] Crear el catálogo inicial de alimentos.
- [ ] Clasificar alimentos por categorías.
- [ ] Crear comidas a partir de alimentos.
- [ ] Crear recetas personalizadas.
- [ ] Crear un plan diario.
- [ ] Crear un plan semanal.
- [ ] Comparar el plan con los macros del usuario.
- [ ] Permitir sustituir alimentos.
- [ ] Guardar recetas favoritas.
- [ ] Mostrar el plan en la aplicación móvil.

---

## Fase 7 - Lista de la compra

Prioridad: alta.

- [ ] Obtener ingredientes desde el plan semanal.
- [ ] Agrupar alimentos repetidos.
- [ ] Calcular cantidades totales.
- [ ] Organizar los productos por categoría.
- [ ] Permitir marcar productos como comprados.
- [ ] Mostrar la lista en la aplicación móvil.

---

## Fase 8 - Entrenamiento y progreso

Prioridad: media.

- [ ] Crear ejercicios.
- [ ] Crear rutinas.
- [ ] Adaptar rutinas al objetivo y los días disponibles.
- [ ] Registrar entrenamientos.
- [ ] Registrar peso corporal.
- [ ] Mantener historial de peso.
- [ ] Mostrar la evolución del peso.
- [ ] Mostrar gráficas de progreso.
- [ ] Añadir otros indicadores de progreso.

---

## Fase 9 - Inteligencia artificial

Prioridad: media.

- [ ] Definir qué decisiones podrá tomar la IA.
- [ ] Definir qué decisiones no dependerán de la IA.
- [ ] Integrar una API de inteligencia artificial.
- [ ] Generar explicaciones personalizadas.
- [ ] Proponer sustituciones de alimentos.
- [ ] Adaptar planes según preferencias.
- [ ] Generar recetas automáticamente.
- [ ] Generar planes nutricionales automáticamente.
- [ ] Generar recomendaciones personalizadas.
- [ ] Ajustar macros según el progreso.
- [ ] Controlar costes y límites de uso.
- [ ] Validar las respuestas generadas.

---

## Fase 10 - Comparación inteligente de precios

Prioridad: posterior al MVP.

- [ ] Investigar fuentes de precios legalmente utilizables.
- [ ] Diseñar el modelo de supermercados.
- [ ] Diseñar el modelo de productos comerciales.
- [ ] Relacionar alimentos con productos reales.
- [ ] Guardar precios y fechas de actualización.
- [ ] Guardar histórico de precios.
- [ ] Detectar ofertas activas.
- [ ] Comparar precios entre supermercados.
- [ ] Optimizar una compra entre varios supermercados.
- [ ] Mostrar ahorro estimado.
- [ ] Integrar el comparador con la lista de la compra.

---

## Fase 11 - Escaneo nutricional

Prioridad: posterior al MVP.

- [ ] Escanear productos mediante código de barras.
- [ ] Obtener información nutricional automáticamente.
- [ ] Buscar productos mediante código EAN.
- [ ] Añadir alimentos escaneados al diario nutricional.
- [ ] Escanear tickets de compra.
- [ ] Analizar platos mediante fotografía.
- [ ] Detectar ingredientes mediante IA.
- [ ] Estimar cantidades mediante IA.
- [ ] Calcular macros aproximados a partir de imágenes.
- [ ] Registrar automáticamente comidas detectadas.

---

## Fase 12 - Comunidad y recetas

Prioridad: posterior al MVP.

- [ ] Crear recetas propias.
- [ ] Editar recetas.
- [ ] Eliminar recetas.
- [ ] Compartir recetas públicamente.
- [ ] Guardar recetas favoritas.
- [ ] Valorar recetas.
- [ ] Comentar recetas.
- [ ] Subir fotografías de recetas.
- [ ] Generar recetas mediante IA.
- [ ] Crear planes semanales a partir de recetas.
- [ ] Recomendar recetas según objetivos y macros.

---

## Fase 13 - Comunidad fitness

Prioridad: posterior al MVP.

- [ ] Crear publicaciones.
- [ ] Editar publicaciones.
- [ ] Eliminar publicaciones.
- [ ] Compartir fotografías de progreso.
- [ ] Compartir rutinas de entrenamiento.
- [ ] Compartir experiencias y consejos.
- [ ] Comentar publicaciones.
- [ ] Dar "me gusta" a publicaciones.
- [ ] Seguir usuarios.
- [ ] Crear retos fitness.
- [ ] Mostrar contenido recomendado.

---

## Fase 14 - Calidad y producción

Prioridad: alta antes del lanzamiento.

- [ ] Configurar variables de entorno.
- [ ] Crear pruebas automáticas.
- [ ] Configurar integración continua.
- [ ] Crear contenedores con Docker.
- [ ] Preparar una base de datos de producción.
- [ ] Desplegar el backend.
- [ ] Configurar registros y seguimiento de errores.
- [ ] Revisar seguridad y privacidad.
- [ ] Crear copias de seguridad.
- [ ] Preparar una demostración pública.
- [ ] Mejorar el README para portfolio.
- [ ] Preparar la presentación para LinkedIn.