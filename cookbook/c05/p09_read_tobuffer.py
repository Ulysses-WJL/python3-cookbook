#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 读取二进制数据到可变缓冲区中
Desc : 
"""
import os.path


def read_into_buffer(filename):
        buf = bytearray(os.path.getsize(filename))
        # 将数据填充到任何预分配的数组中
        with open(filename, 'rb') as f:
            f.readinto(buf)
        return buf


def read_tobuffer():
    buf = bytearray(os.path.getsize('filename'))
    print(buf)
    # 对缓冲区的数据进行切片处理,而没有拷贝
    m1 = memoryview(buf)
    m2 = m1[-5:]
    print(m2)
    m2[:] = b'WORLD'
    print(buf)

    bytearray(b'Hello World')


if __name__ == '__main__':
    read_tobuffer()
