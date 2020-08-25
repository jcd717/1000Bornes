# image tag: mille-bornes:python3.8-alpine
# donc:
# docker build -t mille-bornes:python3.8-alpine .

FROM python:3.8-alpine

EXPOSE 5000
ENV FLASK_APP=milleBornes


WORKDIR /app

# la variable d'environnemt SECRET_KEY injecté de manière "sécurisé" (jusqu'à preuve du contraire)
# si l'image est sur Docker Hub, tout le monde voit la clef dans l'image
# Donc pour une prod, il faut toujours contruire soit même cette image
RUN \
echo "#!/bin/sh" > run.sh && \
echo export SECRET_KEY=$(python -c "import string,random; print(''.join(random.choice(string.ascii_letters+string.digits+'-_:./+%£') for i in range(32)))") >>run.sh && \
echo "exec flask run -h 0.0.0.0" >>run.sh && \
chmod +x run.sh

CMD ["/app/run.sh"]

# le moteur flask
COPY setup.py /app
RUN pip install .

# le code source
COPY . /app

