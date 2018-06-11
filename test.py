import unittest
from malyDom import malyDomek

class TestmalyDomek(unittest.TestCase):
  
  def testMalyDomExist(self):
    malyDomTemp = malyDomek()
  
  def testRozbroj(self):
    malyDomTemp = malyDomek()
    malyDomTemp.Rozbroj()
    self.assertEqual(malyDomTemp.uzbrojony, False)
    self.assertEqual(malyDomTemp.wlasnieUzbroilem, True)
    self.assertEqual(malyDomTemp.buzzer.read(), 0)
  
  def testUzbroj(self):
    malyDomTemp = malyDomek()
    malyDomTemp.Uzbroj()
    self.assertEqual(malyDomTemp.uzbrojony, True)
    self.assertEqual(malyDomTemp.wlasnieUzbroilem, True)

  def testSprawdzTemperatureZimno(self):
    temperatura1 = 300
    malyDomTemp = malyDomek()
    malyDomTemp.SprawdzTemperature(temperatura1)
    self.assertEqual(malyDomTemp.diodaBiala.read(), 1)
    self.assertEqual(malyDomTemp.diodaZielona.read(), 0)
    self.assertEqual(malyDomTemp.diodaCzerwona.read(), 0)
  def testSprawdzTemperatureOpty(self):
    temperatura = 400
    malyDomTemp = malyDomek()
    malyDomTemp.SprawdzTemperature(temperatura)
    self.assertEqual(malyDomTemp.diodaBiala.read(), 0)  
    self.assertEqual(malyDomTemp.diodaZielona.read(), 1)
    self.assertEqual(malyDomTemp.diodaCzerwona.read(),0)

  def testSprawdzTemperatureCieplo(self):
    temperatura = 600
    malyDomTemp = malyDomek()
    malyDomTemp.SprawdzTemperature(temperatura)
    self.assertEqual(malyDomTemp.diodaZielona.read(), 0)
    self.assertEqual(malyDomTemp.diodaCzerwona.read(), 1)
    self.assertEqual(malyDomTemp.diodaBiala.read(), 0)

  def testWyj(self):
    malyDomTemp = malyDomek()
    malyDomTemp.Wyj()
    self.assertEqual(malyDomTemp.buzzer.read(), 1)
    self.assertEqual(malyDomTemp.alarmTrwa, True)

if __name__=="__main__":
  unittest.main()
