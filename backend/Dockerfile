FROM python:3.12.3
EXPOSE 8000
WORKDIR /app
COPY requirements.txt /app
RUN pip install -r requirements.txt --no-cache-dir
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
