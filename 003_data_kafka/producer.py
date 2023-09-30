from confluent_kafka import Producer

producer = Producer({'bootstrap.servers': 'localhost:9092'})

def delivery_report(err, msg):
    if err is not None:
        print('Error: %s' % err)
    else:
        print('Mensaje entregado a %s [%d]' % (msg.topic(), msg.partition()))

for i in range(10):
    mensaje = f'Mensaje #{i}'
    producer.produce('mi-tema', key=str(i), value=mensaje, callback=delivery_report)

producer.flush()
