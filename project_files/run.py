import os
from app import app

# Setze das Arbeitsverzeichnis auf den Ordner, in dem sich das Skript befindet
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Für betrieb in docker-compose: setze die Umgebungsvariable für Postgres
DATABASE_URL = os.getenv("DATABASE_URL")

# Arbeitsverzeichnis ausgeben
print(f"Document Root: {os.getcwd()}")

print('run.py')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=app.config['PORT'], debug=True)
