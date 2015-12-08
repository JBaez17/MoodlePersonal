from django.core.urlresolvers import resolve
from django.template.loader import render_to_string
from django.test import TestCase
from django.http import HttpRequest
from Examen.views import ver_examenes


class TestExamenes(TestCase):

    def test_url_ver_examenes_resuelve_hacia_ver_examenes(self):
        found = resolve('/Examen/ver_examenes/')
        self.assertEqual(found.func, ver_examenes)

    def test_ver_examenes_retorna_el_html_correcto(self):
        request = HttpRequest()
        response = ver_examenes(request)
        esperado = render_to_string('Examen/ver_examenes.html')
        self.assertEqual(response.content.decode(), esperado)
