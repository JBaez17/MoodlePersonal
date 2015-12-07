# -*- coding: utf-8 -*-
from lettuce import step, world
from selenium import webdriver


# scenario 1
@step(u'When Oprimo la tecla Enter')
def when_oprimo_la_tecla_enter(step):
    assert True


@step(u'Given Que ingreso en el navegador la url "([^"]*)" en la barra de direcciones')
def given_que_ingreso_en_el_navegador_la_url_urlDjango_en_la_barra_de_direcciones(step, urlDjango):
    world.driver = webdriver.Firefox()
    world.driver.get(urlDjango)


@step(u'Then Puedo ver en el titulo del navegador la palabra "([^"]*)".')
def then_puedo_ver_en_el_titulo_del_navegador_la_palabra_browserTitle(step, browserTitle):
    assert browserTitle in world.driver.title
