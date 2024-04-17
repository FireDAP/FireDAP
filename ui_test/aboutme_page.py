import lvgl as lv
import usys as sys

import firedap_ui
from firedap_ui import ui,base_page,btn_style,bar_style,drop_down_style,bg_style, label_style
import firedap_api

class aboutme_page(base_page):
    def __init__(self):
        super().__init__()

    def ui(self):
        ## aboutme label
        about_label_style = label_style(self.themes[self.current_theme]["label1_color"], self.font_24)
        about_label = lv.label(self)
        about_label.align(lv.ALIGN.TOP_MID,0,28)
        about_label.add_style(about_label_style, lv.PART.MAIN)
        about_label.set_text("FireDAP")

        about_textarea_style = bg_style(self.themes[self.current_theme]["bg1_color"],20)
        about_textarea = lv.textarea(self)
        about_textarea.add_style(about_textarea_style, lv.PART.MAIN)
        about_textarea.set_size(160,140)
        about_textarea.align(lv.ALIGN.CENTER, 0, 5)

        about_label_2_style = label_style(self.themes[self.current_theme]["label1_color"], self.font_24)
        about_label_2 = lv.label(self)
        about_label_2.align(lv.ALIGN.BOTTOM_MID,0,-20)
        about_label_2.add_style(about_label_2_style, lv.PART.MAIN)
        about_label_2.set_text("By@Pallasmanul")


def test():
    app = ui()
    aboutme_instance = aboutme_page()
    aboutme_instance.ui()
    app.add_page(aboutme_instance)
    app.start()
    while True:
        pass

#test()
