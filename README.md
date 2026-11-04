# Bublic_Basic Project

## A project for systematic python engineering learning
## All are needed for different directions

---
## 1. Requirements

- Python 3.14.5+
- uv

## 2. Getting Started

````bash
git clone https://github.com/Jason-Huang0815/public_basic.git
cd public_basic
````
````bash
uv sync
````
````bash
uv run python src/myproject/main.py
````
````bash
uv run pytest
````

## 3. Project Struture

````
myproject/
├── .venv/
├── docs/
├── src/
│   └── myproject/
│       ├── __init__.py
│       ├── main.py
│       ├── core/
│       │   ├── __init__.py
│       │   └── logic.py
│       └── utils/
│           ├── __init__.py
│           └── helpers.py
├── tests/
│   ├── __init__.py
│   └── test_logic.py
├── .gitignore
├── README.md
├── pyproject.toml
├── uv.lock
└── pre-commit-config.yaml
````