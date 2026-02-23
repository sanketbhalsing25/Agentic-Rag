**Agentic RAG — Compliance Assistant**

A small Retrieval-Augmented Generation (RAG) project that builds a retriever from local documents and exposes an interactive CLI and a FastAPI-based HTTP endpoint with a simple UI.

**Features**
- **Interactive CLI:** Ask compliance questions directly via `app/main.py`.
- **API + UI:** FastAPI endpoint and static UI served from `ui/index.html`.
- **Document ingestion:** loaders, splitters and a vectorstore under `app/ingestion`.

**Requirements**
- **Python:** 3.10+ recommended
- **Dependencies:** install with `pip install -r requirements.txt`

**Quick Install**
Run in your project root:

```bash
python -m pip install -r requirements.txt
```

**Run (CLI)**
Interact with the graph directly:

```bash
python app/main.py
```

This will initialize the document pipeline (it expects example data at `data/BFSI_Compliance_Manual.pdf`) and prompt for a question.

**Run (API + UI)**
Start the FastAPI server and open the UI in your browser:

```bash
uvicorn app.api:api --reload --host 0.0.0.0 --port 8000
```

Then open http://127.0.0.1:8000/ to use the shipped UI.

**Project Structure**
- **app/**: core application code
  - [app/main.py](app/main.py) : initializes the workflow and offers a CLI entrypoint
  - [app/api.py](app/api.py) : FastAPI endpoints and static UI mounting
  - [app/config.py](app/config.py) : configuration (if present)
  - `app/graph/` : workflow and graph-related logic
  - `app/ingestion/` : `loader.py`, `splitter.py`, `vectorstore.py` for document processing
  - `app/utils/` : helper utilities and prompts
- **data/**: local documents (add PDFs or other sources here)
- **ui/**: static web UI (`ui/index.html`)
- **requirements.txt**: Python dependencies

**Data**
- Place source documents (PDFs, text) in the `data/` directory. `app/main.py` references `data/BFSI_Compliance_Manual.pdf` as an example.

**Contributing**
- Open issues and PRs. Add tests and documentation for new features.

**License**
- No license specified. Add a `LICENSE` file to set project licensing.

If you want, I can also:
- Add a minimal `README` badge, demo GIF, or sample data.
- Add a `Makefile` or `scripts/` helpers to simplify running commands.
