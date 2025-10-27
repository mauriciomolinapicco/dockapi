# 🚀 fastapi-microservices-lab

Proyecto caso de estudio para construir una arquitectura moderna con **FastAPI**, **Redis**, **PostgreSQL** y **Docker**.  
La idea es aprender sobre microservicios, asincronismo, colas de trabajo y caching en un entorno realista pero simple.

---

## 🧩 Arquitectura

docker-compose.yml
├── api-service/ # FastAPI principal (CRUD, endpoints, etc.)
├── worker-service/ # Worker que procesa tareas async
├── redis/ # Cache y cola de tareas
└── postgres/ # Base de datos relacional

yaml
Copiar código

Servicios:
- **api-service:** expone endpoints REST para crear tareas y consultar resultados.
- **worker-service:** escucha jobs en Redis y los ejecuta (ej. simulaciones, cálculos, etc.).
- **redis:** almacén en memoria para cache y cola de mensajes.
- **postgres:** base de datos persistente.

---

## ⚙️ Requisitos

- Docker y Docker Compose instalados
- Python 3.10+ (solo si querés correr algo fuera del contenedor)

---

## 🧰 Setup y ejecución

Clonar el repo:
```bash
git clone git@github.com-personal:usuario/fastapi-microservices-lab.git
cd fastapi-microservices-lab
Levantar todos los servicios:

bash
Copiar código
docker compose up --build
El proyecto inicia:

API → http://localhost:8000/docs

Redis → localhost:6379

Postgres → localhost:5432

🧠 Puntos clave
Arquitectura de microservicios con FastAPI

Docker Compose multi-contenedor

Comunicación entre servicios vía Redis

Background tasks (Celery / RQ)

Cache de respuestas

Buenas prácticas con .env y variables de entorno

🧑‍💻 Autor
Proyecto de aprendizaje creado por mi, inspirado en la curiosidad por sistemas distribuidos y backend moderno.

