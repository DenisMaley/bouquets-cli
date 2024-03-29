FROM python:3.7
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
COPY app.py .
ENTRYPOINT ["python", "app.py"]