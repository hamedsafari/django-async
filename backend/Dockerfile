FROM python:3.12
WORKDIR /app
COPY requirements.txt /app
RUN pip install -r requirements.txt --no-cache-dir
# RUN pip install git+https://github.com/QueraTeam/django-nextjs.git@main
RUN pip install git+https://github.com/QueraTeam/django-nextjs.git@stream-nextjs-response
EXPOSE 8000
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
