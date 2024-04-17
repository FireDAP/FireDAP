# import firedap
# import time

# byte_recv_array = bytearray(64)
# byte_send_array = bytearray(64)

# print("This is the kiwidap api")


# while True:
#     firedap.winusb_read(byte_recv_array)
#     send_len = firedap.progress(byte_recv_array, byte_send_array)
#     firedap.winusb_write(byte_send_array, send_len)
#     byte_send_array[:] = b'\0' * len(byte_send_array)
#     byte_recv_array[:] = b'\0' * len(byte_recv_array)
#     time.sleep_ms(40)

