# Arquitectura del sistema - NPL Portfolio Valuation & Machine Learning

## Objetivo

Definir la arquitectura lógica inicial del sistema NPL, relacionando cada componente con los requerimientos funcionales, casos de uso y reglas de negocio que justifican su existencia.

## Componentes arquitectónicos

### ARC-001 - Ingesta de datos

Componente responsable de recibir e incorporar los datos históricos de cartera al sistema.

#### Requerimientos funcionales relacionados

##### RF-001 - Carga de datos históricos

El sistema deberá permitir incorporar información histórica relacionada con créditos.

**Prioridad:** high

**Estado:** draft

#### Casos de uso relacionados

##### CU-001 - Carga de datos históricos

Permitir incorporar información histórica de créditos para su posterior validación, transformación y análisis.

#### Reglas de negocio relacionadas

##### RN-001 - Validación de estructura de datos

Todo archivo o conjunto de datos cargado al sistema deberá cumplir con la estructura esperada y contener los campos obligatorios antes de iniciar cualquier procesamiento.

**Categoría:** data_quality

**Prioridad:** high

##### RN-021 - Identificación única de obligaciones

Cada obligación o crédito deberá contar con un identificador único que permita mantener trazabilidad durante todo el procesamiento.

**Categoría:** data_governance

**Prioridad:** high

##### RN-022 - Consistencia del saldo de obligación

El saldo de una obligación deberá ser mayor o igual a cero y deberá representar el valor vigente utilizado para análisis.

**Categoría:** data_quality

**Prioridad:** high

##### RN-023 - Consistencia de fechas

Las fechas asociadas a una obligación deberán mantener una secuencia temporal válida y no podrán contener inconsistencias lógicas.

**Categoría:** data_quality

**Prioridad:** high

---

### ARC-002 - Calidad de datos

Componente responsable de validar estructura, duplicados, valores inválidos y consistencia de la información recibida.

#### Requerimientos funcionales relacionados

##### RF-002 - Validación de calidad de datos

El sistema deberá validar estructura, campos obligatorios, duplicados, valores nulos e inconsistencias.

**Prioridad:** high

**Estado:** draft

#### Casos de uso relacionados

##### CU-002 - Validación de calidad de datos

Verificar que los datos cargados cumplan con las condiciones mínimas de calidad necesarias para continuar el procesamiento.

#### Reglas de negocio relacionadas

##### RN-001 - Validación de estructura de datos

Todo archivo o conjunto de datos cargado al sistema deberá cumplir con la estructura esperada y contener los campos obligatorios antes de iniciar cualquier procesamiento.

**Categoría:** data_quality

**Prioridad:** high

##### RN-002 - Control de registros duplicados

El sistema deberá identificar registros duplicados antes de persistir la información y deberá aplicar la estrategia de tratamiento definida para evitar duplicidad en los análisis.

**Categoría:** data_quality

**Prioridad:** high

##### RN-003 - Control de valores inválidos

Los registros con valores nulos, formatos incorrectos, inconsistencias lógicas o valores fuera de los rangos permitidos deberán ser identificados durante el proceso de calidad de datos.

**Categoría:** data_quality

**Prioridad:** high

##### RN-021 - Identificación única de obligaciones

Cada obligación o crédito deberá contar con un identificador único que permita mantener trazabilidad durante todo el procesamiento.

**Categoría:** data_governance

**Prioridad:** high

##### RN-022 - Consistencia del saldo de obligación

El saldo de una obligación deberá ser mayor o igual a cero y deberá representar el valor vigente utilizado para análisis.

**Categoría:** data_quality

**Prioridad:** high

##### RN-023 - Consistencia de fechas

Las fechas asociadas a una obligación deberán mantener una secuencia temporal válida y no podrán contener inconsistencias lógicas.

**Categoría:** data_quality

**Prioridad:** high

---

### ARC-003 - Transformación de datos

Componente encargado de limpiar, estandarizar y transformar los datos antes de su persistencia y procesamiento analítico.

#### Requerimientos funcionales relacionados

##### RF-003 - Transformación de datos

El sistema deberá limpiar y transformar los datos antes de utilizarlos para análisis y entrenamiento de modelos.

**Prioridad:** high

**Estado:** draft

#### Casos de uso relacionados

##### CU-003 - Transformación de datos

Limpiar, normalizar y transformar los datos previamente validados para dejarlos listos para análisis, modelado y valoración.

#### Reglas de negocio relacionadas

##### RN-003 - Control de valores inválidos

Los registros con valores nulos, formatos incorrectos, inconsistencias lógicas o valores fuera de los rangos permitidos deberán ser identificados durante el proceso de calidad de datos.

**Categoría:** data_quality

**Prioridad:** high

##### RN-021 - Identificación única de obligaciones

Cada obligación o crédito deberá contar con un identificador único que permita mantener trazabilidad durante todo el procesamiento.

**Categoría:** data_governance

**Prioridad:** high

##### RN-022 - Consistencia del saldo de obligación

El saldo de una obligación deberá ser mayor o igual a cero y deberá representar el valor vigente utilizado para análisis.

**Categoría:** data_quality

**Prioridad:** high

##### RN-023 - Consistencia de fechas

Las fechas asociadas a una obligación deberán mantener una secuencia temporal válida y no podrán contener inconsistencias lógicas.

**Categoría:** data_quality

**Prioridad:** high

---

### ARC-004 - Persistencia

Componente responsable de almacenar información validada y transformada manteniendo integridad y trazabilidad.

#### Requerimientos funcionales relacionados

##### RF-004 - Persistencia de información

El sistema deberá almacenar los datos procesados en una base de datos.

**Prioridad:** high

**Estado:** draft

#### Casos de uso relacionados

##### CU-004 - Persistencia de información

Almacenar de forma controlada la información procesada garantizando consistencia, trazabilidad y disponibilidad.

#### Reglas de negocio relacionadas

##### RN-004 - Persistencia posterior a validación

La información solo podrá ser almacenada como información procesada después de superar las validaciones de calidad definidas.

**Categoría:** data_engineering

**Prioridad:** high

##### RN-021 - Identificación única de obligaciones

Cada obligación o crédito deberá contar con un identificador único que permita mantener trazabilidad durante todo el procesamiento.

**Categoría:** data_governance

**Prioridad:** high

##### RN-024 - Reproducibilidad de resultados

Los procesos analíticos y de Machine Learning deberán registrar parámetros suficientes para permitir reproducir los resultados obtenidos.

**Categoría:** governance

**Prioridad:** medium

---

### ARC-005 - Entrenamiento de Machine Learning

Componente encargado de preparar datasets, entrenar modelos y registrar sus parámetros y resultados.

#### Requerimientos funcionales relacionados

##### RF-005 - Entrenamiento de modelos

El sistema deberá permitir entrenar diferentes modelos de Machine Learning para estimar probabilidades relacionadas con la recuperación.

**Prioridad:** high

**Estado:** draft

#### Casos de uso relacionados

##### CU-005 - Entrenamiento de modelos

Entrenar modelos de Machine Learning utilizando información histórica preparada para estimar probabilidades de recuperación.

#### Reglas de negocio relacionadas

##### RN-005 - Evaluación obligatoria de modelos

Todo modelo de Machine Learning deberá ser evaluado mediante métricas definidas antes de ser considerado válido para generar predicciones.

**Categoría:** machine_learning

**Prioridad:** high

##### RN-016 - Separación entre entrenamiento y evaluación

Los datos utilizados para evaluar un modelo no deberán utilizarse simultáneamente como datos de entrenamiento del mismo modelo.

**Categoría:** machine_learning

**Prioridad:** high

##### RN-017 - Control de fuga de información

Las variables utilizadas por los modelos no deberán contener información futura o información que no estaría disponible en el momento real de realizar una predicción.

**Categoría:** machine_learning

**Prioridad:** high

##### RN-018 - Registro de métricas del modelo

Las métricas obtenidas durante la evaluación de los modelos deberán almacenarse para permitir comparación, auditoría y backtesting.

**Categoría:** machine_learning

**Prioridad:** medium

##### RN-024 - Reproducibilidad de resultados

Los procesos analíticos y de Machine Learning deberán registrar parámetros suficientes para permitir reproducir los resultados obtenidos.

**Categoría:** governance

**Prioridad:** medium

---

### ARC-006 - Evaluación y selección de modelos

Componente responsable de calcular métricas, comparar modelos y seleccionar modelos aprobados.

#### Requerimientos funcionales relacionados

##### RF-006 - Comparación de modelos

El sistema deberá comparar los modelos utilizando métricas de evaluación definidas.

**Prioridad:** high

**Estado:** draft

#### Casos de uso relacionados

##### CU-006 - Comparación de modelos

Comparar el desempeño de los modelos entrenados mediante métricas definidas para seleccionar el modelo más adecuado.

#### Reglas de negocio relacionadas

##### RN-005 - Evaluación obligatoria de modelos

Todo modelo de Machine Learning deberá ser evaluado mediante métricas definidas antes de ser considerado válido para generar predicciones.

**Categoría:** machine_learning

**Prioridad:** high

##### RN-006 - Comparación de modelos

Cuando existan múltiples modelos candidatos, el sistema deberá comparar sus métricas y seleccionar el modelo que cumpla los criterios de aceptación definidos para el proyecto.

**Categoría:** machine_learning

**Prioridad:** high

##### RN-018 - Registro de métricas del modelo

Las métricas obtenidas durante la evaluación de los modelos deberán almacenarse para permitir comparación, auditoría y backtesting.

**Categoría:** machine_learning

**Prioridad:** medium

##### RN-019 - Backtesting de modelos

Los modelos aprobados deberán poder compararse posteriormente contra resultados reales para evaluar su desempeño histórico.

**Categoría:** model_validation

**Prioridad:** medium

---

### ARC-007 - Scoring y predicción

Componente responsable de generar probabilidades de recuperación utilizando modelos aprobados.

#### Requerimientos funcionales relacionados

##### RF-007 - Predicción de recuperación

El sistema deberá estimar la probabilidad de recuperación asociada a cada obligación.

**Prioridad:** high

**Estado:** draft

#### Casos de uso relacionados

##### CU-007 - Predicción de recuperación

Estimar la probabilidad de recuperación asociada a cada obligación utilizando un modelo previamente evaluado y aprobado.

#### Reglas de negocio relacionadas

##### RN-007 - Predicciones basadas en modelos aprobados

Las probabilidades de recuperación solo podrán generarse utilizando modelos previamente evaluados y aprobados.

**Categoría:** machine_learning

**Prioridad:** high

##### RN-008 - Probabilidad de recuperación acotada

Toda probabilidad estimada de recuperación deberá encontrarse en un rango entre 0 y 1.

**Categoría:** machine_learning

**Prioridad:** high

##### RN-014 - Trazabilidad del modelo utilizado

Toda predicción deberá mantener referencia al modelo y versión utilizados para generar el resultado.

**Categoría:** governance

**Prioridad:** high

##### RN-017 - Control de fuga de información

Las variables utilizadas por los modelos no deberán contener información futura o información que no estaría disponible en el momento real de realizar una predicción.

**Categoría:** machine_learning

**Prioridad:** high

##### RN-024 - Reproducibilidad de resultados

Los procesos analíticos y de Machine Learning deberán registrar parámetros suficientes para permitir reproducir los resultados obtenidos.

**Categoría:** governance

**Prioridad:** medium

---

### ARC-008 - Valoración financiera

Componente encargado de proyectar recuperaciones y realizar la valoración económica de las carteras.

#### Requerimientos funcionales relacionados

##### RF-008 - Valoración de cartera

El sistema deberá generar estimaciones financieras relacionadas con una cartera analizada.

**Prioridad:** high

**Estado:** draft

#### Casos de uso relacionados

##### CU-008 - Valoración de cartera

Estimar el valor económico de una cartera utilizando las recuperaciones esperadas, los costos y los supuestos financieros definidos.

#### Reglas de negocio relacionadas

##### RN-009 - Valoración basada en recuperación esperada

La valoración financiera de una cartera deberá considerar la recuperación esperada estimada a partir de los resultados analíticos y predictivos.

**Categoría:** financial_valuation

**Prioridad:** high

##### RN-011 - Aplicación de tasa de descuento

Los flujos futuros utilizados para calcular el VPN deberán descontarse utilizando una tasa de descuento definida para el escenario de valoración.

**Categoría:** financial_valuation

**Prioridad:** high

##### RN-012 - Consideración de costos de recuperación

La valoración deberá considerar los costos asociados al proceso de recuperación cuando dichos costos se encuentren disponibles.

**Categoría:** financial_valuation

**Prioridad:** medium

##### RN-013 - Flujos de recuperación no negativos

Los flujos de recuperación proyectados no podrán registrar valores negativos salvo que correspondan explícitamente a costos o egresos asociados.

**Categoría:** financial_valuation

**Prioridad:** medium

##### RN-015 - Trazabilidad de resultados financieros

Toda valoración deberá mantener referencia a los datos, supuestos, parámetros financieros y resultados utilizados en su cálculo.

**Categoría:** governance

**Prioridad:** high

##### RN-020 - Escenarios de valoración

El sistema deberá permitir diferenciar escenarios de valoración, como mínimo un escenario base y escenarios alternativos cuando se realicen análisis de sensibilidad o simulación.

**Categoría:** financial_valuation

**Prioridad:** medium

---

### ARC-009 - Indicadores financieros

Componente responsable de calcular VPN, TIR, ROI y otros indicadores derivados de la valoración.

#### Requerimientos funcionales relacionados

##### RF-009 - Cálculo de indicadores financieros

El sistema deberá permitir calcular indicadores como VPN, TIR y ROI.

**Prioridad:** medium

**Estado:** draft

#### Casos de uso relacionados

##### CU-009 - Cálculo de indicadores financieros

Calcular indicadores financieros que permitan analizar la rentabilidad y conveniencia económica de una cartera.

#### Reglas de negocio relacionadas

##### RN-010 - Cálculo obligatorio de indicadores financieros

El proceso de valoración deberá permitir calcular como mínimo VPN, TIR y ROI cuando exista información suficiente para ello.

**Categoría:** financial_valuation

**Prioridad:** high

##### RN-011 - Aplicación de tasa de descuento

Los flujos futuros utilizados para calcular el VPN deberán descontarse utilizando una tasa de descuento definida para el escenario de valoración.

**Categoría:** financial_valuation

**Prioridad:** high

##### RN-012 - Consideración de costos de recuperación

La valoración deberá considerar los costos asociados al proceso de recuperación cuando dichos costos se encuentren disponibles.

**Categoría:** financial_valuation

**Prioridad:** medium

##### RN-013 - Flujos de recuperación no negativos

Los flujos de recuperación proyectados no podrán registrar valores negativos salvo que correspondan explícitamente a costos o egresos asociados.

**Categoría:** financial_valuation

**Prioridad:** medium

##### RN-015 - Trazabilidad de resultados financieros

Toda valoración deberá mantener referencia a los datos, supuestos, parámetros financieros y resultados utilizados en su cálculo.

**Categoría:** governance

**Prioridad:** high

##### RN-020 - Escenarios de valoración

El sistema deberá permitir diferenciar escenarios de valoración, como mínimo un escenario base y escenarios alternativos cuando se realicen análisis de sensibilidad o simulación.

**Categoría:** financial_valuation

**Prioridad:** medium

---

### ARC-010 - Consulta de resultados

Componente responsable de exponer y consultar predicciones, métricas, valoraciones e indicadores.

#### Requerimientos funcionales relacionados

##### RF-010 - Consulta de resultados

El sistema deberá permitir consultar resultados de predicción y valoración.

**Prioridad:** medium

**Estado:** draft

#### Casos de uso relacionados

##### CU-010 - Consulta de resultados

Permitir consultar los resultados generados por los procesos de predicción, evaluación de modelos y valoración financiera.

#### Reglas de negocio relacionadas

##### RN-014 - Trazabilidad del modelo utilizado

Toda predicción deberá mantener referencia al modelo y versión utilizados para generar el resultado.

**Categoría:** governance

**Prioridad:** high

##### RN-015 - Trazabilidad de resultados financieros

Toda valoración deberá mantener referencia a los datos, supuestos, parámetros financieros y resultados utilizados en su cálculo.

**Categoría:** governance

**Prioridad:** high

##### RN-018 - Registro de métricas del modelo

Las métricas obtenidas durante la evaluación de los modelos deberán almacenarse para permitir comparación, auditoría y backtesting.

**Categoría:** machine_learning

**Prioridad:** medium

##### RN-024 - Reproducibilidad de resultados

Los procesos analíticos y de Machine Learning deberán registrar parámetros suficientes para permitir reproducir los resultados obtenidos.

**Categoría:** governance

**Prioridad:** medium

---

## Componentes transversales

### ARC-X01 - Gobernanza y trazabilidad

Responsabilidad transversal para registrar origen de datos, procesos, modelos, parámetros, métricas y resultados.

#### Reglas de negocio relacionadas

##### RN-014 - Trazabilidad del modelo utilizado

Toda predicción deberá mantener referencia al modelo y versión utilizados para generar el resultado.

**Categoría:** governance

**Prioridad:** high

##### RN-015 - Trazabilidad de resultados financieros

Toda valoración deberá mantener referencia a los datos, supuestos, parámetros financieros y resultados utilizados en su cálculo.

**Categoría:** governance

**Prioridad:** high

##### RN-018 - Registro de métricas del modelo

Las métricas obtenidas durante la evaluación de los modelos deberán almacenarse para permitir comparación, auditoría y backtesting.

**Categoría:** machine_learning

**Prioridad:** medium

##### RN-021 - Identificación única de obligaciones

Cada obligación o crédito deberá contar con un identificador único que permita mantener trazabilidad durante todo el procesamiento.

**Categoría:** data_governance

**Prioridad:** high

##### RN-024 - Reproducibilidad de resultados

Los procesos analíticos y de Machine Learning deberán registrar parámetros suficientes para permitir reproducir los resultados obtenidos.

**Categoría:** governance

**Prioridad:** medium

---

### ARC-X02 - Documentación automatizada

Responsabilidad transversal para generar documentación estructurada y trazable a partir de las fuentes de verdad del proyecto.

---

## Matriz de trazabilidad

| Componente | Requerimiento funcional | Caso de uso |
|---|---|---|
| ARC-001 - Ingesta de datos | RF-001 - Carga de datos históricos | CU-001 - Carga de datos históricos |
| ARC-002 - Calidad de datos | RF-002 - Validación de calidad de datos | CU-002 - Validación de calidad de datos |
| ARC-003 - Transformación de datos | RF-003 - Transformación de datos | CU-003 - Transformación de datos |
| ARC-004 - Persistencia | RF-004 - Persistencia de información | CU-004 - Persistencia de información |
| ARC-005 - Entrenamiento de Machine Learning | RF-005 - Entrenamiento de modelos | CU-005 - Entrenamiento de modelos |
| ARC-006 - Evaluación y selección de modelos | RF-006 - Comparación de modelos | CU-006 - Comparación de modelos |
| ARC-007 - Scoring y predicción | RF-007 - Predicción de recuperación | CU-007 - Predicción de recuperación |
| ARC-008 - Valoración financiera | RF-008 - Valoración de cartera | CU-008 - Valoración de cartera |
| ARC-009 - Indicadores financieros | RF-009 - Cálculo de indicadores financieros | CU-009 - Cálculo de indicadores financieros |
| ARC-010 - Consulta de resultados | RF-010 - Consulta de resultados | CU-010 - Consulta de resultados |
