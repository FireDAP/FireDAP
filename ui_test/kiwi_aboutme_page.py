import lvgl as lv
import usys as sys

import kiwidap_ui
from kiwidap_ui import kiwidap_ui,base_page,btn_style,bar_style,drop_down_style,bg_style
import kiwidap_api

class aboutme_page(base_page):
    def __init__(self):
        super().__init__()

    def ui(self):
        ## aboutme label
        about_label = lv.label(self)
        about_label.align(lv.ALIGN.TOP_MID,0,28)
        about_label.set_recolor(True)
        about_label.set_style_text_font(self.font_24, 0)
        about_label.set_text("#87de87 KIWIDAP")

        about_textarea_style = bg_style(self.themes[self.current_theme]["bg1_color"],20)
        about_textarea = lv.textarea(self)
        about_textarea.add_style(about_textarea_style, lv.PART.MAIN)
        about_textarea.set_size(160,140)
        about_textarea.align(lv.ALIGN.CENTER, 0, 5)

        about_label_2 = lv.label(self)
        about_label_2.align(lv.ALIGN.BOTTOM_MID,0,-15)
        about_label_2.set_recolor(True)
        about_label_2.set_style_text_font(self.font_18, 0)
        about_label_2.set_text("#87de87 By@Pallasmanul")

def test():
    app = kiwidap_ui()
    aboutme_instance = aboutme_page()
    aboutme_instance.ui()
    app.add_page(aboutme_instance)
    app.start()
    while True:
        pass

#test()
