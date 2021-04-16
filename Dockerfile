FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt


COPY . .
RUN pip install -e .


EXPOSE 8000
CMD ["gunicorn", "wsgi:app", "--bind", "0.0.0.0:8000"]