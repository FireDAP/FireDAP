
import kiwidap
import time

SWDIO = 3
SWCLK = 4
RESET = 5
TDI = 6
TDO = 7

kiwidap.init(SWCLK,SWDIO,TDI,TDO,RESET)

RXBUFFER = bytearray(64)
TXBUFFER = bytearray(64)

def kiwidap_thread():
    while True:
        if(kiwidap.winusb_read(RXBUFFER) == True):
            len = kiwidap.progress(RXBUFFER,TXBUFFER)
            kiwidap.winusb_write(TXBUFFER,len)
            print(RXBUFFER)
            print(TXBUFFER)
        time.sleep_us(1)

kiwidap_thread()
