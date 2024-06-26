
import lvgl as lv
import usys as sys

import firedap_ui
from firedap_ui import ui,base_page,btn_style,bar_style, label_style
import firedap_api


class targetmem_page(base_page):
    def __init__(self):
        super().__init__()

    def ui(self):
        ##################### Connect Button #########################
        table_style = btn_style(self.themes[self.current_theme]["btn1_bg_color"],10)
        table = lv.table(self)
        table.add_style(table_style, lv.PART.MAIN)
        table.add_style(table_style, lv.PART.ITEMS)
        table.set_cell_value(0,0,"Addr")
        table.set_cell_value(0,1,"Value")
        table.set_col_width(0,80)
        table.set_col_width(1,80)
        table.set_size(180,163)
        table.align(lv.ALIGN.TOP_MID, 0, 80)

        targetmem_label = lv.label(self)
        targetmem_label_style = label_style(self.themes[self.current_theme]["label1_color"],self.font_24)
        targetmem_label.add_style(targetmem_label_style,lv.PART.MAIN)
        targetmem_label.set_text("MEMORY")
        targetmem_label.align(lv.ALIGN.TOP_MID, 0, 30)


def test():
    app = ui()
    targetmem_page_instance = targetmem_page()
    targetmem_page_instance.ui()
    app.add_page(targetmem_page_instance)
    app.start()
    while True:
        pass

#test()
