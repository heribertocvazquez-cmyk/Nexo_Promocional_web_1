# Agent notes

## What this project is
Single-file Streamlit app (`app.py`) that renders one large static marketing page
(Nexo Promocional) through `streamlit.components.v1.html`. There is no backend API,
no database and no external service: all content and images come from `assets/`
(embedded as base64 at render time). Only third-party dependency is `streamlit`
(`requirements.txt`).

No environment variables or credentials are required.

## Running it (Base44 sandbox)
```
docker compose -f docker-compose.base44.yml up -d
```
- `web` service builds `.base44/Dockerfile` (Python 3.11 + `pip install -r requirements.txt`),
  bind-mounts the repo at `/app` and runs Streamlit's dev server on container port 8501,
  published on host port 3000 (the preview entry point).
- Streamlit reruns `app.py` from the mounted source on save (`--server.runOnSave`, with
  `--server.fileWatcherType=poll` so bind-mount change events are reliable). Edits show up
  without a rebuild; the image only needs rebuilding if `requirements.txt` changes.

## Sandbox-specific overrides (and why)
- `--server.enableCORS=false` / `--server.enableXsrfProtection=false`: the page is served
  through the preview proxy, so the browser `Origin` never matches the container host and
  Streamlit would refuse the websocket connection. These match the flags the repo's own
  `.devcontainer` uses. Dev-preview only — do not carry them into a production deployment.
- `BASE44_PREVIEW_MODE` is passed through to the container but the app does not read it.

## Verifying it works
- Health: `curl -s http://localhost:3000/_stcore/health` → `ok`
- Page: `curl -s -o /dev/null -w '%{http_code}' http://localhost:3000/` → `200`
- A plain `curl` only returns Streamlit's shell HTML ("Skip to main content"); the actual
  content is rendered inside the Streamlit iframe over the websocket, so confirm the page
  in the browser (the hero should read "Tu proyecto. Muchas ideas. Un solo Nexo.").

## Notes
- `st.components.v1.html` logs a deprecation notice ("replace with `st.iframe`"); it is
  harmless on the current Streamlit version and not needed for the app to run.
- `CORREO` / `WHATSAPP` at the top of `app.py` are blank by design; with them blank the
  contact form falls back to downloading a text file instead of emailing/WhatsApp.
