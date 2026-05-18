# AI Agents Portfolio

Coleccion de agentes AI pensados como proyectos de referencia para entrevistas tecnicas.

El repo muestra una arquitectura simple pero profesional:

- agentes desacoplados por caso de uso
- proveedor LLM intercambiable
- API con FastAPI
- CLI para demos rapidas
- modo `mock` para probar sin consumir API
- pruebas unitarias basicas

## Agentes incluidos

### 1. Interview Coach Agent

Recibe perfil del candidato, descripcion del puesto y objetivos.

Devuelve:

- pitch personalizado
- riesgos o gaps frente a la vacante
- preguntas probables
- historias tipo STAR para entrevista

### 2. Research Brief Agent

Convierte notas largas o desordenadas en un brief ejecutivo.

Devuelve:

- resumen ejecutivo
- hallazgos clave
- riesgos
- recomendaciones
- siguientes pasos

### 3. CSV Insight Agent

Analiza metadata y muestras de un dataset tabular.

Devuelve:

- chequeos de calidad de datos
- hipotesis de negocio
- features utiles
- visualizaciones sugeridas
- plan de analisis

## Stack

- Python 3.10+
- FastAPI
- Pydantic
- OpenAI SDK opcional
- Pytest

## Estructura

```text
ai-agents-portfolio/
  src/ai_agents_portfolio/
    agents/
    app.py
    cli.py
    config.py
    llm.py
    registry.py
    schemas.py
  examples/
  tests/
  .env.example
  pyproject.toml
```

## Instalacion

```bash
cd ai-agents-portfolio
python -m venv .venv
.venv\Scripts\activate
pip install -e .[dev]
```

## Variables de entorno

```bash
copy .env.example .env
```

Si defines `OPENAI_API_KEY`, la app usa OpenAI.

Si no defines clave, la app funciona en modo `mock`, ideal para demos locales y pruebas.

## Ejecutar API

```bash
uvicorn ai_agents_portfolio.app:app --reload --port 8010
```

Endpoints principales:

- `GET /health`
- `GET /agents`
- `POST /agents/interview-coach/run`
- `POST /agents/research-brief/run`
- `POST /agents/csv-insight/run`

## Ejecutar CLI

```bash
python -m ai_agents_portfolio.cli list
python -m ai_agents_portfolio.cli run interview-coach --input examples/interview_input.json
python -m ai_agents_portfolio.cli run research-brief --input examples/research_input.json
python -m ai_agents_portfolio.cli run csv-insight --input examples/csv_input.json
```

## Ejemplo de request

```bash
curl -X POST http://localhost:8010/agents/interview-coach/run ^
  -H "Content-Type: application/json" ^
  -d "{\"candidate_profile\":\"3 years building ML dashboards and FastAPI services\",\"job_description\":\"Looking for an applied AI engineer who can ship customer-facing copilots\",\"goals\":[\"tailor my pitch\",\"anticipate technical questions\"]}"
```

## Como venderlo en entrevistas

Puedes presentarlo como:

`Built a small agent platform with reusable prompts, pluggable LLM providers, CLI/API access, and deterministic mock mode for local testing.`

Puntos fuertes para mencionar:

- separacion entre logica de negocio y proveedor LLM
- salidas estructuradas para integracion
- modo mock para desarrollo reproducible
- capacidad de convertirlo en sistema multi-agent mas adelante

## Siguiente paso recomendado

1. Subir este repo como uno independiente en GitHub.
2. Agregar screenshots o un GIF de la API/CLI funcionando.
3. Grabar un video corto de 60 a 90 segundos explicando arquitectura y decisiones.
