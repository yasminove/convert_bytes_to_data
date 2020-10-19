from struct import *

convert_to_bytes = pack('iif', 2, 4, 6.7)

original_data = unpack('iif', convert_to_bytes)
# original_data = unpack('iif', b'\x02\x00\x00\x00\x04\x00\x00\x00ff\xd6@')

# print(convert_to_bytes)
print(original_data)