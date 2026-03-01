# 📊 Excel AI Analyzer

API REST que permite analizar archivos Excel usando inteligencia artificial con **Cohere** como LLM. Cuenta con un frontend estático integrado para interactuar con el servicio desde el navegador.

---

## 🚀 Tecnologías

- **Python 3.13** + **FastAPI**
- **Cohere** (LLM)
- **HTML/CSS/JS** (Frontend estático)

---

## 📁 Estructura del proyecto

```
.
├── app/
│   ├── api/              # Endpoints de la API
│   ├── core/             # Configuración global
│   ├── schemas/          # Modelos Pydantic
│   ├── services/         # Lógica del LLM (Cohere)
│   └── main.py           # Entrada de la aplicación
├── frontend/
│   ├── static/           # CSS y JS
│   └── templates/        # HTML
└── requirements.txt
```

---

## ⚙️ Instalación y uso

### 1. Clonar el repositorio

```bash
git clone https://github.com/tu-usuario/tu-repo.git
cd tu-repo
```

### 2. Crear entorno virtual e instalar dependencias

```bash
python -m venv venv
source venv/bin/activate        # Linux/Mac
venv\Scripts\activate           # Windows

pip install -r requierements.txt
```

### 3. Configurar variables de entorno

Crea un archivo `.env` en la raíz del proyecto:

```env
COHERE_API_KEY=tu_api_key_aqui
```

> Puedes obtener tu API Key en [https://dashboard.cohere.com](https://dashboard.cohere.com)

### 4. Levantar el servidor

```bash
uvicorn app.main:app --reload
```

La API estará disponible en `http://localhost:8000` y el frontend en la misma URL.

---

## 📡 Endpoints de la API

### `GET /health`
Verifica que el servidor esté corriendo correctamente.

**Response:**
```json
{
  "status": "ok"
}
```

---

### `POST /api/analyze`
Analiza contenido de texto o datos con IA.

**Body:**
```json
{
  "content": "texto o datos a analizar"
}
```

**Response:**
```json
{
  "result": "análisis generado por el LLM"
}
```

---

### `POST /api/analyze-excel`
Recibe un archivo Excel y retorna un análisis generado por Cohere.

**Form-data:**
| Campo  | Tipo   | Descripción              |
|--------|--------|--------------------------|
| `file` | `file` | Archivo `.xlsx` o `.xls` |

**Response:**
```json
{
  "filename": "datos.xlsx",
  "analysis": "resumen e insights generados por IA"
}
```

---

## 📝 Notas
- El servidor utiliza Python 3.13. Versiones anteriores pueden causar incompatibilidades.
