FROM python:3

WORKDIR /usr/src/app

COPY . .

RUN pip install -r project/requirements.txt && pip install --upgrade pip && python -m pip install argon2-cffi

#EXPOSE 8001

#ENTRYPOINT ["/usr/src/app/"]

#CMD ["gunicorn", "-c", "project/conf.py", "project.wsgi"]
