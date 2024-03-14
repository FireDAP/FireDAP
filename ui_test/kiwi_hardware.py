import usys as sys
import lvgl as lv
import fs_driver
import lv_utils
from  lv_utils import event_loop
import SDL


class hal:
    def __init__(self):
        self.group = lv.group_create()
        self.group.set_default()

        if not event_loop.is_running():
            if sys.platform == 'rp2':
                self.init_rp2_gui()
            elif sys.platform == 'linux':
                self.init_sdl_gui()


    def init_sdl_gui(self):
        # used fo lvgl v9
        # self.event_loop = lv_utils.event_loop()
        # self.disp_drv = lv.sdl_window_create(240, 280)
        # self.indev_drv = lv.sdl_mouse_create()
        # self.keyboard = lv.sdl_keyboard_create()
        # self.keyboard.set_group(self.group)

        lv.init()

        self.WIDTH = 240
        self.HEIGHT = 280
        self.ZOOM = 1
        self.FULLSCREEN = False

        SDL.init(w=self.WIDTH, h=self.HEIGHT, zoom=self.ZOOM, fullscreen=self.FULLSCREEN, auto_refresh=False)
        self.event_loop = lv_utils.event_loop()

        self.disp_buf1 = lv.disp_draw_buf_t()
        self.buf1_1 = bytes(self.WIDTH * 10)
        self.disp_buf1.init(self.buf1_1, None, len(self.buf1_1)//4)
        self.disp_drv = lv.disp_drv_t()
        self.disp_drv.init()
        self.disp_drv.draw_buf = self.disp_buf1
        self.disp_drv.flush_cb = SDL.monitor_flush
        self.disp_drv.hor_res = self.WIDTH
        self.disp_drv.ver_res = self.HEIGHT
        self.disp_drv.register()

        # Regsiter SDL mouse driver
        self.indev_drv = lv.indev_drv_t()
        self.indev_drv.init()
        self.indev_drv.type = lv.INDEV_TYPE.POINTER
        self.indev_drv.read_cb = SDL.mouse_read
        self.mouse = self.indev_drv.register()

        # Register keyboard driver
        self.keyboard_drv = lv.indev_drv_t()
        self.keyboard_drv.init()
        self.keyboard_drv.type = lv.INDEV_TYPE.KEYPAD
        self.keyboard_drv.read_cb = SDL.keyboard_read
        self.keyboard = self.keyboard_drv.register()
        self.keyboard.set_group(self.group)

        ## fs driver init
        self.fs_drv = lv.fs_drv_t()
        fs_driver.fs_register(self.fs_drv, 'S')


        ## png load feature
        from imagetools import get_png_info, open_png

        decoder = lv.img.decoder_create()
        decoder.info_cb = get_png_info
        decoder.open_cb = open_png


    def init_rp2_gui(self):
        import st77xx
        spi=machine.SPI(
            1,
            baudrate=24_000_000,
            polarity=0,
            phase=0,
            sck=machine.Pin(10,machine.Pin.OUT),
            mosi=machine.Pin(11,machine.Pin.OUT),
            miso=machine.Pin(12,machine.Pin.IN)
        )
        self.disp=st77xx.St7789(rot=st77xx.ST77XX_INV_LANDSCAPE,res=(240,280),spi=spi,cs=9,dc=8,bl=13,rst=15,rp2_dma=None)
        self.disp.set_backlight(100)


