# 🌵 Raízes do Nordeste API

API desenvolvida para gerenciamento de pedidos, estoque e fidelidade da rede fictícia **Raízes do Nordeste**.

---

## 🚀 Tecnologias

* Python 3.10+
* FastAPI
* SQLite (dev)
* SQLAlchemy
* JWT Authentication

---

## ⚙️ Requisitos

* Python instalado
* Git
* Virtualenv (opcional)

---

## 🔧 Instalação

```bash
git clone https://github.com/seu-usuario/seu-repo.git
cd raizes_do_nordeste
python -m venv .venv
.venv\Scripts\activate  # Windows
pip install -r requirements.txt
```

---

## 🗄 Banco de Dados

O projeto utiliza SQLite automaticamente:

```bash
raizes.db
```

---

## ▶️ Executar API

```bash
uvicorn app.main:app --reload
```

---

## 📚 Documentação (Swagger)

Acesse:

```
http://127.0.0.1:8000/docs
```

---

## 🔐 Autenticação

* Endpoint: `/auth/login`
* Retorna token JWT

Utilizar no header:

```
Authorization: Bearer {token}
```

---

## 🔁 Fluxo implementado (MVP)

✔ Cadastro de produto
✔ Controle de estoque
✔ Autenticação JWT

---

## 🧪 Testes

Utilizar coleção Postman disponível no repositório.

---

## 📌 Observações

* Banco SQLite usado para desenvolvimento
* Estrutura preparada para PostgreSQL
