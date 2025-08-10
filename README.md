# MVP1 · Coach IA para Pilotos (Streamlit)

Despliegue con **Streamlit Community Cloud** en minutos.

## Archivos
- `streamlit_app.py` → App principal
- `requirements.txt` → Dependencias
- `.streamlit/secrets.toml.example` → Ejemplo de configuración de Secrets

## Despliegue (vía GitHub)
1. Crea un repositorio en GitHub (por ej. `mvp1-pilotos-streamlit`) y sube estos archivos.
2. Ve a https://share.streamlit.io/ → **New app** → conecta tu GitHub y selecciona el repo y el archivo `streamlit_app.py`.
3. En la app de Streamlit, abre **Settings → Secrets** y pega:

```
OPENAI_API_KEY = "sk-..."
OPENAI_MODEL = "ft:gpt-4o-mini-2024-07-18:alphapio::By30iumK"
```

4. Deploy. Obtendrás una **URL pública** para compartir.

## Ejecución local (opcional)
```bash
pip install -r requirements.txt
# En Windows PowerShell:
$env:OPENAI_API_KEY="sk-..." ; $env:OPENAI_MODEL="ft:gpt-4o-mini-2024-07-18:alphapio::By30iumK"
streamlit run streamlit_app.py
```
