Feature: Wlaczanie syreny
	Scenario: Alarm
		Given smartHome, alarm wylaczony, touch nie przycisniety, button nie przycisniety
		When touch przycisniety
		Then wlacz alarm
	Scenario: Alarm
		Given smartHome, alarm rozbrojony, przycisk nie przycisniety
		When przycisk zostal wcisniety
		Then uzbroj alarm
    Scenario: Alarm
		Given smartHome, alarm nie trwa
		When przycisk przycisniety
		Then syrena wyje             
    Scenario: Alarm
		Given smartHome
		When czujnik odczyta temperature ponizej 15
		Then zapal biala diode     
	Scenario: Alarm
		Given smartHome
		When czujnik odczyta temperature miedzy 16 a 25
		Then zapal zielona diode 
    Scenario: Alarm
		Given smartHome
		When czujnik odczyta temperature miedzy 26 a 50
		Then zapal czerwona diode
