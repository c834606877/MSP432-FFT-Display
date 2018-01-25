#!/usr/bin/evn python

import serial
import time
from Tkinter import *

class MSP432(object):
    """docstring for msp432"""
    def __init__(self):
        self.ser = serial.Serial('COM4', 115200, timeout=1)
        self.rate = 8000

    def getPortName(self):
        return self.ser.name

    def get256data(self):
        self.ser.write('ACK=rfft')
        return self.ser.read(256)
    def get512data(self):
        self.ser.write('ACK=rfft')
        return self.ser.read(512)
    def setSamplingRate(self, rate = 8000):
        print rate
        self.rate = rate
        if rate == 8000:
            self.ser.write('ACK=s1')
        elif rate == 16000:
            self.ser.write('ACK=s2')
        elif rate == 32000:
            self.ser.write('ACK=s3')

    def readPCMtoWave(self):
        self.ser.write('ACK=pcmon')
        file = open('c:/1.wav', 'wb')
        count = 0
        try:
            while True:
                pcmdata = self.ser.read(1024)
                if pcmdata is None or  len(pcmdata) == 0:
                    break
                hexShow(pcmdata)
                file.write(pcmdata)
                count = count + 1
                if count > 100:
                    self.stopPCM()
        except Exception as e:
            print 'MSP432: PCMoffline', e
        finally:
            file.close()
        

        # import wave
        # wavfile =  wave.open('c:/1.wav', 'wb')
        # wavfile.setparams((1, 2, self.rate, 0, 'NONE', 'NONE'))
        # try:
        #     while True:
        #         pcmdata = self.ser.read(1024)
        #         hexShow(pcmdata)
        #         wavfile.writeframesraw(pcmdata)
        # except Exception as e:
        #     print 'MSP432: PCMoffline', e

        # finally:
        #     wavfile.close()

    def stopPCM(self):
        self.ser.write('ACK=pcmoff')




        






class Wnd(Frame):
    """docstring for Wnd"""
    def __init__(self, master=None):
        Frame.__init__(self, master, height = 600, width = 400)
        self.grid()
        self.createWidgets()
        self.master.title("MSP432 Autio FFT Display")
        self.master.maxsize(600, 400)
        self.lines = []
        for i in xrange(256):
            self.lines.append(self.cavs.create_line(i,127,i,126,fill='black'))
 

    def createWidgets(self):
        self.cavs = Canvas(self, bg = '#FFFFFF', \
            borderwidth=1, height = 128, width = 256)
        self.cavs.grid()

        self.BtnChSample1 = Button(self, text='Rate 8000',
            command=lambda: msp432.setSamplingRate(8000))
        self.BtnChSample1.grid()

        self.BtnChSample2 = Button(self, text='Rate 16000',
            command=lambda: msp432.setSamplingRate(16000))
        self.BtnChSample2.grid()

        self.BtnChSample3 = Button(self, text='Rate 32000',
            command=lambda: msp432.setSamplingRate(32000))
        self.BtnChSample3.grid()

        self.quitButton = Button(self, text='Quit',
            command=self.quit)
        self.quitButton.grid()


    def updateDataFFT(self):
        s = msp432.get512data()
        hexShow(s)
        # print '\n'
        for i in xrange(256):
            # x = ord(s[2*i]) + 256*ord(s[2*i+1])
            y = ord(s[2*i])     + 256 * ord(s[2*i + 1])
            y = y / 4

            self.cavs.coords(self.lines[i], i, 127-y,  i, 127)
            
            # self.cavs.create_line(i*2,0,i*2,128-(ord(s[i]) + ord(s[i+1]))/4,fill='white')
            # self.cavs.create_line(i*2,128-(ord(s[i])+ord(s[i+1]))/4,i*2,128,fill='black')
            # self.cavs.create_line(i*2+1,0,i*2+1,128-(ord(s[i]) + ord(s[i+1]))/4,fill='white')
            # self.cavs.create_line(i*2+1,128-(ord(s[i])+ord(s[i+1]))/4,i*2+1,128,fill='black')
        self.after(80,self.updateDataFFT)

    def updateData(self):
        #msp432.readPCMtoWave()
        #self.quit()
        self.updateDataFFT()


       


def hexShow(argv):    
    result = ''    
    hLen = len(argv)    
    for i in xrange(hLen):    
        hvol = ord(argv[i])    
        hhex = '%02x'%hvol    
        result += hhex+' '    
    print 'hexShow:',result    


msp432 = MSP432()

def main():
    # print msp432.getPortName()

    wnd = Wnd()

    
    wnd.after(100,wnd.updateData)
    wnd.mainloop()


if __name__ == '__main__':
    main()