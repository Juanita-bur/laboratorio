from django.test import TestCase
from django.urls import reverse
from .models import Laboratorio

class LaboratorioModelTest(TestCase):
    def setUp(self):
        Laboratorio.objects.create(nombre='Lab Test')

    def test_nombre_label(self):
        lab = Laboratorio.objects.get(id=1)
        field_label = lab._meta.get_field('nombre').verbose_name
        self.assertEqual(field_label, 'nombre')

class LaboratorioListViewTest(TestCase):
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/laboratorio/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('laboratorio_list'))
        self.assertEqual(response.status_code, 200)
    
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('laboratorio_list'))
        self.assertTemplateUsed(response, 'laboratorio/laboratorio_list.html')

class LaboratorioDetailViewTest(TestCase):
    def setUp(self):
        Laboratorio.objects.create(nombre='Lab Test')

    def test_view_url_exists_at_desired_location(self):
        lab = Laboratorio.objects.get(id=1)
        response = self.client.get('/laboratorio/{}/'.format(lab.id))
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        lab = Laboratorio.objects.get(id=1)
        response = self.client.get(reverse('laboratorio_detail', args=[lab.id]))
        self.assertEqual(response.status_code, 200)
    
    def test_view_uses_correct_template(self):
        lab = Laboratorio.objects.get(id=1)
        response = self.client.get(reverse('laboratorio_detail', args=[lab.id]))
        self.assertTemplateUsed(response, 'laboratorio/laboratorio_detail.html')

class LaboratorioCreateViewTest(TestCase):
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/laboratorio/nuevo/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('laboratorio_create'))
        self.assertEqual(response.status_code, 200)
    
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('laboratorio_create'))
        self.assertTemplateUsed(response, 'laboratorio/laboratorio_form.html')
