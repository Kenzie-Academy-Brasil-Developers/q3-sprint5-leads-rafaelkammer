# Aplicação de gerenciamento de Leads

| Método     | Rota   |
| ---------- | ------ |
| **GET**    | /leads |
| **POST**   | /leads |
| **PATCH**  | /leads |
| **DELETE** | /leads |

---

# Passos para utilização

Instalação de dependências

```
pip install -r requirements.txt
```

Configurar variaveis de ambiente no .env conforme mostrado no .env.example

```
FLASK_ENV=development
DB_URI="postgresql://user:password@localhost:5432/database"
```

Executar a criação das tabelas com flask migrate

```
flask db init
flask db migrate -m "mensagem"
flask db upgrade
```

Verificar as rotas

```
flask routes
```

Rodar a aplicação

```
flask run
```

---

# /POST - Criar nova lead

Registra um novo Lead no banco de dados.

`EXEMPLO DE REQUISIÇÃO`

```json
{
  "name": "John Doe",
  "email": "john@email.com",
  "phone": "(41)90000-0000"
}
```

`EXEMPLO DE RESPOSTA - STATUS 201`

```json
{
  "name": "John Doe",
  "email": "john@email.com",
  "phone": "(41)90000-0000",
  "creation_date": "Fri, 10 Sep 2021 17:53:25 GMT",
  "last_visit": "Fri, 10 Sep 2021 17:53:25 GMT",
  "visits": 1
}
```

---

# /GET - Buscar todas as leads

Lista todos os LEADS por ordem de visitas, do maior para o menor.

`Get /leads - SEM CORPO DE REQUISIÇÃO`

`Get /leads - EXEMPLO DE RESPOSTA - STATUS 200`

```json
[
  {
    "name": "John Doe",
    "email": "john@email.com",
    "phone": "(41)90000-0000",
    "creation_date": "Fri, 10 Sep 2021 17:53:25 GMT",
    "last_visit": "Fri, 10 Sep 2021 17:53:25 GMT",
    "visits": 1
  },
  {
    "name": "John Doe1",
    "email": "john1@email.com",
    "phone": "(41)80000-0000",
    "creation_date": "Fri, 10 Sep 2021 17:53:25 GMT",
    "last_visit": "Fri, 10 Sep 2021 17:53:25 GMT",
    "visits": 1
  }
]
```

---

# /PATCH - Atualizar uma lead

A cada requisição aumenta em 1 o valor de visits e atualiza last_visit para o momento da requisição.

`Patch /leads - EXEMPLO DE REQUISIÇÃO`

```json
{
  "email": "john@email.com"
}
```

`Patch /leads - EXEMPLO DE RESPOSTA - STATUS 204`

`Sem corpo de resposta`

---

# /DELETE - Excluir uma lead

Exclui um Lead específico.

`Delete /leads - EXEMPLO DE REQUISIÇÃO`

```json
{
  "email": "john@email.com"
}
```

`Delete /leads - EXEMPLO DE RESPOSTA - STATUS 204`

`Sem corpo de resposta`
