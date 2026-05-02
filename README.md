 # 🌽 Raízes do Nordeste API

API desenvolvida para o sistema da rede **Raízes do Nordeste**, uma franquia de lanchonetes especializadas em culinária nordestina, com foco em escalabilidade, organização e integração entre múltiplos canais de atendimento.

---

## 📌 Descrição

Este projeto tem como objetivo fornecer uma API REST para gerenciamento de:

* 📦 Produtos
* 🧾 Pedidos
* 🏪 Unidades
* 👤 Clientes
* 💳 Pagamentos (simulados)
* 🎯 Programa de fidelidade

A API foi construída considerando um cenário real de crescimento de uma franquia, com múltiplas unidades e necessidade de padronização, desempenho e rastreabilidade.

---

## 🚀 Tecnologias Utilizadas

* Python 3.x
* FastAPI
* Uvicorn
* Pydantic
* (ou outro banco configurado)
* Git & GitHub

---

## ⚙️ Instalação e Configuração

### 🔧 1. Clonar o repositório

```bash
git clone https://github.com/tamileoliveira/raizes_do_nordeste.git
cd raizes_do_nordeste
```

---

### 🐍 2. Criar e ativar ambiente virtual

```bash
python -m venv .venv
```

#### Windows:

```bash
.venv\Scripts\activate
```

#### Linux/Mac:

```bash
source .venv/bin/activate
```

---

### 📦 3. Instalar dependências

```bash
pip install -r requirements.txt
```

---

## 🔐 Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto baseado no exemplo:

### 📄 `.env.example`

```env
DATABASE_URL=sqlite:///./database.db
SECRET_KEY=sua_chave_secreta
```

---

## 🗄️ Banco de Dados

Caso utilize SQLite, o banco será criado automaticamente ao iniciar a aplicação.

Se estiver usando outro banco (PostgreSQL, MySQL), configure a variável `DATABASE_URL` corretamente.

---

## ▶️ Executando a API

```bash
uvicorn app.main:app --reload
```

A API estará disponível em:

```
http://127.0.0.1:8000
```

---

## 📄 Documentação da API (Swagger)

Acesse a documentação interativa em:

```
http://127.0.0.1:8000/docs
```

Ou alternativa:

```
http://127.0.0.1:8000/redoc
```

---

## 📌 Funcionalidades Principais

### 🛒 Pedidos

* Criar pedido
* Atualizar status
* Acompanhar andamento

### 📦 Produtos

* Listar produtos
* Filtrar por unidade
* Cadastro e atualização

### 👤 Clientes

* Cadastro de cliente
* Consentimento de dados (LGPD)

### 💳 Pagamentos (Simulado)

* Solicitação de pagamento
* Retorno de status:

  * aprovado
  * recusado

### 🎯 Fidelidade

* Acúmulo de pontos
* Aplicação de descontos

---

## 🔐 LGPD e Segurança

Este projeto considera boas práticas de proteção de dados:

* Consentimento explícito do usuário
* Minimização de dados sensíveis
* Estrutura preparada para anonimização
* Controle de acesso e rastreabilidade

---

## 📈 Arquitetura do Projeto

O projeto segue uma arquitetura em camadas:

```
app/
 ├── main.py          # Inicialização da API
 ├── routes/          # Rotas (endpoints)
 ├── schemas/         # Validação de dados (Pydantic)
 ├── models/          # Modelos de dados
```

### 🔎 Padrões adotados:

* API REST
* Separação de responsabilidades
* Código modular e escalável

---

## 📊 Melhorias Futuras

* Integração com gateway de pagamento real
* Autenticação com JWT
* Deploy em nuvem (Render/Railway)
* Testes automatizados com Pytest
* Logs e auditoria completos

---

## 👨‍💻 Autor

Desenvolvido por **Tamile de Oliveira Mendes**
Projeto acadêmico – Curso de Análise e Desenvolvimento de Sistemas

---

## 📎 Observações

Este projeto foi desenvolvido com foco em simular um ambiente real de mercado, priorizando:

* Organização
* Clareza
* Escalabilidade
* Boas práticas de desenvolvimento

---

