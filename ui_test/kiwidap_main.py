import lvgl as lv
import usys as sys

import kiwidap_ui
from kiwidap_ui import kiwidap_ui,base_page,btn_style,bar_style
import kiwidap_api


from kiwi_start_page import start_page
from kiwi_burn_page import burn_page
from kiwi_capture_page import capture_page
from kiwi_targetreg_page import targetreg_page
from kiwi_targetmem_page import targetmem_page
from kiwi_aboutme_page import aboutme_page


def main():
    app = kiwidap_ui()

    start_page_instance = start_page()
    start_page_instance.ui()

    burn_page_instance = burn_page()
    burn_page_instance.ui()


    capture_page_instance = capture_page()
    capture_page_instance.ui()


    targetreg_page_instance = targetreg_page()
    targetreg_page_instance.ui()

    targetmem_page_instance = targetmem_page()
    targetmem_page_instance.ui()

    aboutme_page_instance = aboutme_page()
    aboutme_page_instance.ui()

    app.add_page(start_page_instance)
    app.add_page(burn_page_instance)
    app.add_page(capture_page_instance)
    app.add_page(targetreg_page_instance)
    app.add_page(targetmem_page_instance)
    app.add_page(aboutme_page_instance)

    app.start()
    while True:
        pass

main()

