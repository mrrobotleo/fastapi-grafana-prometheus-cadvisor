FROM python:3.12.0a4-slim 

RUN groupadd -g 999 python && \
    useradd -r -u 999 -g python python

RUN mkdir /usr/app && chown python:python /usr/app
WORKDIR /usr/app

COPY --chown=python:python ./requirements.txt /usr/app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /usr/app/requirements.txt
COPY --chown=python:python ./main.py /usr/app/main.py
USER 999

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]

