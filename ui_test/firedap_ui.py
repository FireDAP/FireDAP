import usys as sys
import lvgl as lv
import lv_utils
from lv_utils import event_loop
import fs_driver
import firedap_hardware

print("Hello This is the KiwidapUi")

sys.path.append('')

try:
    script_path = __file__[:__file__.rfind('/')] if __file__.find('/') >= 0 else '.'
except NameError:
    script_path = ''

lv.init()


class bg_style(lv.style_t):
    def __init__(self, color, radius):
        super().__init__()
        self.set_bg_color(lv.color_hex(color))
        self.set_radius(lv.dpx(radius))

class btn_style(lv.style_t):
    def __init__(self, color, radius):
        super().__init__()
        self.set_bg_color(lv.color_hex(color))
        self.set_radius(lv.dpx(radius))

class label_style(lv.style_t):
    def __init__(self, color, font):
        super().__init__()
        self.set_text_color(lv.color_hex(color))
        self.set_text_font(font)

class bar_style(lv.style_t):
    def __init__(self, color):
        super().__init__()
        self.set_bg_opa(lv.OPA.COVER)
        self.set_bg_color(lv.color_hex(color))
        self.set_bg_grad_color(lv.color_hex(0x87de87))
        self.set_bg_grad_dir(lv.GRAD_DIR.HOR)

class drop_down_style(lv.style_t):
    def __init__(self, color):
        super().__init__()
        self.set_bg_color(lv.color_hex(color))


class ui(firedap_hardware.hal):
    def __init__(self):
        super().__init__()
        self.pages = []
        self.current_page=0

    def start(self):
        if len(self.pages) > 0:
            print("load page")
            lv.scr_load(self.pages[self.current_page])
        else:
            print("Please Add a  Page")

    def add_page(self,page):
        page.add_event_cb(self.switch_page_event_cb,lv.EVENT.GESTURE,None)
        self.pages.append(page)
        print(self.pages)

    def switch_page_event_cb(self,event):
        screen = event.get_current_target()
        indev = event.get_indev()
        dir = indev.get_gesture_dir()
        if dir == lv.DIR.LEFT:
            if len(self.pages)-1 > self.current_page:
                self.current_page = self.current_page + 1
                self.start()
            else:
                print("no more page")

        elif dir == lv.DIR.RIGHT:
            if self.current_page > 0 :
                self.current_page = self.current_page - 1
                self.start()
            else:
                print("no more page")

        elif dir == lv.DIR.TOP:
            pass
        elif dir == lv.DIR.BOTTOM:
            pass


class base_page(lv.obj):
    def __init__(self, *args, **kwds):
        super().__init__(*args, **kwds)

        self.themes={}
        self.fonts = []
        self.colors = {"pink":0xff80e5,"green":0x87de87,"perpel":0x9955ff, "grey":0x353535, "grey1":0x535d6c}
        self.current_theme = "Dracula_Theme"
        self.Dracula_Theme = { "name": "Dracula_Theme", "bg_color": 0x353535,"bg1_color":0x555555, "btn1_bg_color": 0xff80e5, "btn1_label_color":0x535d6c , "btn2_bg_color":0x87de87, "btn2_label_color": 0x535d6c, "label_bg_color": 0x9955ff, "label1_color": 0x87de87}
        self.add_theme(self.Dracula_Theme)

        page_style = bg_style(self.themes[self.current_theme]["bg_color"],50)
        self.add_style(page_style, lv.PART.MAIN)

        ## Load font , it should be late with fs driver init
        self.font_12 = lv.font_load("S:%s/font/font-12.font" % script_path)
        self.font_18 = lv.font_load("S:%s/font/font-18.font" % script_path)
        self.font_24 = lv.font_load("S:%s/font/font-24.font" % script_path)
        self.font_source_12 = lv.font_load("S:%s/font/font-source-12.font" % script_path)
        self.font_source_24 = lv.font_load("S:%s/font/font-source-24.font" % script_path)

    def add_font(self,font):
        self.fonts.append(font)

    def add_color(self,color):
        pass

    def add_theme(self,theme):
        self.themes[theme['name']]=theme
        print(self.themes)

    def set_current_theme(self,theme_name):
       print(len(self.themes[theme_name]))
       if len(self.themes[theme_name]) != 0:
           self.current_theme = theme_name
       else:
           print("no theme")


