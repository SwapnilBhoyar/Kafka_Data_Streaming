from kafka import KafkaProducer
import json
import requests
from os import environ as env
from dotenv import load_dotenv
import pydoop.hdfs as hdfs

load_dotenv()
key = env['KEY']

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],api_version=(0,10,1),value_serializer=lambda v: json.dumps(v).encode('utf-8'))

url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=key'
r = requests.get(url)
data = r.json()

producer.send('stock1', data)