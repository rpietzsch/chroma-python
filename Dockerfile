FROM python:3-alpine

WORKDIR /python-docker
COPY . .
RUN pip3 install -r requirements.txt
RUN pip3 install -e .

EXPOSE 5000

ENV FLASK_APP chroma
ENV FLASK_ENV development

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]