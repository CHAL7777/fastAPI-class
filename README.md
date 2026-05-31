# FastAPI Learning Notes

This repo is my personal sandbox for learning FastAPI. It starts small and grows as I practice core ideas like routing, request/response models, and dependency injection.

## Goals

- Build small, focused examples
- Learn FastAPI fundamentals step by step
- Keep notes and commands in one place

## Quick Start

1. Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requerements-dev.txt
```

3. Run the app:

```bash
uvicorn main:app --reload
```

4. Open the docs in a browser:

- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

## Project Structure

```
main.py
README.md
requerements-dev.txt
```

## Notes

- Use `--reload` during development so the server restarts on file changes.
- If `uvicorn` is not found, install it with `pip install "uvicorn[standard]"`.

## Next Ideas

- Add a `GET /health` route
- Create a `POST` endpoint with a Pydantic model
- Add basic tests with `pytest`
