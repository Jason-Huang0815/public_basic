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

## 4. Pipeline
**阶段一：地基（1-2 周）—— 让项目"像个项目"**

- 目标：把你的烂脚本改造成标准项目结构。

- 目录结构：src/包名/ 布局，拆 core/、services/、models/、config.py

- 依赖管理：装 uv（比 poetry 快，别纠结），建 pyproject.toml，虚拟环境跑起来

- 格式化 + Lint：ruff（格式+lint 一把梭）+ black，配 pre-commit hook

- Git 规范：分支策略、commit message 别写"改了点东西"

验收标准：你那个旧脚本，现在能 uv sync 装依赖、ruff check 零报错、目录结构能让别人一眼看懂哪个文件干啥。

---
**阶段二：保命层（2-3 周）—— 让代码"改不坏"**

- 目标：敢改代码，因为知道改了不会炸。

- 类型注解：全项目标 typing，mypy 或 pyright 跑通

- 异常处理：干掉所有裸 except，精确捕获

- 日志：logging 替换所有 print，分级别

- pytest 入门：先测 core/ 里的纯函数，fixture 管测试数据

验收标准：随便改一个 core/ 函数，mypy 能告诉你哪里调用方要跟着改，pytest 能告诉你逻辑有没有改坏。

---
**阶段三：隔离层（1-2 周）—— 测试不碰真实世界**

- 目标：测试跑得快、不依赖网络和数据库。

- mock：unittest.mock / monkeypatch，记住 patch 路径是"被使用的地方"

- 专用库：responses/respx 管 HTTP，freezegun 管时间

- 边界意识：只 mock 外部边界（网络/DB/时间/文件），自己的逻辑真跑

验收标准：你的测试套件断网也能全绿，跑完不超过 30 秒。

---
**阶段四：环境层（1-2 周）—— 在哪跑都一样**

- 目标：环境一致性，部署不靠嘴。

- Dockerfile：python:3.12-slim 起步，多阶段构建，.dockerignore，非 root 用户

- docker-compose：服务 + PostgreSQL + Redis 一键起

- testcontainers：集成测试临时起真容器，测完销毁

验收标准：同事 clone 你仓库，docker compose up 一条命令跑起来，不用问你任何环境问题。

---
**阶段五：自动化层（1 周）—— 门禁卡死**

- 目标：烂代码进不了主分支。

- CI：GitHub Actions / GitLab CI，push 触发 → ruff → mypy → pytest → 全绿才允许合并

- pre-commit：提交前本地先跑一遍，别等 CI 红了再改

验收标准：你故意提交一个类型错误，CI 直接拦住，合并不了。

---
**阶段六：方向分化（长期）—— 选一条扎进去**

前面五个阶段是所有 Python 工程师的公共底子，走完你已经是"能交付"的人了。然后选方向：

- 后端：FastAPI/Django → Pydantic 校验 → SQLAlchemy → 认证授权 → 部署

- 数据/爬虫：asyncio 并发 → pandas → 数据管道 → 调度

- 工具/CLI：click/typer → 打包发布到 PyPI

