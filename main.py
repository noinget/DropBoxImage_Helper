import os
import os.path
import re
from datetime import datetime


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def is_image(filename):
    for ext in ['.png', 'jpg']:
        if filename.endwith(ext):
            return True
    return False


def is_image_maper(filename):
    return any(map(filename.endwith, ['.png', '.jpg']))


def get_time(filename):
    p = r'\d{4}-\d{2}-\d{2} \d{2}\.\d{2}\.\d{2}'
    math_obj = re.match(p, filename)
    if math_obj:
        year, month, day, hour, minute, second = map(int, math_obj.groups())
        return datetime(year, month, day, hour, minute, second)


if __name__ == '__main__':
    print_hi('PyCharm')

filenames = os.listdir(os.getcwd())
filenames = os.listdir('images/')
print(filenames)
images = filter(is_image_maper, filenames)
print(images)
get_time(images)
