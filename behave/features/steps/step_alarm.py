from behave import given, when, then, step
from malyDom import malyDomek
@given('smartHome, alarm wylaczony, touch nie przycisniety, button nie przycisniety')
def step_impl(context):
    context.malyDom = malyDomek()

@when('touch przycisniety')
def step_impl(context):
    context.malyDom.Wyj()

@then('wlacz alarm')
def step_impl(context):
    assert context.malyDom.alarmTrwa is True
@given('smartHome, alarm rozbrojony, przycisk nie przycisniety')
def step_impl(context):
    context.malyDom = malyDomek()

@when('przycisk zostal wcisniety')
def step_impl(context):
    context.malyDom.Uzbroj()

@then('uzbroj alarm')
def step_impl(context):
    assert context.malyDom.uzbrojony is True
    assert context.malyDom.wlasnieUzbroilem is True
    
@given('smartHome, alarm nie trwa')
def step_impl(context):
    context.malyDom = malyDomek()

@when('przycisk przycisniety')
def step_impl(context):
    context.malyDom.Wyj()

@then('syrena wyje')
def step_impl(context):
    assert context.malyDom.buzzer.read() is 1
    
#temperatury    

@given('smartHome')
def step_impl(context):
    context.malyDom = malyDomek()

@when('czujnik odczyta temperature ponizej 15')
def step_impl(context):
    t=300
    context.malyDom.SprawdzTemperature(t)


@then('zapal biala diode')
def step_impl(context):
    assert context.malyDom.diodaBiala.read() is 1
    assert context.malyDom.diodaZielona.read() is 0
    assert context.malyDom.diodaCzerwona.read() is 0
    
@given('smartHome')
def step_impl(context):
    context.malyDom = malyDomek()

@when('czujnik odczyta temperature miedzy 16 a 25')
def step_impl(context):
    t=400
    context.malyDom.SprawdzTemperature(t)

@then('zapal zielona diode')
def step_impl(context):
    assert context.malyDom.diodaBiala.read() is 0
    assert context.malyDom.diodaZielona.read() is 1
    assert context.malyDom.diodaCzerwona.read() is 0

    
@given('smartHome')
def step_impl(context):
    context.malyDom = malyDomek()

@when('czujnik odczyta temperature miedzy 26 a 50')
def step_impl(context):
    t=600
    context.malyDom.SprawdzTemperature(t)


@then('zapal czerwona diode')
def step_impl(context):
    assert context.malyDom.diodaBiala.read() is 0
    assert context.malyDom.diodaZielona.read() is 0
    assert context.malyDom.diodaCzerwona.read() is 1