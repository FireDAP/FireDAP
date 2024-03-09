
import lvgl as lv
import usys as sys

import kiwidap_ui
from kiwidap_ui import kiwidap_ui,base_page,btn_style,bar_style,text_style
import kiwidap_api


class capture_page(base_page):
    def __init__(self):
        super().__init__()

    def ui(self):
        ##################### Connect Button #########################
        ## font style
        font1_stype = text_style(self.themes[self.current_theme]["font1_color"])
        font2_stype = text_style(self.themes[self.current_theme]["font2_color"])

        ## Capture Button View
        capture_button_style = btn_style(self.themes[self.current_theme]["btn1_bg_color"],20)
        capture_button = lv.button(self)
        capture_button.set_width(180)
        capture_button.set_height(83)
        capture_button.align(lv.ALIGN.CENTER, 0, 0)
        capture_button.add_style(capture_button_style, lv.PART.MAIN)
        capture_button_label = lv.label(capture_button)
        # capture_button_label.set_recolor(True)
        ## Connect Label View
        capture_button_label.set_style_text_font(self.font_24, 0)
        capture_button_label.add_style(font2_stype, lv.PART.MAIN)
        capture_button_label.set_text("CAPTURE")
        capture_button_label.align(lv.ALIGN.CENTER,0 ,0)
        ## Connect Button Callback
        capture_button.add_event_cb(self.capture_button_cb, lv.EVENT.CLICKED, None)

        try:
            script_path = __file__[:__file__.rfind('/')] if __file__.find('/') >= 0 else '.'
        except NameError:
            script_path = ''

        ## image 1
        image_1 = lv.image(self)
        image_1.set_src("S:%s/picture/computer.png" % script_path)
        image_1.align(lv.ALIGN.TOP_MID, 0, 30)

        ## image 2
        image_2 = lv.image(self)
        image_2.set_src("S:%s/picture/pcb.png" % script_path)
        image_2.align(lv.ALIGN.BOTTOM_MID, 0, -30)


    ## CallBack Function
    def capture_button_cb(self,event):
        print("capture button clicked!")


def test():
    app = kiwidap_ui()
    capture_page_instance = capture_page()
    capture_page_instance.ui()
    app.add_page(capture_page_instance)
    app.start()
    while True:
        pass

#test()



