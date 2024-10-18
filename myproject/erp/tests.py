from django.test import TestCase
from .models import Fabrica, Producto

class FabricaModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Fabrica.objects.create(nombre="Fábrica A", pais="Ubicación A")

    def test_model_content_fabrica(self):
        fabrica = Fabrica.objects.get(id=1)
        self.assertEqual(fabrica.nombre, "Fábrica A")
        self.assertEqual(fabrica.pais, "Ubicación A")

class ProductoModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Producto.objects.create(nombre="Producto A", costo=100)

    def test_model_content_producto(self):
        producto = Producto.objects.get(id=1)
        self.assertEqual(producto.nombre, "Producto A")
        self.assertEqual(producto.costo, 100)

    def test_producto_url_status_code(self):
        response = self.client.get('/producto/')
        self.assertEqual(response.status_code, 200)

    def test_mostrar_pro_url(self):
        response = self.client.get('/mostrar-pro/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'nombre_de_la_plantilla.html')
        self.assertContains(response, "Información de Productos")