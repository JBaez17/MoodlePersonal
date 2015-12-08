# -*- coding: utf-8 -*-
from lettuce import step, world
from selenium import webdriver
import time


@step(u'Given Que ingreso a la pagina de login con el usuario "([^"]*)", contraseña "([^"]*)"')
def given_que_ingreso_a_la_pagina_de_login_con_el_usuario_group1_contrasena_group1(step, group1, group2):
    world.driver = webdriver.Firefox()
    world.driver.get("10.1.39.175:8000/alumnos")
    usuario = world.driver.find_element_by_id("username")
    usuario.send_keys(group1)
    password = world.driver.find_element_by_id("password")
    password.send_keys(group2)
    btnClick = world.driver.find_element_by_xpath("//*[@type='submit']")
    btnClick.click()
    time.sleep(4)


@step(u'Cuando se muestra la pantalla principal')
def cuando_se_muestra_la_pantalla_principal(step):
    titulo = u'Pantalla Principal Moodle'
    assert titulo in world.driver.title
    time.sleep(5)


@step(u'Entonces Puedo ver las diferentes opciones')
def entonces_puedo_ver_las_diferentes_opciones(step):
    buscador = world.driver.find_element_by_name("csrfmiddlewaretoken")
    world.driver.close()
    time.sleep(4)
