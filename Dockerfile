FROM python:3

WORKDIR /usr/src/app

COPY . .

RUN pip install -r project/requirements.txt

EXPOSE 8000

#ENTRYPOINT ["/usr/src/app/"]

#CMD ["gunicorn", "-c", "project/conf.py", "project.wsgi"]
