FROM python:3.12
EXPOSE 8000
WORKDIR /app
COPY requirements.txt /app
RUN pip install -r requirements.txt --no-cache-dir
RUN pip install git+https://github.com/QueraTeam/django-nextjs.git@stream-nextjs-response
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
