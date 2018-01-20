import json
import mmap
import contextlib
import time
from random import randint

CLEAR = "                                                                              "


def create_map_file():
    with open('ultrasonic_sensors.txt', 'w') as f:
        f.write(CLEAR)


def start():
    with open('ultrasonic_sensors.txt', 'r+') as f:
        with contextlib.closing(mmap.mmap(f.fileno(), 0)) as m:
            while True:
                # replace random with a call to read each sensor
                sensors = {'front': randint(20, 750),
                           'left': randint(20, 750),
                           'right': randint(20, 750)}
                sensors_json = str.encode(json.dumps(sensors))  # serialize data into a bytes

                m.seek(0)  # rewind memory map and clear buffer
                m.write(str.encode(CLEAR))
                m.flush()

                m.seek(0)  # rewind memory map and write data
                m.write(sensors_json)
                m.flush()

                m.seek(0)  # rewind and test read
                print('line :%s' % m.readline())
                time.sleep(.1)


if __name__ == '__main__':
    create_map_file()
    start()
