import io
import socket
import struct
import time
import picamera
import config

# Connect a client socket to my_server:8000 (change my_server to the
# hostname of your server)
client_socket = socket.socket()
client_socket.connect((config.server_host, 8000))

# Make a file-like object out of the connection
connection = client_socket.makefile('wb')

try:

    with picamera.Camera() as camera:

        camera.resolution = (640, 480)
        camera.start_preview()

        # Start a preview and let the camera warm up for 2 seconds
        camera.start_preview()
        time.sleep(2)

        # Note the start time and construct a stream to hold image data
        # temporarily (we could write it directly to connection but in this
        # case we want to find out the size of each capture first to keep
        # our protocol simple)
        start = time.time()
        stream = io.BytesIO()

        while True:

            camera.capture(stream, 'jpeg')

            # Write the length of the capture to the stream and flush to
            # ensure it actually gets sent
            connection.write(struct.pack('<L', stream.tell()))
            connection.flush()

            # Rewind the stream and send the image data over the wire
            stream.seek(0)
            connection.write(stream.read())

            # Wait until it's time for the next capture
            time.sleep(config.camera_delay)

            # PiZero loops through here until the experiment is over
            # TODO: Threads needed since PZero needs to do other things too
            if time.time() - start > config.experiment_length:
                break

            # Reset the stream for the next capture
            stream.seek(0)
            stream.truncate()

    # Write a length of zero to the stream to signal we're done
    connection.write(struct.pack('<L', 0))

finally:
    connection.close()
    client_socket.close()
