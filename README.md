# PokéColeção

Aplicação Django para organizar cartas Pokémon por raridade, tipo, estágio de evolução e valor estimado.

## Como executar

1. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

2. Execute as migrações:

   ```bash
   python manage.py migrate
   ```

3. Inicie o servidor:

   ```bash
   python manage.py runserver
   ```

4. Acesse:

   - Aplicação: http://127.0.0.1:8000/
   - Administração: http://127.0.0.1:8000/admin/

## Acesso administrativo

Use as credenciais abaixo para acessar o painel de administração:

```text
Usuário: admin
Senha: Pokemon123!
```

## Funcionalidades

- Listagem de raridades e quantidade de cartas.
- Listagem de cartas associadas a cada raridade.
- Busca de cartas pelo nome.
- Ordenação das cartas por valor estimado.
- Cadastro e edição pelo painel administrativo.
