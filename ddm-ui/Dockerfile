# start by pulling the python image
FROM python:3.10

WORKDIR /app

COPY requirements.txt ./
RUN pip install -r requirements.txt --index-url=https://pypi.python.org/simple/

COPY . .

CMD ["python", "app.py"]
