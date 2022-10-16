FROM python:3.8.5

RUN mkdir /app
WORKDIR /app

COPY app.py /app
COPY requirements.txt /app
RUN pip install -r requirements.txt

EXPOSE 5000
ENTRYPOINT [ "flask" ]
CMD ["run", "--host=0.0.0.0", "--port=5000"]

