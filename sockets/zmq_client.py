import zmq
host = '127.0.0.1'
port = 6789
context = zmq.Context()
client = context.socket(zmq.REQ)
client.connect(("tcp://{}:{}".format(host,port)))
for num in range(5):
    requests_str = "message {}".format(num)
    requests_bytes = requests_str.encode('utf-8')
    client.send(requests_bytes)
    reply_bytes = client.recv()
    reply_str = reply_bytes.decode('utf-8')
    print('Sent {}, received {}'.format(requests_str, reply_str))