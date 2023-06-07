"""
Полигон - 1
"""
import datetime

PATH = 'what-what'


def write_memory(text_memory, mode):
    with open(PATH, mode=mode, encoding='utf-8') as wf:
        wf.write(f'{datetime.datetime.now()}\n'
                 f'{text_memory}\n')
    with open(PATH, mode='r', encoding='utf-8') as wf:
        print(*wf)


if __name__ == '__main__':
    write_memory('Но вот как это сделать...?', 'a')
