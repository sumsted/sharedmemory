import mmap
import contextlib
import time

commands = [['Robot__left_speed', 'speed'],
            ['Robot__right_speed', 'speed'],
            ['Robot_stop'],
            ['Robot_forward', 'speed', 'seconds'],
            ['Robot_backward', 'speed', 'seconds'],
            ['Robot_right', 'speed', 'seconds'],
            ['Robot_left', 'speed', 'seconds'],
            ['Robot_left_glide', 'speed', 'seconds'],
            ['Robot_right_glide', 'speed', 'seconds']]

with open('joystick_position.txt', 'r') as f:
    with contextlib.closing(mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)) as m:
        while (1):
            m.seek(0)
            print('\nreading...')
            command = commands[ord(m.read(1))]
            print('command = %s'% command[0])
            for param in command[1:]:
                print('%s = %d'%(param, ord(m.read(1))))
            time.sleep(.25)
