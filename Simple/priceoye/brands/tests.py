from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from brands.models import Brand
from accounts.models import CustomUser

class BrandTests(APITestCase):
    """
    Test cases for the Brand API.

    Each method represents a specific test scenario.
    """
    def setUp(self):
    # Create a superuser for testing
        self.superuser = CustomUser.objects.create_superuser('admin', 'admin@example.com', 'adminpassword')
        login_success = self.client.login(email='admin@example.com', password='adminpassword')
        # Check if the login was successful
        self.assertTrue(login_success)

    #TESTING POST REQUEST
    def test_create_brand(self):
        """
        Test creating a new brand using a POST request.

        Ensures that a new brand can be created and is retrievable.
        """
        view_name = 'brand-list'
        url = reverse(f'{view_name}')
        data = {'name': 'OnePlus'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Brand.objects.count(), 1)
        self.assertEqual(Brand.objects.get().name, 'OnePlus')

    #TESTING GET RESPONSE FOR LIST.
    def test_get_brand(self):
        """
        Test retrieving a list of brands using a GET request.

        Ensures that the API returns a list of brands with a 200 status code.
        """
        view_name = 'brand-list'
        url = reverse(f'{view_name}')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), Brand.objects.count())

    #TESTING GET RESPONSE FOR SPECIFIC ID.
    def test_get_brand_detail(self):
        """
        Test retrieving details of a specific brand using a GET request.

        Ensures that the API returns the correct details for a specific brand with a 200 status code.
        """
        self.brand = Brand.objects.create(name='Sony') #create a new instance of brand
        view_name = 'brand-detail'
        brand_id = self.brand.id 
        url = reverse(view_name, args=[brand_id]) #Reverse function to generate the URL
        response = self.client.get(url) #GET Request
        self.assertEqual(response.status_code, status.HTTP_200_OK) #Check for successful response 
        self.assertEqual(response.data['name'], self.brand.name) #Check the new Response received from the API
        self.assertEqual(response.data['id'], self.brand.id) #Check the new Response received from the API

    #TESTING PUT (UPDATING) REQUEST FOR SPECIFIC ID
    def test_update_brand(self):
        """
        Test updating details of a specific brand using a PUT request.

        Ensures that the details of a specific brand can be successfully updated with a 200 status code.
        """
        self.brand = Brand.objects.create(name='Samsung')
        view_name = 'brand-detail'
        brand_id = self.brand.id

        url = reverse(view_name, args=[brand_id])
        data = {'name': 'Apple'}
        response = self.client.put(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Brand.objects.get(id=brand_id).name, 'Apple')

    #TESTING DELETE REQUEST FOR SPECIFIC ID
    def test_delete_brand(self):
        """
        Test deleting a specific brand using a DELETE request.

        Ensures that a specific brand can be successfully deleted with a 204 status code.
        """
        self.brand = Brand.objects.create(name='Samsung')
        view_name = 'brand-detail'
        brand_id = self.brand.id

        url = reverse(view_name, args=[brand_id]) 
        response = self.client.delete(url) #Performing DELETE Request.

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT) #after deleting, NO CONTENT SHOULD BE RECEIVED.
        with self.assertRaises(Brand.DoesNotExist): #Trying to retrieve the brand with specific ID will raise exception DoesNotExist.
            Brand.objects.get(id=brand_id)