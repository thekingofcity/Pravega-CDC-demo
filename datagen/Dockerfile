FROM python:3.9

RUN pip install --no-cache-dir mysql-connector-python pravega===0.2.0 yfinance

CMD [ "python", "-u", "./datagen.py" ]
