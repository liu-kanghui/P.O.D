import io
import select
import socket
import sys
import struct
from PIL import Image
from datetime import datetime


# Start a socket listening for connections on 0.0.0.0:8000 (0.0.0.0 means
# all interfaces)
server_socket = socket.socket()
server_socket.bind(('0.0.0.0', 8000))
server_socket.listen(0)

inputs = [server_socket]

# Accept a single connection and make a file-like object out of it
# connection = server_socket.accept()[0].makefile('rb')

# Server setup to allow client PODs to connect
# socket_dic = {}
# socket_dic[server_socket]

try:

    while True:

        readable, writeable, exceptions = select.select(inputs, [], [])

        for s in readable:

            if s is server_socket:

                connection = server_socket.accept()[0].makefile('rb')
                # connection.setblocking(0)
                # inputs.append(connection)

        # Read the length of the image as a 32-bit unsigned int. If the
        # length is zero, quit the loop
        # image_len = struct.unpack('<L',
        #                           connection.read(struct.calcsize('<L')))[0]
        # if not image_len:
        #     break

        # Construct a stream to hold the image data and read the image
        # data from the connection
        image_stream = io.BytesIO()
        image_stream.write(connection.read(image_len))

        # Rewind the stream, open it as an image with PIL and do some
        # processing on it
        image_stream.seek(0)
        image = Image.open(image_stream)
        pod_src = connection.getpeername())
        name = '%s-%s.jpg' % pod_src, (str(datetime.now()))

        # outfile = '%s/%s.jpg' % (self.tgtdir,
        # self.basename + str(datetime.now()))
        image.save('/home/pi/NewPod/photo/' + name, 'JPEG')
        # print('Image is %dx%d' % image.size)
        image.verify()
        print('Image is verified')

        connection.close()

finally:
    # connection.close()
    server_socket.close()
