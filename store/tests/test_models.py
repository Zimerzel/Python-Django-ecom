from django.test import TestCase

from store.models import Category, Product

class TestCategoriesModel(TestCase):

    def setUp(self) -> None:
        def setUp(self):
            self.data1 = Category.objects.create(name='shirts', slug='shirts')

        def test_category_model_entry(self):
            data =self.data1
            self.assertTrue(isinstance(data, Category))

        def test_category_model_return(self):
            data =self.data1
            self.assertEqual(str(data), 'shirt')
