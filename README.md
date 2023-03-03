# MODBUS CRC16

This is a project to perform CRC16 based in [LacobusVentura] (https://github.com/LacobusVentura/MODBUS-CRC16) tests cases.

CRC16 Modbus is a cyclic redundancy check algorithm that is widely used in serial communication protocols, especially in the Modbus protocol. It is a checksum that is calculated over a block of data to ensure its integrity and detect any errors during transmission.
S
## How it Works
The CRC16 Modbus algorithm works by generating a 16-bit checksum over a block of data. The data is divided into 8-bit bytes and a polynomial is applied to each byte to generate a 16-bit remainder. This remainder is then combined with the next byte and the process is repeated until all the bytes have been processed.

The polynomial used in CRC16 Modbus is x^16 + x^15 + x^2 + 1, which is represented in binary as 11000000000000101. This polynomial is used to generate a 16-bit remainder for each byte of data.

Once all the bytes have been processed, the final remainder is the CRC16 Modbus checksum. This checksum is appended to the end of the data block and transmitted along with the data. The receiver then calculates the checksum over the received data and compares it with the checksum received. If the two checksums match, the data is considered to be valid.

## Implementations
The CRC16 Modbus algorithm is widely used in many applications, including industrial control systems, building automation systems, and energy management systems. It is commonly implemented in software or hardware, depending on the application.

In software, the algorithm can be implemented using a lookup table or by using a bit-wise calculation. The bit-wise calculation method is more efficient and is commonly used in embedded systems with limited resources.

In hardware, the algorithm can be implemented using a dedicated CRC16 module or by using a programmable logic device (PLD) or field-programmable gate array (FPGA).

## Conclusion
The CRC16 Modbus algorithm is an important checksum used in many serial communication protocols. It provides a simple and efficient method for ensuring data integrity and detecting errors during transmission. The implementation of the algorithm can vary depending on the application, but it is widely supported and has proven to be a reliable method for data validation.
