import lvgl as lv
import lv_utils

print("Hello This is the Kiwidap")

lv.init()
event_loop = lv_utils.event_loop()
disp_drv = lv.sdl_window_create(240, 280)
indev_drv = lv.sdl_mouse_create()

scr1 = lv.obj()

screen_style = lv.style_t()


btn1 = lv.button(scr1)
btn1.align(lv.ALIGN.TOP_RIGHT, -5, 5)
label = lv.label(btn1)
label.set_text(">")

lv.screen_load(scr1)

while True:
    pass
