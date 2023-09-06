# Bawk

- Após ser modificado a modelagem dos dados, deve-se utilizar o comando:

```bash
    alembic revision --autogenerate -m "nome-da-migration"
    alembic upgrade head
```
