# Calculadora Avançada

Uma calculadora web desenvolvida com Django, com funcionalidades como operações básicas (adição, subtração, multiplicação, divisão), cálculo de porcentagem, histórico de operações e suporte a teclas de atalho. O projeto é responsivo e pode ser usado em desktops, tablets e smartphones.

## Pré-requisitos

Antes de iniciar, certifique-se de ter os seguintes itens instalados:
- [Python 3.8+](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/installation/)
- [Git](https://git-scm.com/downloads/) (opcional, para clonar o repositório)

## Instalação

Siga os passos abaixo para configurar e executar a calculadora localmente:

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seu-usuario/calculadora-django.git
   cd calculadora-django

2. **Crie um ambiente virtual:**
   ```bash
   python -m venv venv

3. **Ative o ambiente virtual:**
   * No Windows:
   ```bash
    venv\Scripts\activate
   
  * No macOS/Linux:
    ```bash
     source venv/bin/activate
    

4. **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    
5. **Configure o projeto:**
   *Atualize a chave secreta (```SECRET_KEY```) em ```settings.py``` com uma nova chave gerada (use ```python -c "import secrets; print(secrets.token_urlsafe(50))"``` para gerar uma).
   *Certifique-se de que o banco de dados SQLite está configurado (padrão em ```settings.py```).

6. **Aplique as migrações:**
    ```bash
    python manage.py migrate
7. **Crie um superusuário (opcional, para acessar o admin):
   ```bash
   python manage.py createsuperuser

8. **Inicie o servidor:**
   ```bash
   python manage.py runserver

9 **Acesse a aplicação:**
--
*Abra o navegador e vá para ```http://127.0.0.1:8000/login/```.
*Faça login com as credenciais criadas pelo comando ```createsuperuser```.



