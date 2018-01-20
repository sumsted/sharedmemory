import json
import mmap
import contextlib
import time

with open('ultrasonic_sensors.txt', 'r') as f:
    with contextlib.closing(mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)) as m:
        while True:
            m.seek(0)
            print('\nreading...')
            sensors_json = m.readline().decode("utf-8")
            print(sensors_json)
            try:
                sensors = json.loads(sensors_json)
            except Exception as e:
                print("exception %s"% str(e))
            print('front: %(front)s\nleft: %(left)s\nright: %(right)s\n' % sensors)
            time.sleep(.25)
