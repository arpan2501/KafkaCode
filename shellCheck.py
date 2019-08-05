import os

res = os.popen('/Users/arpan/Documents/kafka_2.12-2.0.0/bin/kafka-consumer-groups.sh --bootstrap-server localhost:9092 --list').read()

t= res.split()
#t.pop()

print(t)
for g in t:
    res = os.popen('/Users/arpan/Documents/kafka_2.12-2.0.0/bin/kafka-consumer-groups.sh --bootstrap-server localhost:9092 --describe --group '+g).read()
    #print(res)
    f=res.split()

    print(f)