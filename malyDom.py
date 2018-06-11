import mraa
import time
import math
class malyDomek:
    
    def __init__(self):
        self.uzbrojony = False
        self.alarmTrwa = False
        self.wlasnieUzbroilem = False
        self.dotyk = mraa.Gpio(5)
        self.btn = mraa.Gpio(3)
        self.diodaCzerwona = mraa.Gpio(6)
        self.diodaZielona = mraa.Gpio(7)
        self.diodaBiala = mraa.Gpio(2)
        self.temperatura = mraa.Aio(0)
        self.buzzer = mraa.Gpio(8)
        self.diodaBiala.dir(mraa.DIR_OUT)
        self.diodaZielona.dir(mraa.DIR_OUT)
        self.diodaCzerwona.dir(mraa.DIR_OUT)
        self.diodaBiala.dir(mraa.DIR_OUT)
        self.diodaZielona.dir(mraa.DIR_OUT)
        self.diodaCzerwona.dir(mraa.DIR_OUT)
        self.btn.dir(mraa.DIR_IN)
        self.dotyk.dir(mraa.DIR_IN)  
        self.buzzer.dir(mraa.DIR_OUT)
       
    def Rozbroj(self):
        self.uzbrojony = False
        self.wlasnieUzbroilem = True
        print("rozbrojony")
     
    def Uzbroj(self):
        print("uzbrojony")
        self.uzbrojony = True
        self.wlasnieUzbroilem = True
 
    def Cos(self):
        self.wlasnieUzbroilem = False
     
    def SprawdzTemperature(self, W):      
        B = 4255
        #W = self.temperatura.read()
        resistance = (1023-W)*10000/W
        temp = 1/(math.log(resistance/10000)/B+1/298.15)-273.15
        tem = 1023/W-1
        R = 100000.0*tem
        tem2 = 1/(math.log(R/100000)/B+1/298.15)-273.15
        #print(tem2)
        #temp = W
        if(temp>=0 and temp<=15):
            print("zimno")
            self.diodaBiala.write(1)
            self.diodaCzerwona.write(0)
            self.diodaZielona.write(0)
        if(temp>=16 and temp<=25):
            self.diodaZielona.write(1)
            self.diodaBiala.write(0)
            self.diodaCzerwona.write(0)
            print("optymalnie")
        if (temp>=26 and temp<=50):
            self.diodaCzerwona.write(1)
            self.diodaZielona.write(0)
            self.diodaBiala.write(0)
   
 
    def Wyj(self):  
        self.buzzer.write(1)
        self.alarmTrwa = True
 
 
    def Odpal(self):
         
        while True:
            if(self.uzbrojony==False):
                self.buzzer.write(0)
            self.SprawdzTemperature()
            if(self.dotyk.read() != 0 and self.uzbrojony == False and self.wlasnieUzbroilem == False):
                self.Uzbroj()
            if (self.dotyk.read()!=0 and self.wlasnieUzbroilem == False):
                self.Rozbroj()
            if(self.dotyk.read()==0 and self.wlasnieUzbroilem == True):
                self.Cos()
            if(self.btn.read() != 0 and self.alarmTrwa == False):
                self.Wyj()
 
#wywolanie = malyDomek()
#wywolanie.Odpal() 
