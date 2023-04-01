from PIL import Image
from tkinter import Tk

global dat

dat = []


def s_det():
    f = open('other docs\\screen_details.txt', 'w')
    root = Tk()
    root.state('zoomed')
    screen_w = root.winfo_screenwidth()
    dat.append(screen_w)
    screen_h = root.winfo_screenheight()
    dat.append(screen_h)
    f.write(str(screen_w) + ' ' + str(screen_h))
    f.close()
    root.destroy()


def image_resize(image_name, dim='none', num='none'):
    global screen_w, screen_h
    if dim == 'none':
        screen_w = int(dat[0])
        screen_h = int(dat[1])
    if dim == 'sq':
        screen_w = sy(num)
        screen_h = screen_w
    elif dim == 'rec':
        screen_w = sx(num[0])
        screen_h = sy(num[1])
    else:
        pass
    image = Image.open(image_name)
    # The (screen_h, screen_w) is (height, width)
    image_x = image.resize((screen_w, screen_h), Image.ANTIALIAS)
    return image_x


def sx(num):
    screen_w = int(dat[0])
    # screen_w = 1426
    xa = screen_w * num
    xb = round(xa / 1280)
    return round(xb)


def sy(num):
    screen_h = int(dat[1])

    ya = screen_h * num
    yb = round(ya / 720)
    return round(yb)


def get_data():
    return dat


s_det()

if __name__ == '__main__':
    pass
