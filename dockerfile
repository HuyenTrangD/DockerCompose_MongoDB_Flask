# image source
FROM python

# récupération des dépendances de mon projet
COPY requirements.txt requirements.txt

# installer mes dépendances
RUN pip install -r requirements.txt

# ajout de mon app Flask
COPY app.py app.py

# ouvrir le port
EXPOSE 9001

# démarrer mon app
CMD [ "python", "app.py" ]

