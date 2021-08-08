# Kafka_Data_Streaming

# Step 1: Starting zookeeper

neo@neo:~/Downloads/kafka_2.12-2.8.0$ bin/zookeeper-server-start.sh config/zookeeper.properties

# Step 2: Starting kafka

neo@neo:~/Downloads/kafka_2.12-2.8.0$ bin/kafka-server-start.sh config/server.properties

# Step 3: Start Hadoop

start-all.sh

# Step 3: Start flume

$bin/flume-ng agent --conf ./conf/ -f conf/kafkaSourse.conf -n flume1 Dflume.root.logger=TRACE,console

# Step 4: run producer.py

# Step 5: run consumer.py
