# Arquitectura del Sistema

## Proyecto

NPL Portfolio Valuation & Machine Learning

## Objetivo

Definir la arquitectura de alto nivel del sistema encargado de procesar información histórica de cartera NPL, validar y transformar datos, entrenar y evaluar modelos de Machine Learning, generar probabilidades de recuperación, realizar procesos de valoración financiera y exponer los resultados de forma trazable y reproducible.

## Alcance

La arquitectura cubrirá los componentes necesarios para:

- Ingesta de datos históricos.
- Validación de calidad de datos.
- Transformación y procesamiento.
- Persistencia de información.
- Entrenamiento y evaluación de modelos.
- Generación de predicciones de recuperación.
- Valoración financiera.
- Cálculo de VPN, TIR y ROI.
- Consulta de resultados.
- Trazabilidad y reproducibilidad.
- Generación automatizada de documentación.


## Arquitectura de alto nivel

El sistema se organizará mediante componentes desacoplados, donde cada componente
tendrá una responsabilidad específica dentro del procesamiento de una cartera NPL.

La arquitectura permitirá separar las responsabilidades relacionadas con ingeniería
de datos, Machine Learning, valoración financiera, consulta de resultados,
gobernanza y documentación.

### Flujo general

```text
FUENTES DE DATOS
      |
      v
+---------------------------+
| 1. Ingesta de datos       |
| RF-001 / CU-001           |
+-------------+-------------+
              |
              v
+---------------------------+
| 2. Calidad de datos       |
| RF-002 / CU-002           |
+-------------+-------------+
              |
              v
+---------------------------+
| 3. Transformación         |
| RF-003 / CU-003           |
+-------------+-------------+
              |
              v
+---------------------------+
| 4. Persistencia           |
| RF-004 / CU-004           |
+-------------+-------------+
              |
              v
+---------------------------+
| 5. Entrenamiento ML       |
| RF-005 / CU-005           |
+-------------+-------------+
              |
              v
+---------------------------+
| 6. Evaluación de modelos  |
| RF-006 / CU-006           |
+-------------+-------------+
              |
              v
+---------------------------+
| 7. Scoring / Predicción   |
| RF-007 / CU-007           |
+-------------+-------------+
              |
              v
+---------------------------+
| 8. Valoración financiera  |
| RF-008 / CU-008           |
+-------------+-------------+
              |
              v
+---------------------------+
| 9. Indicadores financieros|
| RF-009 / CU-009           |
+-------------+-------------+
              |
              v
+---------------------------+
| 10. Consulta resultados   |
| RF-010 / CU-010           |
+---------------------------+


## Matriz de trazabilidad arquitectónica

La siguiente matriz relaciona los requerimientos funcionales,
casos de uso y componentes arquitectónicos definidos.

| Requerimiento | Caso de uso | Componente arquitectónico |
|---|---|---|
| RF-001 | CU-001 | Ingesta de datos |
| RF-002 | CU-002 | Calidad de datos |
| RF-003 | CU-003 | Transformación de datos |
| RF-004 | CU-004 | Persistencia |
| RF-005 | CU-005 | Entrenamiento de Machine Learning |
| RF-006 | CU-006 | Evaluación y selección de modelos |
| RF-007 | CU-007 | Scoring y predicción |
| RF-008 | CU-008 | Valoración financiera |
| RF-009 | CU-009 | Indicadores financieros |
| RF-010 | CU-010 | Consulta de resultados |

Esta trazabilidad permite justificar cada componente
de la arquitectura a partir de una necesidad funcional previamente definida.


## Principios de diseño

La arquitectura seguirá los siguientes principios:

- Separación de responsabilidades.
- Bajo acoplamiento entre componentes.
- Alta cohesión dentro de cada componente.
- Trazabilidad de datos, modelos y resultados.
- Reproducibilidad de procesos analíticos.
- Validación antes de persistencia y procesamiento.
- Independencia entre lógica de negocio y tecnologías concretas.
- Facilidad de prueba y mantenimiento.
- Evolución incremental del sistema.
- Preparación para automatización y despliegue.


## Decisiones arquitectónicas iniciales

### Arquitectura modular

El sistema se desarrollará inicialmente como una arquitectura modular.

Cada dominio principal tendrá responsabilidades separadas,
aunque inicialmente pueda ejecutarse dentro de un mismo proyecto.

Los principales módulos serán:

- data_ingestion
- data_quality
- data_transformation
- persistence
- machine_learning
- scoring
- financial_valuation
- reporting
- api
- governance
- documentation

Esta decisión permite mantener una estructura clara sin introducir
prematuramente la complejidad de una arquitectura distribuida.


### Separación entre datos, Machine Learning y valoración

La lógica de ingeniería de datos, Machine Learning y valoración financiera
se mantendrá separada.

Esto permitirá:

- modificar procesos ETL sin afectar directamente los modelos;
- reemplazar modelos sin modificar la lógica financiera;
- modificar supuestos financieros sin reentrenar modelos;
- probar cada dominio de manera independiente.


### Persistencia centralizada

El sistema contará con una capa de persistencia centralizada
para almacenar información relacionada con:

- obligaciones;
- cargas de datos;
- resultados de calidad;
- datos procesados;
- modelos;
- métricas;
- predicciones;
- valoraciones;
- escenarios;
- indicadores financieros;
- trazabilidad.

La tecnología específica de base de datos se seleccionará
posteriormente durante el diseño del modelo de datos.


### Procesamiento reproducible

Los procesos de datos y Machine Learning deberán registrar
los parámetros necesarios para reproducir resultados.

Esto incluye:

- versión de datos;
- parámetros de transformación;
- variables utilizadas;
- modelo y versión;
- parámetros del modelo;
- métricas obtenidas;
- supuestos financieros;
- tasa de descuento;
- escenario analizado.


### Exposición mediante API

Los resultados del sistema deberán poder ser consultados
mediante una interfaz de aplicación.

La API permitirá desacoplar la lógica interna del sistema
de futuras interfaces gráficas, dashboards o integraciones externas.


### Documentación como componente del proyecto

La documentación será tratada como parte del sistema
y no como una actividad manual independiente.

El agente de documentación permitirá mantener trazabilidad
entre requerimientos, reglas de negocio, casos de uso,
arquitectura y futuras decisiones técnicas.


## Tecnologías candidatas

Las siguientes tecnologías se consideran candidatas iniciales
para implementar los diferentes componentes.

Estas tecnologías todavía no representan decisiones definitivas.

### Lenguaje principal

Python

Motivos:

- procesamiento de datos;
- Machine Learning;
- automatización;
- integración con librerías financieras;
- desarrollo de APIs;
- amplio ecosistema científico.


### Procesamiento de datos

Candidatos:

- pandas
- NumPy

Uso previsto:

- limpieza;
- transformación;
- análisis;
- preparación de datasets.


### Base de datos

Candidatos:

- PostgreSQL
- SQL Server

La selección definitiva dependerá del modelo de datos,
requerimientos del proyecto y facilidad de despliegue del laboratorio.


### Machine Learning

Candidatos:

- scikit-learn
- XGBoost
- LightGBM

Modelos iniciales considerados:

- Regresión Logística
- Random Forest
- XGBoost
- LightGBM


### Valoración financiera

Candidatos:

- NumPy
- SciPy
- numpy-financial

Uso previsto:

- VPN
- TIR
- ROI
- descuento de flujos
- análisis de escenarios
- simulaciones


### API

Candidato principal:

- FastAPI

Motivos:

- integración directa con Python;
- validación mediante Pydantic;
- documentación automática OpenAPI;
- buen rendimiento;
- facilidad de integración con procesos analíticos.


### Contenedores

Candidato:

- Docker

Uso previsto:

- reproducibilidad del entorno;
- despliegue;
- aislamiento de dependencias.


### Control de versiones

Tecnologías:

- Git
- GitHub

Uso previsto:

- versionamiento;
- trazabilidad de cambios;
- portafolio técnico;
- colaboración futura.


### Observabilidad

Candidatos:

- logging estructurado
- Grafana
- herramientas de métricas y monitoreo

La implementación definitiva se realizará
en una fase posterior del proyecto.


## Flujo arquitectónico resumido

El flujo principal del sistema será:

```text
Fuente de datos
    |
    v
Ingesta
    |
    v
Calidad
    |
    v
Transformación
    |
    v
Persistencia
    |
    +--------------------+
    |                    |
    v                    v
Entrenamiento ML      Consulta histórica
    |
    v
Evaluación
    |
    v
Modelo aprobado
    |
    v
Scoring
    |
    v
Probabilidad de recuperación
    |
    v
Valoración financiera
    |
    v
VPN / TIR / ROI
    |
    v
API / Consulta