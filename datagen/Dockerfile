FROM python:3.9

RUN pip install --no-cache-dir mysql-connector-python pravega yfinance

COPY datagen.py tail.py ./

CMD [ "python", "-u", "./datagen.py" ]
