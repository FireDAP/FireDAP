import lvgl as lv
import usys as sys

import firedap_ui
from firedap_ui import ui,base_page,btn_style,bar_style
import firedap_api


class start_page(base_page):
    def __init__(self):
        super().__init__()

    def ui(self):
        ##################### Connect Button #########################

        ## Connect Button View
        connect_button_style = btn_style(self.themes[self.current_theme]["btn1_bg_color"],20)
        connect_button = lv.btn(self)
        connect_button.set_width(180)
        connect_button.set_height(83)
        connect_button.align(lv.ALIGN.CENTER, 0, -20)
        connect_button.add_style(connect_button_style, lv.PART.MAIN)
        connect_button_label = lv.label(connect_button)
        connect_button_label.set_recolor(True)
        ## Connect Label View
        connect_button_label.set_style_text_font(self.font_24, 0)
        connect_button_label.set_text("#535d6c CONNECT")
        connect_button_label.align(lv.ALIGN.CENTER,0 ,0)
        ## Connect Button Callback
        connect_button.add_event_cb(self.connect_button_cb, lv.EVENT.CLICKED, None)


        ###################### Light  Button #########################

        light_button_style = btn_style(self.themes[self.current_theme]["btn2_bg_color"],10)
        light_button = lv.btn(self)
        light_button.add_style(light_button_style, lv.PART.MAIN)
        light_button.align(lv.ALIGN.TOP_LEFT, 35, 35)
        light_button.set_width(59)
        light_button.set_height(26)
        light_button_label = lv.label(light_button)
        light_button_label.set_recolor(True)
        light_button_label.set_style_text_font(self.font_12, 0)
        light_button_label.set_text("#535d6c SLEEP")
        light_button_label.align(lv.ALIGN.CENTER, 0, 0)



        ####################### Battery  Bar  #########################

        ## Battery bar view
        battery_bar_style = bar_style(self.themes[self.current_theme]["btn1_bg_color"])
        battery_bar = lv.bar(self)
        battery_bar.set_size(42,20)
        battery_bar.align(lv.ALIGN.TOP_RIGHT, -30, 35)
        battery_bar.add_style(battery_bar_style, lv.PART.INDICATOR)
        battery_bar.set_range(0,100)
        battery_bar.set_value(21,lv.ANIM.ON)
        ## Battery bar label view
        battery_bar_label = lv.label(battery_bar)
        battery_bar_label.align(lv.ALIGN.CENTER, 0 ,0)
        battery_bar_label.set_recolor(True)
        battery_bar_label.set_text("#535d6c 89%")
        ## Battery bar animation
        battery_bar_animation = lv.anim_t()
        battery_bar_animation.init()
        battery_bar_animation.set_time(3000)
        battery_bar_animation.set_playback_time(3000)
        battery_bar_animation.set_var(battery_bar)
        battery_bar_animation.set_values(0,100)
        battery_bar_animation.set_repeat_count(lv.ANIM_REPEAT.INFINITE)
        ## Battery bar callback
        battery_bar_animation.set_custom_exec_cb(lambda a, val: self.set_temp(battery_bar,val))
        lv.anim_t.start(battery_bar_animation)


        ####################### Memory Meter  #########################

        ## memory meter view
        memory_meter = lv.meter(self)
        memory_meter.remove_style(None, lv.PART.MAIN)
        memory_meter.remove_style(None, lv.PART.INDICATOR)
        memory_meter.set_size(80,80)
        memory_meter.align(lv.ALIGN.BOTTOM_RIGHT ,-30 ,-20)
        memory_meter_scale = memory_meter.add_scale()
        memory_meter.set_scale_ticks( memory_meter_scale,0, 0, 0, lv.color_black())
        memory_meter.set_scale_range( memory_meter_scale,0, 100, 360, 0)
        indic_w = 100
        indic1 = memory_meter.add_arc( memory_meter_scale, indic_w,lv.color_hex(0xff80e5), 0)
        memory_meter.set_indicator_start_value(indic1, 0)
        memory_meter.set_indicator_end_value(indic1, 100)
        indic2 = memory_meter.add_arc( memory_meter_scale, indic_w, lv.color_hex(0x87de87), 0)
        memory_meter.set_indicator_start_value(indic2, 0)  # Start from the previous
        memory_meter.set_indicator_end_value(indic2, 40)
        ## memory meter label view
        memory_meter_label = lv.label(self)
        memory_meter_label.align(lv.ALIGN.BOTTOM_LEFT, 30, -60)
        memory_meter_label.set_recolor(True)
        memory_meter_label.set_style_text_font(self.font_source_24, 0)
        memory_meter_label.set_text("#87de87 REMAIN")
        memory_meter_label = lv.label(self)
        memory_meter_label.align(lv.ALIGN.BOTTOM_LEFT, 30, -30)
        memory_meter_label.set_recolor(True)
        memory_meter_label.set_style_text_font(self.font_source_24, 0)
        memory_meter_label.set_text("#87de87 MEM")
        memory_meter_label = lv.label(self)
        memory_meter_label.align(lv.ALIGN.BOTTOM_LEFT, 85, -35)
        memory_meter_label.set_recolor(True)
        memory_meter_label.set_text("#87de87 32%")

    ## CallBack Function
    def connect_button_cb(self,event):
        print("connect button clicked !")

    def set_temp(self, bar, temp):
        bar.set_value(temp, lv.ANIM.ON)


def test():
    app = ui()
    start_page_instance = start_page()
    start_page_instance.ui()
    app.add_page(start_page_instance)
    app.start()
    while True:
        pass

#test()
