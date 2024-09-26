FROM python:3.11

RUN adduser hello
USER hello

COPY . /home/hello
WORKDIR /home/hello

RUN export FLASK_APP=hello.py
RUN python -m venv venvdock
RUN pip install -r requirements.txt


EXPOSE 5002
ENTRYPOINT [ "python" ]
CMD ["hello.py"]


