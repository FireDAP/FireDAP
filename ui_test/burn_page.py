import lvgl as lv
import usys as sys

import firedap_ui
from firedap_ui import ui,base_page,btn_style,bar_style,drop_down_style,bg_style, label_style
import firedap_api



class burn_page(base_page):
    def __init__(self):
        super().__init__()

    def ui(self):
        burn_firmware_drop_down_style = drop_down_style(self.themes[self.current_theme]['btn2_bg_color'])
        burn_firmware_drop_down = lv.dropdown(self)
        burn_firmware_drop_down.set_options("\n".join([
            "example.elf",
            "timesf.elf",
            "colad.elf"
        ]))
        burn_firmware_drop_down.set_size(160,40)
        burn_firmware_drop_down.add_style(burn_firmware_drop_down_style, lv.PART.MAIN)
        burn_firmware_drop_down.align(lv.ALIGN.TOP_MID, 0, 30)

        burn_firmware_page_style = bg_style(self.themes[self.current_theme]["bg1_color"],10)
        burn_firmware_page = lv.textarea(self)
        burn_firmware_page.add_style(burn_firmware_page_style, lv.PART.MAIN)
        burn_firmware_page.set_size(160,110)
        burn_firmware_page.align(lv.ALIGN.CENTER, 0, 0)


        ## burn target label
        burn_button_style = btn_style(self.themes[self.current_theme]["btn1_bg_color"],20)
        burn_button = lv.btn(self)
        burn_button.set_width(160)
        burn_button.set_height(43)
        burn_button.align(lv.ALIGN.CENTER, 0, 90)
        burn_button.add_style(burn_button_style, lv.PART.MAIN)

        burn_target_label_style = label_style(self.themes[self.current_theme]["btn1_label_color"], self.font_18)
        burn_target_label = lv.label(burn_button)
        burn_target_label.align(lv.ALIGN.BOTTOM_LEFT,10,-3)
        burn_target_label.add_style(burn_target_label_style, lv.PART.MAIN)
        burn_target_label.set_text("DOWNLOAD")

def test():
    app = ui()
    burn_page_instance = burn_page()
    burn_page_instance.ui()
    app.add_page(burn_page_instance)
    app.start()
    while True:
        pass

#test()
