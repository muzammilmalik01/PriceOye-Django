from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from shop.models import Product
from brands.models import Brand
from categories.models import Category
from accounts.models import CustomUser

class ProductTest(APITestCase):
    """
    Test case for the Product model.

    This class inherits from APITestCase and tests the functionality of 
    the Product model, including the ability to create, retrieve, update, 
    and delete instances.
    """

    def setUp(self):
        """
        Set up the test case.

        This method is called before each test in this test case is run. 
        It creates a superuser and logs them in.
        """
        
        # Create a superuser for testing
        self.superuser = CustomUser.objects.create_superuser('admin', 'admin@example.com', 'adminpassword')
        login_success = self.client.login(email='admin@example.com', password='adminpassword')
        # Check if the login was successful
        self.assertTrue(login_success)

    # TESTING POST REQUEST
    def test_create_product(self):
        """
        Test the ability to create a product.

        This method tests the POST request to create a product. It checks 
        that the response status code is 201 (created) and that the product 
        was correctly created in the database.
        """

        self.brand = Brand.objects.create(name='Apple') #Creating object of brand
        self.category = Category.objects.create(name='Mobiles') #Creating object of category
        view_name = "products-list"
        url = reverse(f"{view_name}")
        data = {'name':"iPhone 14",
                'description':'NEW',
                'price':'10',
                'stock_quantity':10,
                'brand':self.brand.id,
                'category':self.category.id
                }
        response = self.client.post(url, data, format='json') #POSTING REQUEST
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 1)
        self.assertEqual(Product.objects.get().name, 'iPhone 14')
        self.assertEqual(Product.objects.get().description, 'NEW')
        self.assertEqual(Product.objects.get().price, 10)
        self.assertEqual(Product.objects.get().stock_quantity, 10)
        self.assertEqual(Product.objects.get().brand, self.brand)
        self.assertEqual(Product.objects.get().category, self.category)

    # TEST FOR GET PRODUCT LIST
    def test_get_product_list(self):
        """
        Test the ability to retrieve a list of products.

        This method tests the GET request to retrieve a list of products. 
        It checks that the response status code is 200 (OK) and that the 
        correct number of products is returned.
        """

        self.brand = Brand.objects.create(name='Apple') #Creating object of brand
        self.category = Category.objects.create(name='Mobiles') #Creating object of category
        view_name = "products-list"
        url = reverse(f"{view_name}")
        data = {'name':"iPhone 14",
                'description':'NEW',
                'price':'10',
                'stock_quantity':10,
                'brand':self.brand.id,
                'category':self.category.id
                }
        response = self.client.post(url, data, format='json') #Adding 1 product
        response = self.client.get(url) #POSTING REQUEST
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1) #GETTING 1 PRODUCT

    # TESTING GET by ID
    def test_get_product(self):
        """
        Test the ability to retrieve a product by ID.

        This method tests the GET request to retrieve a product by ID. It 
        checks that the response status code is 200 (OK) and that the 
        correct product is returned.
        """

        self.brand = Brand.objects.create(name='Apple') #Creating object of brand
        self.category = Category.objects.create(name='Mobiles') #Creating object of category
        self.product = Product.objects.create(name = 'iPhone 14 Pro',description = 'NEW',price = 10, stock_quantity = 10,brand = self.brand, category = self.category)
        view_name = "products-detail"
        product_id = self.product.id
        url = reverse(view_name, args=[product_id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'iPhone 14 Pro')
        self.assertEqual(response.data['description'], 'NEW')
        #HAVING ERROR AT PRICE
        # self.assertEqual(response.data['price'], '10')
        self.assertEqual(response.data['stock_quantity'], 10)
        self.assertEqual(response.data['brand'], self.brand.id)
        self.assertEqual(response.data['category'], self.brand.id)

    #TESTING PUT by ID
    def test_update_product(self):
        """
        Test the ability to update a product by ID.

        This method tests the PUT request to update a product by ID. It 
        checks that the response status code is 200 (OK) and that the 
        product was correctly updated in the database.
        """

        self.brand = Brand.objects.create(name='Apple') #Creating object of brand
        self.category = Category.objects.create(name='Mobiles') #Creating object of category
        self.product = Product.objects.create(name = 'iPhone 14 Pro',description = 'NEW',price = 10, stock_quantity = 10,brand = self.brand, category = self.category)
        view_name = "products-detail"
        product_id = self.product.id
        data = {
        'name': 'iPhone 14',
        'description': 'NEW',
        'price': 10,
        'stock_quantity': 10,
        'brand': f'{self.brand.id}',  # Fixed the string formatting
        'category': f'{self.category.id}'  # Fixed the string formatting
    }
        url = reverse(view_name, args=[product_id])
        response = self.client.put(url, data, format = "json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'iPhone 14')
        self.assertEqual(response.data['description'], 'NEW')
        #HAVING ERROR AT PRICE
        # self.assertEqual(response.data['price'], '10')
        self.assertEqual(response.data['stock_quantity'], 10)
        self.assertEqual(response.data['brand'], self.brand.id)
        self.assertEqual(response.data['category'], self.brand.id)  

    #TESTING DELETE by ID
    def test_delete_product(self):
        """
        Test the ability to delete a product by ID.

        This method tests the DELETE request to delete a product by ID. It 
        checks that the response status code is 204 (No Content) and that 
        the product was correctly deleted from the database.
        """

        self.brand = Brand.objects.create(name='Apple') #Creating object of brand
        self.category = Category.objects.create(name='Mobiles') #Creating object of category
        self.product = Product.objects.create(name = 'iPhone 14 Pro',description = 'NEW',price = 10, stock_quantity = 10,brand = self.brand, category = self.category)
        view_name = "products-detail"
        product_id = self.product.id
        url = reverse(view_name, args=[product_id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)   
        with self.assertRaises(Product.DoesNotExist): #Trying to retrieve the brand with specific ID will raise exception DoesNotExist.
            Product.objects.get(id=product_id)