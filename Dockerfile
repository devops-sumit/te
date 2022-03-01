FROM python:3.9

WORKDIR /app

COPY ./ requirements.txt ./

RUN apt-get update
RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT ["python"]
CMD ["main.py"]
