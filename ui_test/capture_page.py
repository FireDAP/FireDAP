import lvgl as lv
import usys as sys

import firedap_ui
from firedap_ui import ui,base_page,btn_style,bar_style
import firedap_api


class capture_page(base_page):
    def __init__(self):
        super().__init__()

    def ui(self):
        ##################### Connect Button #########################
        ## Capture Button View
        capture_button_style = btn_style(self.themes[self.current_theme]["btn1_bg_color"],20)
        capture_button = lv.btn(self)
        capture_button.set_width(180)
        capture_button.set_height(83)
        capture_button.align(lv.ALIGN.CENTER, 0, 0)
        capture_button.add_style(capture_button_style, lv.PART.MAIN)
        capture_button_label = lv.label(capture_button)
        capture_button_label.set_recolor(True)
        ## Connect Label View
        capture_button_label.set_style_text_font(self.font_24, 0)
        capture_button_label.set_text("#535d6c CAPTURE")
        capture_button_label.align(lv.ALIGN.CENTER,0 ,0)
        ## Connect Button Callback
        capture_button.add_event_cb(self.capture_button_cb, lv.EVENT.CLICKED, None)

        try:
            script_path = __file__[:__file__.rfind('/')] if __file__.find('/') >= 0 else '.'
        except NameError:
            script_path = ''



        # load png resource
        try:
            with open('./picture/pcb.png','rb') as f:
                self.png_data = f.read()
        except:
            print("Could not find img_cogwheel_argb.png")
            sys.exit()

        image_pcb_png = lv.img_dsc_t({
            'data_size': len(self.png_data),
            'data': self.png_data
        })

        try:
            with open('./picture/computer.png','rb') as f:
                self.png_data = f.read()
        except:
            print("Could not find img_cogwheel_argb.png")
            sys.exit()

        image_computer_png = lv.img_dsc_t({
            'data_size': len(self.png_data),
            'data': self.png_data
        })

        image_1 = lv.img(self)
        image_1.set_src(image_computer_png)
        image_1.align(lv.ALIGN.TOP_MID, 0, 30)

        ## image 2
        image_2 = lv.img(self)
        image_2.set_src(image_pcb_png)
        image_2.align(lv.ALIGN.BOTTOM_MID, 0, -30)


    ## CallBack Function
    def capture_button_cb(self,event):
        print("capture button clicked!")


def test():
    app = ui()
    capture_page_instance = capture_page()
    capture_page_instance.ui()
    app.add_page(capture_page_instance)
    app.start()
    while True:
        pass

#test()
