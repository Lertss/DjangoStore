from django.test import TestCase
from .models import Product

class ProductModelTest(TestCase):

    def setUp(self):
        # Create a test product
        self.product = Product.objects.create(
            name="Test Product",
            price=100,
            description="Test description",
            image="images/test_image.jpg"
        )

    def test_product_creation(self):
        """Test to check product creation"""
        self.assertEqual(self.product.name, "Test Product")
        self.assertEqual(self.product.price, 100)
        self.assertEqual(self.product.description, "Test description")
        self.assertEqual(self.product.image, "images/test_image.jpg")

    def test_product_str_representation(self):
        """Test to verify the __str__ method"""
        self.assertEqual(str(self.product), "Test Product")

    def test_product_max_length_constraints(self):
        """Test to check max_length constraints for fields"""
        name_max_length = Product._meta.get_field('name').max_length
        description_max_length = Product._meta.get_field('description').max_length
        self.assertEqual(name_max_length, 100)
        self.assertEqual(description_max_length, 200)

    def test_blank_image_field(self):
        """Test to ensure the image field can be left blank"""
        product_without_image = Product.objects.create(
            name="No Image Product",
            price=200,
            description="Product without image"
        )
        self.assertEqual(product_without_image.image, "")

