FROM python:3.10

COPY requirements.txt .


RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE $PORT

CMD gunicorn --workers=1 --bind 0.0.0.0:$PORT app:app

