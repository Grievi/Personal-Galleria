from django.test import TestCase
from .models import  Category, Location, Img

class CategoryTestClass (TestCase):

    def setUp(self):
            self.category = Category(name='home')
            self.category.save_category()

    def test_instance(self):
        self.assertTrue(isinstance(self.category, Category))
    def test_save_category(self):
        self.category.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)

    def test_delete_category(self):
        self.category.delete_category()
        category = Category.objects.all()
        self.assertTrue(len(category) == 0)

class TestLocation(TestCase):

    def setUp(self):
        self.location = Location(name='Quala-Lumpa')
        self.location.save_location()
    
    def test_instance(self):
        self.assertTrue(isinstance(self.location, Location)) 

    def test_get_locations(self):
        self.location.save_location()
        locations = Location.get_locations()
        self.assertTrue(len(locations) > 1)

    def test_update_location(self):
        new_location = 'Amazon'
        self.location.update_location(self.location.id, new_location)
        changed_location = Location.objects.filter(name='Amazon')
        self.assertTrue(len(changed_location) > 0)

    def test_save_location(self):
        self.location.save_location()
        locations = Location.get_locations()
        self.assertTrue(len(locations) > 0)

    def test_delete_location(self):
        self.location.delete_location()
        location = Location.objects.all()
        self.assertTrue(len(location) == 0)

class TestImg(TestCase):
    def setUp(self):
        self.location = Location(name='Quala-Lumpa')
        self.location.save_location()
        self.category = Category(name='Destination')
        self.category.save_category()
        self.image_test = Img(id=1, name='summer', description='A serene environment for relaxation', location=self.location,
                                category=self.category)
        
    def test_instance(self):
        self.assertTrue(isinstance(self.image_test, Img))

    def test_save_image(self):
        self.image_test.save_image()
        after = Img.objects.all()
        self.assertTrue(len(after) > 0)

    def test_get_image_by_id(self):
        found_image = self.image_test.get_image_by_id(self.image_test.id)
        image = Img.objects.filter(id=self.image_test.id)
        self.assertTrue(found_image, image)

    def test_search_image_by_category(self):
        category = 'home'
        found_img = self.image_test.search_by_category(category)
        self.assertTrue(len(found_img) > 1)

    def test_search_image_by_location(self):
        self.image_test.save_image()
        found_images = self.image_test.filter_by_location(location='moringa')
        self.assertTrue(len(found_images) == 1)

    def test_update_image(self):
        self.image_test.save_image()
        self.image_test.update_image(self.image_test.id, 'photos/test.jpg')
        changed_img = Img.objects.filter(image='photos/test.jpg')
        self.assertTrue(len(changed_img) > 0)

    def test_delete_image(self):
        self.image_test.delete_image()
        images = Img.objects.all()
        self.assertTrue(len(images) == 0)

    def test_update_image(self):
        self.image_test.save_image()
        self.image_test.update_image(self.image_test.id, 'photos/test.jpg')
        changed_img = Img.objects.filter(image='photos/test.jpg')
        self.assertTrue(len(changed_img) > 0)