# Projeto Django com Login e Registro

Este projeto Django implementa um sistema de login e registro de usuários, utilizando SQLite como banco de dados.

## Funcionalidades

- **Tela de Login:**
  - Validação de e-mail e senha.
  - Tratamento de erros para e-mail/senha inválidos ou inexistentes.
  - Redirecionamento para a tela de registro.
  - Redirecionamento para a tela "Menu" após login bem-sucedido.
- **Tela de Registro:**
  - Formulário com campos de nome, e-mail, senha e confirmação de senha.
  - Validação de campos:
    - Nome: Apenas letras.
    - E-mail: Formato válido.
    - Senha: Mínimo de 8 caracteres, 1 caractere especial, 1 número e 1 letra maiúscula.
    - Confirmação de senha: Deve ser idêntica à senha.
  - Opção de visualizar/ocultar caracteres da senha.
  - Botões de "Registrar" e "Cancelar".

## Pré-requisitos

- Python 3.x
- pip (gerenciador de pacotes do Python)

## Instalação

1.  **Clone o repositório:**

    ```bash
    git clone [https://github.com/jooao7/desafio-login.git](https://github.com/jooao7/desafio-login.git)
    cd [desafio-login]
    ```

2.  **Crie um ambiente virtual (recomendado):**

    ```bash
    python -m venv venv
    ```

    - No Windows:

      ```bash
      venv\Scripts\activate
      ```

    - No macOS/Linux:

      ```bash
      source venv/bin/activate
      ```

3.  **Instale as dependências:**

    ```bash
    pip install django
    ```

4.  **Realize as migrações:**

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5.  **Crie um superusuário (opcional, para acessar o painel de administração):**

    ```bash
    python manage.py createsuperuser
    ```

6.  **Inicie o servidor de desenvolvimento:**

    ```bash
    python manage.py runserver
    ```

7.  **Acesse o projeto no seu navegador:**

    - Abra `http://127.0.0.1:8000/`

## Considerações

- Utilizei SQLite pela simplicidade. Em produção, considerarei usar um banco de dados mais robusto como PostgreSQL ou MySQL.
- A tela "Menu" está "vazia" apenas com uma mensagem de boas vindas.
- Para segurança em produção, utilize HTTPS e configure corretamente as definições de segurança do Django.
