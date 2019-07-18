FROM python:latest

ADD my_script.py /

RUN pip install requests
ENTRYPOINT ["python", "./my_script.py"]