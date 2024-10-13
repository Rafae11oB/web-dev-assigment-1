FROM python:3.9-slim

WORKDIR /myproject

COPY requirements.txt /myproject/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /myproject/

RUN mkdir -p /myproject/static

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
