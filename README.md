# Social-Media-API

Social Media API written on DRF

## Installing using GitHub

1. Install PostgresSQL and create a database.

   ```bash
   git clone https://github.com/Veinmax/Social-Media-API.git
   cd Social-Media-API
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
   Configure Environment Variables:
- Create a .env file in the project root.
- Make sure it includes all the variables listed in the .env.sample file.
- Ensure that the variable names and values match those in the sample file.
   ```bash
   set POSTGRES_HOST=<your db hostname>
   set POSTGRES_DB=<your db name>
   set POSTGRES_USER=<your db username>
   set POSTGRES_PASSWORD=<your db user password>
   set SECRET_KEY=<your secret key>
   python manage.py migrate
   ```
  
Run the Server:
```bash
python manage.py runserver
```

# Run with Docker
Docker should be installed
```bash
docker-compose up --build
```

# Getting access
- create user via /api/user/register/
- get access token via /api/user/login/
- to invalidate a token, you must log out via /api/user/logout/
- explore the API documentation at /api/doc/swagger/.