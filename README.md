````markdown
# NPL Portfolio Valuation & Machine Learning

Proyecto orientado al análisis y valoración de carteras NPL
(Non-Performing Loans), combinando:

- Data Engineering
- Data Science
- Machine Learning
- Financial Valuation
- Software Engineering
- Automatización de documentación con agentes de IA

---

## Objetivo del proyecto

Construir una plataforma capaz de:

- procesar información histórica de créditos,
- validar y transformar datos,
- entrenar modelos de Machine Learning,
- estimar probabilidades de recuperación,
- apoyar procesos de valoración financiera,
- calcular indicadores como VPN, TIR y ROI,
- generar documentación técnica automáticamente.

---

# Arquitectura del sistema documental

La documentación del proyecto parte de archivos YAML que funcionan
como fuente de verdad.

```text
requirements/
    project.yaml
    actors.yaml
    functional_requirements.yaml
    business_rules.yaml
            ↓
    Pydantic Models
            ↓
         Loaders
            ↓
      ContextBuilder
            ↓
   DocumentationAgent
            ↓
         LLMClient
            ↓
      Output Validation
            ↓
     MarkdownRenderer
            ↓
docs/use_cases/*.md
````

El modelo de IA no constituye la fuente de verdad.

Los archivos YAML contienen la información oficial del proyecto.

La IA puede proponer documentación, pero las referencias generadas
son verificadas antes de aceptar el resultado.

---

# Estructura principal

```text
npl-portfolio-ml/
│
├── agents/
│   └── documentation_agent/
│       ├── agent.py
│       ├── context_builder.py
│       ├── index_renderer.py
│       ├── llm_client.py
│       ├── loader.py
│       ├── markdown_renderer.py
│       ├── models.py
│       ├── project_loader.py
│       └── validators.py
│
├── docs/
│   ├── architecture/
│   ├── business_rules/
│   ├── data/
│   ├── machine_learning/
│   ├── requirements/
│   └── use_cases/
│       ├── README.md
│       ├── CU-001.md
│       ├── CU-002.md
│       ├── CU-003.md
│       ├── CU-004.md
│       ├── CU-005.md
│       ├── CU-006.md
│       ├── CU-007.md
│       ├── CU-008.md
│       ├── CU-009.md
│       └── CU-010.md
│
├── prompts/
│   └── use_case_prompt.txt
│
├── requirements/
│   ├── actors.yaml
│   ├── business_rules.yaml
│   ├── functional_requirements.yaml
│   └── project.yaml
│
├── scripts/
│   ├── generate_all_use_cases.py
│   ├── generate_use_case_index.py
│   ├── test_actors.py
│   ├── test_context.py
│   ├── test_documentation_agent.py
│   ├── test_markdown_renderer.py
│   ├── test_requirements.py
│   └── validate_documentation_coverage.py
│
├── tests/
│   └── fake_llm_client.py
│
├── src/
│   └── npl/
│
├── requirements.txt
└── README.md
```

---

# Configuración del entorno

El proyecto utiliza Python 3.11.

Crear entorno virtual:

```bash
python3.11 -m venv .venv
```

Activarlo:

```bash
source .venv/bin/activate
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

---

# Comandos principales

## Validar requerimientos

```bash
python -m scripts.test_requirements
```

## Validar actores

```bash
python -m scripts.test_actors
```

## Validar contexto documental

```bash
python -m scripts.test_context
```

## Probar DocumentationAgent

```bash
python -m scripts.test_documentation_agent
```

## Generar todos los casos de uso

```bash
python -m scripts.generate_all_use_cases
```

Este comando genera:

```text
docs/use_cases/CU-001.md
...
docs/use_cases/CU-010.md
```

## Generar índice de casos de uso

```bash
python -m scripts.generate_use_case_index
```

Genera:

```text
docs/use_cases/README.md
```

## Validar cobertura documental

```bash
python -m scripts.validate_documentation_coverage
```

Este proceso comprueba que cada requerimiento funcional tenga
un caso de uso asociado.

Ejemplo esperado:

```text
RF-001 -> CU-001 -> OK
RF-002 -> CU-002 -> OK
...
RF-010 -> CU-010 -> OK

FASE 1: COBERTURA VALIDADA
```

---

# Trazabilidad documental

El sistema mantiene relaciones entre:

```text
Actor
  ↓
ACT-XXX

Requerimiento funcional
  ↓
RF-XXX

Caso de uso
  ↓
CU-XXX

Regla de negocio
  ↓
RN-XXX
```

Ejemplo:

```text
RF-006 - Comparación de modelos
        ↓
CU-006 - Comparación de modelos
        ↓
RN-005 - Evaluación obligatoria de modelos
RN-006 - Comparación de modelos
```

Las referencias se validan automáticamente antes de aceptar
un caso de uso.

---

# Validaciones implementadas

Actualmente existen tres niveles de validación.

### Validación estructural

Pydantic verifica la estructura de:

* requerimientos,
* actores,
* reglas de negocio,
* casos de uso.

### Validación de referencias

El sistema comprueba que existan:

```text
ACT-XXX
RF-XXX
RN-XXX
```

Si una IA genera, por ejemplo:

```text
ACT-999
```

el sistema rechaza la respuesta.

### Validación de cobertura

Se comprueba que cada:

```text
RF-XXX
```

tenga su correspondiente:

```text
CU-XXX.md
```

---

# Fases del proyecto

## Fase 1 - Levantamiento de requerimientos

Estado:

```text
COMPLETADA
```

Componentes terminados:

* definición del proyecto,
* definición de actores,
* requerimientos funcionales,
* reglas de negocio,
* casos de uso,
* trazabilidad RF → CU → RN,
* validación de referencias,
* generación automática Markdown,
* generación del índice,
* validación automática de cobertura.

---

## Fase 2 - Reglas de negocio y casos de uso detallados

Próximos objetivos:

* mejorar reglas de negocio,
* profundizar flujos alternativos,
* definir excepciones,
* definir condiciones especiales,
* mejorar precondiciones y postcondiciones,
* documentar relaciones entre procesos,
* preparar documentación para arquitectura.

---

## Fase 3 - Arquitectura

Pendiente.

---

## Fase 4 - Modelo de datos

Pendiente.

---

## Fase 5 - Selección y adquisición del dataset

Pendiente.

---

## Fase 6 - Ingeniería de datos / ETL

Pendiente.

---

## Fase 7 - Análisis exploratorio de datos

Pendiente.

---

## Fase 8 - Feature Engineering

Pendiente.

---

## Fase 9 - Machine Learning

Pendiente.

---

## Fase 10 - Evaluación y Backtesting

Pendiente.

---

## Fase 11 - Valoración financiera

Pendiente.

---

## Fase 12 - Simulación Monte Carlo

Pendiente.

---

## Fase 13 - API con FastAPI

Pendiente.

---

## Fase 14 - Docker, pruebas y observabilidad

Pendiente.

---

## Fase 15 - Documentación final y publicación

Pendiente.

---

# Estado actual

```text
FASE 1 COMPLETADA
↓
FASE 2 LISTA PARA INICIAR
```

El siguiente objetivo es profundizar las reglas de negocio y los casos
de uso antes de comenzar el diseño de arquitectura.

````

Después de guardar el `README.md`, ejecuta otra vez:

```bash
python -m scripts.validate_documentation_coverage
````


