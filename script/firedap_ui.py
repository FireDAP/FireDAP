import os
import time
import machine
import rp2
import array
import uctypes

import lvgl as lv

from hal.dma import DMA


class FireDAP_UI:
    def __init__( self, parent, display_driver):
        self.parent = parent
        self.display_driver = display_driver
    
        self.run = False
    
        print(" build ui ")
    
    def process( self ):
#         if (self.display_driver.dma_running == True):
#             self.display_driver.lcd.wait_dma()
#             self.display_driver.dma_running = False
#             print( "wait dma " )
        print("timer running")