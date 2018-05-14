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
        # Start a preview and let the camera warm up for 2 seconds
        #camera.start_preview()
        #time.sleep(2)

        # Note the start time and construct a stream to hold image data
        # temporarily (we could write it directly to connection but in this
        # case we want to find out the size of each capture first to keep
        # our protocol simple)
        start = time.time()
        stream = io.BytesIO()

        while time.time() < exp_start:
            time.sleep(1)

        cur_time = time.time() - exp_start
        while int(cur_time) < exp_dur:
            if int(cur_time) % camera_delay == 0:
                for foo in camera.capture_continuous(stream, 'jpeg'):
                    # Write the length of the capture to the stream and flush to
                    # ensure it actually gets sent
                    connection.write(struct.pack('<L', stream.tell()))
                    connection.flush()
                    # Rewind the stream and send the image data over the wire
                    stream.seek(0)
                    connection.write(stream.read())
                    # If we've been capturing for more than 30 seconds, quit
                    if time.time() - start > 30:
                        break
                    # Reset the stream for the next capture
                    stream.seek(0)
                    stream.truncate()
                # Write a length of zero to the stream to signal we're done
                connection.write(struct.pack('<L', 0))
            cur_time = time.time() - exp_start
finally:
    connection.close()
    client_socket.close()
