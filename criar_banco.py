from sitees import database, app

from sitees.models import Usuario,Fotos

with app.app_context():
    database.create_all()