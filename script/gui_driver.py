import lvgl as lv

class Display_Driver:
    def __init__( self, width, height, lcd, tsc, fb_rows=64 ):
        self.width = width
        self.height = height
        self.lcd = lcd
        self.tsc = tsc
        self.fb_rows = fb_rows

        self.is_fb1 = True
        self.dma_running = False

        self.x = 0
        self.y = 0
        self.s = 0

        self.init_gui()

    def init_gui( self ):
        lv.init()

        self.disp_drv = lv.disp_create(self.width, self.height)

        self.fb1 = bytearray( self.width*self.fb_rows )
        self.fb2 = bytearray( self.width*self.fb_rows )
        print( "len( fb1 )", len( self.fb1 ) )
        print( "len( fb2 )", len( self.fb2 ) )

        print( "disp set draw buffers" )
        self.disp_drv.set_draw_buffers(self.fb1, self.fb2, len(self.fb1),lv.DISP_RENDER_MODE.PARTIAL)

        print( "disp set flash cb")
        self.disp_drv.set_flush_cb(self.disp_drv_flush_cb)

#         print( "disp set indev" )
#         self.indev_drv = lv.indev_t()
#         self.indev_drv.set_disp(self.disp_drv)
#         self.indev_drv.set_type(lv.INDEV_TYPE.POINTER)
#         self.indev_drv.set_read_cb(self.indev_drv_read_cb)


    def disp_drv_flush_cb( self, disp_drv, area, color ):
        print( "disp_drv_flush_cb", area.x1, area.x2, area.y1, area.y2 )

        if( self.dma_running == True ):
            self.lcd.wait_dma()
            self.dma_running = False

        if( self.is_fb1 ):
            fb = memoryview( self.fb1 )
        else:
            fb = memoryview( self.fb2 )
        self.is_fb1 = not self.is_fb1

        x = area.x1
        y = area.y1
        w = area.x2 - area.x1 + 1
        h = area.y2 - area.y1 + 1
        self.lcd.draw_bitmap_dma( x, y, w, h, fb[0:w*h*lv.color_t.__SIZE__], is_blocking=False )
        self.dma_running = True

        disp_drv.flush_ready()

    def indev_drv_read_cb( self, indev_drv, data ):
        #print( "indev_drv_read_cb", self.x, self.y, self.s )

        if( self.dma_running == True ):
            self.lcd.wait_dma()
            self.dma_running = False

        self.tsc.spi_init()
        x, y = self.tsc.read()
        self.lcd.spi_init() # Reinit SPI with LCD settings

        if( x or y ):
            self.x = x
            self.y = y
            self.s = 1
            #print( "indev_drv_read_cb", self.x, self.y, self.s )
        else:
            self.s = 0

        data.point.x = self.x
        data.point.y = self.y
        data.state = self.s

        return False

print("done")
