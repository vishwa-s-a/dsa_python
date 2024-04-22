import math

# Constants for MD5 algorithm
T = [int(2**32 * abs(math.sin(i + 1))) & 0xFFFFFFFF for i in range(64)]
S = [
    [7, 12, 17, 22], [5, 9, 14, 20], [4, 11, 16, 23], [6, 10, 15, 21]
]

def left_rotate(x, n):
    return ((x << n) | (x >> (32 - n))) & 0xFFFFFFFF

def md5(message):
    # Initialize variables
    A = 0x67452301
    B = 0xEFCDAB89
    C = 0x98BADCFE
    D = 0x10325476

    # Pre-processing: padding the message
    orig_len_in_bits = len(message) * 8
    message += b'\x80'
    while len(message) % 64 != 56:
        message += b'\x00'
    message += orig_len_in_bits.to_bytes(8, byteorder='little')

    # Process the message in 512-bit blocks
    for i in range(0, len(message), 64):
        chunk = message[i:i+64]
        a, b, c, d = A, B, C, D

        # Main loop
        for j in range(64):
            if j < 16:
                F = (B & C) | ((~B) & D)
                g = j
            elif j < 32:
                F = (D & B) | ((~D) & C)
                g = (5 * j + 1) % 16
            elif j < 48:
                F = B ^ C ^ D
                g = (3 * j + 5) % 16
            else:
                F = C ^ (B | (~D))
                g = (7 * j) % 16

            d_temp = d
            d = c
            c = b
            b = (b + left_rotate((a + F + T[j] + int.from_bytes(chunk[4*g:4*g+4], byteorder='little')), S[j//16][j%4])) & 0xFFFFFFFF
            a = d_temp

        # Update variables
        A = (A + a) & 0xFFFFFFFF
        B = (B + b) & 0xFFFFFFFF
        C = (C + c) & 0xFFFFFFFF
        D = (D + d) & 0xFFFFFFFF

    # Concatenate the hash segments
    return (A.to_bytes(4, byteorder='little') +
            B.to_bytes(4, byteorder='little') +
            C.to_bytes(4, byteorder='little') +
            D.to_bytes(4, byteorder='little'))

# Example usage
message = b"Hello, World!!"
print("The input message is: Hello World!!")
hashed_message = md5(message)
print("MD5 Hash:", hashed_message.hex())

