from confluent_kafka import Consumer, KafkaError

consumer = Consumer({
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'mi-grupo',
    'auto.offset.reset': 'earliest'
})

consumer.subscribe(['mi-tema'])

while True:
    msg = consumer.poll(1.0)

    if msg is None:
        continue
    if msg.error():
        if msg.error().code() == KafkaError._PARTITION_EOF:
            print('Final de partición alcanzado')
        else:
            print('Error en el mensaje: %s' % msg.error())
    else:
        print('Mensaje recibido: %s' % (msg.value()))

consumer.close()
