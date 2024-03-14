import lvgl as lv
import lv_utils

print("Hello This is the Kiwidap")

import SDL
import sys 

WIDTH = 240
HEIGHT = 280
ZOOM = 1
FULLSCREEN = False

lv.init()

SDL.init(w=WIDTH, h=HEIGHT, zoom=ZOOM, fullscreen=FULLSCREEN, auto_refresh=False)
event_loop = lv_utils.event_loop()
group = lv.group_create()
group.set_default()

# Register SDL display driver.
disp_buf1 = lv.disp_draw_buf_t()
buf1_1 = bytes(WIDTH * 10)
disp_buf1.init(buf1_1, None, len(buf1_1)//4)
disp_drv = lv.disp_drv_t()
disp_drv.init()
disp_drv.draw_buf = disp_buf1
disp_drv.flush_cb = SDL.monitor_flush
disp_drv.hor_res = WIDTH
disp_drv.ver_res = HEIGHT
disp_drv.register()
# Regsiter SDL mouse driver
indev_drv = lv.indev_drv_t()
indev_drv.init()
indev_drv.type = lv.INDEV_TYPE.POINTER
indev_drv.read_cb = SDL.mouse_read
mouse = indev_drv.register()
# Register keyboard driver
keyboard_drv = lv.indev_drv_t()
keyboard_drv.init()
keyboard_drv.type = lv.INDEV_TYPE.KEYPAD
keyboard_drv.read_cb = SDL.keyboard_read
keyboard = keyboard_drv.register()
keyboard.set_group(group)


scr1 = lv.obj()

screen_style = lv.style_t()


btn1 = lv.btn(scr1)
btn1.align(lv.ALIGN.TOP_RIGHT, -5, 5)
label = lv.label(btn1)
label.set_text(">")

try:
    script_path = __file__[:__file__.rfind('/')] if __file__.find('/') >= 0 else '.'
except NameError:
    script_path = ''

from imagetools import get_png_info, open_png

decoder = lv.img.decoder_create()
decoder.info_cb = get_png_info
decoder.open_cb = open_png

try:
    with open('./picture/pcb.png','rb') as f:
        png_data = f.read()
except:
    print("Could not find img_cogwheel_argb.png")
    sys.exit()


img_cogwheel_argb = lv.img_dsc_t({
  'data_size': len(png_data),
  'data': png_data
})

img1 = lv.img(scr1)
img1.set_src(img_cogwheel_argb)
img1.align(lv.ALIGN.CENTER, 0, -20)



lv.scr_load(scr1)

while True:
    pass
