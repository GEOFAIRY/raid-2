Project migrated to https://github.com/GEOFAIRY/d2raidfinder

raid-2

running the finder:
    npm install
    npm run dev

running the api:
    pipenv install
    pipenv shell
    python run.py


creating the DB:
    pipenv install
    pipenv shell
    python
    >>from app import db
    >>db.create_all()
