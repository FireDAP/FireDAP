
import lvgl as lv
import usys as sys

import kiwidap_ui
from kiwidap_ui import kiwidap_ui,base_page,btn_style,bar_style,drop_down_style,bg_style,text_style
import kiwidap_api



class burn_page(base_page):
    def __init__(self):
        super().__init__()

    def ui(self):
        ## font style
        font1_stype = text_style(self.themes[self.current_theme]["font1_color"])
        font2_stype = text_style(self.themes[self.current_theme]["font2_color"])

        burn_firmware_drop_down_style = drop_down_style(self.themes[self.current_theme]['btn1_bg_color'])
        burn_firmware_drop_down = lv.dropdown(self)
        burn_firmware_drop_down.set_options("\n".join([
            "example.elf",
            "timesf.elf",
            "colad.elf"
        ]))
        burn_firmware_drop_down.set_size(160,40)
        burn_firmware_drop_down.add_style(burn_firmware_drop_down_style, lv.PART.MAIN)
        burn_firmware_drop_down.align(lv.ALIGN.TOP_MID, 0, 40)

        burn_firmware_page_style = bg_style(self.themes[self.current_theme]["bg1_color"],10)
        burn_firmware_page = lv.textarea(self)
        burn_firmware_page.add_style(burn_firmware_page_style, lv.PART.MAIN)
        burn_firmware_page.set_size(160,110)
        burn_firmware_page.align(lv.ALIGN.CENTER, 0, 10)

        ## firmware download bar view
        burn_frimware_download_bar_style = bar_style(self.themes[self.current_theme]["btn1_bg_color"])
        burn_frimware_download_bar = lv.bar(self)
        burn_frimware_download_bar.set_size(163,12)
        burn_frimware_download_bar.align(lv.ALIGN.BOTTOM_MID, 0, -50)
        burn_frimware_download_bar.add_style(burn_frimware_download_bar_style, lv.PART.INDICATOR)
        burn_frimware_download_bar.set_range(0,100)
        burn_frimware_download_bar.set_value(0,lv.ANIM.ON)

        ## Battery bar label view
        burn_frimware_download_bar_label = lv.label(burn_frimware_download_bar)
        burn_frimware_download_bar_label.align(lv.ALIGN.CENTER, 0 ,0)
        burn_frimware_download_bar_label.add_style(font2_stype, lv.PART.MAIN)
        burn_frimware_download_bar_label.set_text("89%")

        ## burn target label
        burn_target_label = lv.label(self)
        burn_target_label.align(lv.ALIGN.BOTTOM_LEFT,30,-20)
        burn_target_label.add_style(font1_stype, lv.PART.MAIN)
        burn_target_label.set_style_text_font(self.font_18, 0)
        burn_target_label.set_text("TARGET")

def test():
    app = kiwidap_ui()
    burn_page_instance = burn_page()
    burn_page_instance.ui()
    app.add_page(burn_page_instance)
    app.start()
    while True:
        pass

#test()


