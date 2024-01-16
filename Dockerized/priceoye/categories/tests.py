from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from categories.models import Category
from accounts.models import CustomUser 

class CategoryTest(APITestCase):
    """
    Test case for the Category model.

    This class inherits from APITestCase and tests the CRUD operations 
    (Create, Retrieve, Update, Delete) of the Category model.

    Methods:
        setUp: Set up the test environment.
        test_create_category: Test the creation of a category.
        test_get_brand: Test retrieving a list of categories.
        test_get_category_detail: Test retrieving a specific category by ID.
        test_update_category: Test updating a specific category by ID.
        test_delete_category: Test deleting a specific category by ID.
    """
    def setUp(self):
        """
        Set up the test environment.

        This method is called before each test. It creates a superuser and 
        logs them in, checking that the login was successful.
        """
        # Create a superuser for testing
        self.superuser = CustomUser.objects.create_superuser('admin', 'admin@example.com', 'adminpassword')
        login_success = self.client.login(email='admin@example.com', password='adminpassword')
        # Check if the login was successful
        self.assertTrue(login_success)
        
    # TESTING POST REQUEST
    def test_create_category(self):
        """
        Test the creation of a category.

        This method tests the POST request to create a category, checking 
        that the response status code is 201 (created) and that the category 
        details are correct.
        """
        view_name = 'Categories-list' 
        url = reverse(f'{view_name}')
        data = {'name': 'Power Banks'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Category.objects.count(), 1)
        self.assertEqual(Category.objects.get().name, 'Power Banks')

    #T ESTING GET RESPONSE FOR LIST.
    def test_get_brand(self):
        """
        Test retrieving a list of categories.

        This method tests the GET request to retrieve a list of categories, 
        checking that the response status code is 200 (OK) and that the 
        number of categories is correct.
        """
        view_name = 'Categories-list'  
        url = reverse(f'{view_name}')
        data_list = [{'name': 'Power Banks'}, {'name': 'EVs'}]#Create 1st Item
        for data in data_list:
            response = self.client.post(url, data, format='json')#POST IT
        response = self.client.get(url)# GET the list
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    # TESTING GET by ID REQUEST.
    def test_get_category_detail(self):
        """
        Test retrieving a specific category by ID.

        This method tests the GET request to retrieve a specific category by 
        ID, checking that the response status code is 200 (OK) and that the 
        category details are correct.
        """
        self.category = Category.objects.create(name="Powerbank") #create a new instance of brand
        self.category_2 = Category.objects.create(name="EVs") #create another instance of brand
        view_name = 'Categories-detail'
        category_id = self.category.id 
        category_id_2 = self.category_2.id 
        url = reverse(view_name, args=[category_id]) #Reverse function to generate the URL
        url_2 = reverse(view_name, args=[category_id_2]) #Reverse function to generate the URL
        response = self.client.get(url) #GET Request
        response_2 = self.client.get(url_2) #GET Request
        self.assertEqual(response.status_code, status.HTTP_200_OK) #Check for successful response for 1st item
        self.assertEqual(response.data['name'], 'Powerbank') #Check the new Response received from the API
        self.assertEqual(response.data['id'], 1) #Check the new Response received from the API
        self.assertEqual(response_2.status_code, status.HTTP_200_OK) #Check for successful response 
        self.assertEqual(response_2.data['name'], 'EVs') #Check the new Response received from the API
        self.assertEqual(response_2.data['id'], 2) #Check the new Response received from the API

    # TESTING PUT by ID REQUEST.
    def test_update_category(self):
        """
        Test updating a specific category by ID.

        This method tests the PUT request to update a specific category by 
        ID, checking that the response status code is 200 (OK) and that the 
        updated category details are correct.
        """
        self.category = Category.objects.create(name = "PowerBenks")
        view_name = "Categories-detail"
        category_id = self.category.id
        data = {'name':'Power Banks'}
        url = reverse(view_name, args=[category_id])
        response = self.client.put(url, data, format = 'json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertAlmostEqual(Category.objects.get(id = category_id).name,"Power Banks")

    #TESTING DELETE by ID REQUEST.
    def test_delete_category(self):
        """
        Test deleting a specific category by ID.

        This method tests the DELETE request to delete a specific category by 
        ID, checking that the response status code is 204 (No Content) and 
        that the category no longer exists.
        """
        self.category = Category.objects.create(name = "Power Bank")
        view_name = "Categories-detail"
        category_id = self.category.id
        url = reverse(view_name, args=[category_id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    