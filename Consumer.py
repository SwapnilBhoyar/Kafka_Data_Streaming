"""
@Author: Swapnil Bhoyar
@Date: 2021-08-09
@Last Modified by: Swapnil Bhoyar
@Last Modified time: 2021-08-09
@Title : Fetching real time stock data using kafka.
"""
from kafka import KafkaConsumer
import json
import pydoop.hdfs as hdfs

consumer = KafkaConsumer('stock1')
hdfs_path='hdfs://localhost:9000//liveStockData/myData.txt'
for message in consumer:
    values=message.value
    with hdfs.open(hdfs_path,'a') as f:
        f.write(values)