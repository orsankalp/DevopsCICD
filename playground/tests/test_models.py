from django.test import TestCase
from playground.models import MVRS_Category,Cars
from django.core.files.uploadedfile import SimpleUploadedFile

class TestModels(TestCase):

    def setUp(self):
        self.category = MVRS_Category.objects.create( MVRS_cat_name = 'Project1',MVRS_cat_description = 'Test' )
        
        self.car_image = SimpleUploadedFile(
            name='test_image.jpg',
            content=b'',  # Here we're using an empty byte string for simplicity
            content_type='image/jpeg'
        )
        self.Cars = Cars.objects.create( MVRS_car_name = 'Project1',MVRS_car_description = 'Test', car_category=self.category,MVRS_car_image=self.car_image )
    def test_MVRS_Category_Test(self):
        self.assertEqual(self.category.MVRS_cat_name, 'Project1')
        self.assertEqual(self.category.MVRS_cat_description, 'Test')
        self.assertEqual(str(self.category), 'Project1')
    def test_MVRS_Cars_Test(self):
        self.assertEqual(self.Cars.MVRS_car_name, 'Project1')
        self.assertEqual(self.Cars.MVRS_car_description, 'Test')
        self.assertEqual(self.Cars.car_category, self.category)
        self.assertTrue(self.Cars.MVRS_car_image.name.startswith('Cars/test_image'))
    