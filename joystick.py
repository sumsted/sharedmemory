import mmap
import contextlib
import time

with open('joystick_position.txt', 'r+') as f:
    with contextlib.closing(mmap.mmap(f.fileno(), 0)) as m:
        i = 1
        while (1):
            m.seek(0)  # rewind
            i = 0 if i > 250 else i
            m[0] = i%8
            i += 1
            m[1] = i%100
            i += 1
            m[2] = i%100
            i += 1
            m[3] = i%100
            i += 1
            m.flush()

            m.seek(0)  # rewind
            if True:#i % 100 == 0:
                print('byte via read :%d'%i)
                # print('byte via read :', m.read(1))
                # print('byte via read :', m.read(1))
                # print('byte via read :', m.read(1))
