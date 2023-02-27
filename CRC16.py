def MODBUS_CRC16_v1(buf, length):
    crc = 0xFFFF
    for i in range(length):
        crc ^= buf[i]
        for bit in range(8):
            if crc & 0x0001:
                crc >>= 1
                crc ^= 0xA001
            else:
                crc >>= 1
    return crc

def MODBUS_CRC16_v2(buf, length):
    table = [0x0000, 0xA001]
    crc = 0xFFFF
    for i in range(length):
        crc ^= buf[i]
        for bit in range(8):
            xor = crc & 0x01
            crc >>= 1
            crc ^= table[xor]
    return crc
    

if __name__ == '__main__':
    
    buf = bytearray([0x5a, 0x00, 0x3f, 0x01, 0x00])
    crc = MODBUS_CRC16_v1(buf, len(buf))

    print('CRC: {}'.format(hex(crc)))
