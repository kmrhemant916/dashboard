FROM python:3.9.16-alpine3.17
EXPOSE 5000
WORKDIR /opt
COPY ./requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt
COPY . .
CMD ["flask", "run", "--host", "0.0.0.0", "--debugger", "--reload"]