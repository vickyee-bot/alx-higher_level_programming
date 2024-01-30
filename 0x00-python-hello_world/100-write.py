import sys

message = "and that piece of art is useful - Dora Korpar, 2015-10-19\n"

    message_bytes = message.encode('utf-8')

    sys.stderr.write(message_bytes)

    sys.exit(1)
