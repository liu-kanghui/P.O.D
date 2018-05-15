import io
import socket
import struct
import time
import picamera
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-start", type=float, required=True, help="experiment start time")
parser.add_argument("-duration", type=int, required=True, help="experiment duration")
parser.add_argument("-picdelay", type=int, required=True, help="pictures per day")

args = parser.parse_args()
print("camera args: ",args)
exp_start = args.start
exp_dur = args.duration
camera_delay = args.picdelay

# Connect a client socket to my_server:8000 (change my_server to the
# hostname of your server)
client_socket = socket.socket()
client_socket.connect(('192.168.1.100', 8000))

# Make a file-like object out of the connection
connection = client_socket.makefile('wb')

try:
    with picamera.PiCamera() as camera:

        camera.resolution = (640, 480)
        camera.start_preview()

        # Note the start time and construct a stream to hold image data
        # temporarily (we could write it directly to connection but in this
        # case we want to find out the size of each capture first to keep
        # our protocol simple)
        stream = io.BytesIO()

        while time.time() < exp_start:
            print('sleeping')
            time.sleep(1)

        cur_time = time.time() - exp_start
        print(exp_dur - int(cur_time))
        while int(cur_time) < exp_dur:
            #if int(cur_time) % camera_delay == 0:

            camera.capture(stream, 'jpeg')

            # Write the length of the capture to the stream and flush to
            # ensure it actually gets sent
            connection.write(struct.pack('<L', stream.tell()))
            connection.flush()

            # Rewind the stream and send the image data over the wire
            stream.seek(0)
            connection.write(stream.read())

            # Reset the the stream for the next capture
            stream.seek(0)
            stream.truncate()

            # Write a length of zero to the stream to signal we're done
            

            time.sleep(camera_delay)

            cur_time = time.time() - exp_start

finally:
    connection.write(struct.pack('<L', 0))
    connection.close()
    client_socket.close()
