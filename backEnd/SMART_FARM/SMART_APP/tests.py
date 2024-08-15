from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Product, Cart, CartItem

User = get_user_model()

class UserModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='testuser@example.com', password='testpass123')

    def test_user_creation(self):
        self.assertEqual(self.user.username, 'testuser')
        self.assertEqual(self.user.email, 'testuser@example.com')
        self.assertFalse(self.user.is_premium)

class ProductModelTest(TestCase):

    def setUp(self):
        self.product = Product.objects.create(name='Test Product', description='A test product', price=19.99, stock=100)

    def test_product_creation(self):
        self.assertEqual(self.product.name, 'Test Product')
        self.assertEqual(self.product.description, 'A test product')
        self.assertEqual(self.product.price, 19.99)
        self.assertEqual(self.product.stock, 100)

class CartModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='testuser@example.com', password='testpass123')
        self.product = Product.objects.create(name='Test Product', description='A test product', price=19.99, stock=100)
        self.cart = Cart.objects.create(user=self.user)

    def test_cart_creation(self):
        self.assertEqual(self.cart.user, self.user)
        self.assertEqual(self.cart.products.count(), 0)  # No products added yet

    def test_adding_product_to_cart(self):
        cart_item = CartItem.objects.create(cart=self.cart, product=self.product, quantity=2)
        self.cart.products.add(self.product)
        self.assertEqual(self.cart.products.count(), 1)
        self.assertEqual(cart_item.quantity, 2)
        self.assertEqual(cart_item.product, self.product)

class CartItemModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='testuser@example.com', password='testpass123')
        self.product = Product.objects.create(name='Test Product', description='A test product', price=19.99, stock=100)
        self.cart = Cart.objects.create(user=self.user)
        self.cart_item = CartItem.objects.create(cart=self.cart, product=self.product, quantity=3)

    def test_cart_item_creation(self):
        self.assertEqual(self.cart_item.cart, self.cart)
        self.assertEqual(self.cart_item.product, self.product)
        self.assertEqual(self.cart_item.quantity, 3)
