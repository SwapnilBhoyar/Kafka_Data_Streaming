from kafka import KafkaConsumer
import json
import pydoop.hdfs as hdfs

consumer = KafkaConsumer('stock1')
hdfs_path='hdfs://localhost:9000//liveStockData/myData.txt'
for message in consumer:
    values=message.value
    with hdfs.open(hdfs_path,'a') as f:
        f.write(values)