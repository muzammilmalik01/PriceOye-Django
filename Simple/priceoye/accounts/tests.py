from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from accounts.models import CustomUser

class AccountTest(APITestCase):
    """
    Test case for the Account model.

    This class inherits from APITestCase and tests the CRUD operations 
    (Create, Retrieve, Update, Delete) of the Account model.

    Methods:
        setUp: Set up the test environment.
        test_create_account: Test the creation of an account.
        test_get_account_list: Test retrieving a list of accounts.
        test_get_account: Test retrieving a specific account by ID.
        test_put_account: Test updating a specific account by ID.
        test_delete_account: Test deleting a specific account by ID.
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
    def test_create_account(self):
        """
        Test the creation of an account.

        This method tests the POST request to create an account, checking 
        that the response status code is 201 (created) and that the account 
        details are correct.
        """
        view_name = "customusers-list"
        url = reverse(view_name)
        data = {
            'username' : 'Muzamil',
            'email' : 'muzamil@gmail.com',
            'first_name' : 'Muhammad', 
            'last_name': 'Muzamil'
        }
        response = self.client.post(url,data,format = "json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CustomUser.objects.count(),1)
        self.assertEqual(CustomUser.objects.get().username,'Muzamil')
        self.assertEqual(CustomUser.objects.get().first_name,'Muhammad')
        self.assertEqual(CustomUser.objects.get().last_name,'Muzamil')
        self.assertEqual(CustomUser.objects.get().email,'muzamil@gmail.com')

    # TESTING GET LIST REQUEST
    def test_get_account_list(self):
        """
        Test retrieving a list of accounts.

        This method tests the GET request to retrieve a list of accounts, 
        checking that the response status code is 200 (OK) and that the 
        number of accounts is correct.
        """
        view_name = "customusers-list"
        url = reverse(view_name)
        data = {
            'username' : 'Muzamil',
            'email' : 'muzamil@gmail.com',
            'first_name' : 'Muhammad', 
            'last_name': 'Muzamil'
        }
        response = self.client.post(url, data, format="json")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data),1)

    # TESTING GET ACCOUNT by ID REQUEST
    def test_get_account(self):
        """
        Test retrieving a specific account by ID.

        This method tests the GET request to retrieve a specific account by 
        ID, checking that the response status code is 200 (OK) and that the 
        account details are correct.
        """
        self.account = CustomUser.objects.create(username = 'Muzamil',first_name = 'Muhammad', last_name = 'Muzamil', email = 'muzamil@gmail.com')
        view_name = "customusers-detail"
        account_id = self.account.id
        url = reverse(view_name, args=[account_id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(CustomUser.objects.get().username, self.account.username)
        self.assertEqual(CustomUser.objects.get().first_name, self.account.first_name)
        self.assertEqual(CustomUser.objects.get().last_name, self.account.last_name)
        self.assertEqual(CustomUser.objects.get().email, self.account.email)

    # TESTING PUT ACCOUNT by ID REQUEST
    def test_put_account(self):
        """
        Test updating a specific account by ID.

        This method tests the PUT request to update a specific account by 
        ID, checking that the response status code is 200 (OK) and that the 
        updated account details are correct.
        """
        self.account = CustomUser.objects.create(username = 'Muzamil',first_name = 'Muhammad', last_name = 'Muzamil', email = 'muzamil@gmail.com')
        view_name = "customusers-detail"
        account_id = self.account.id
        data = {
            'username' : 'Muzamil',
            'email' : 'muzamil@proton.com',
            'first_name' : 'Muhammad', 
            'last_name': 'Muzamil'
        } # Updated the email here.
        url = reverse(view_name, args=[account_id])
        response = self.client.put(url, data, response = 'json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(CustomUser.objects.get().username, self.account.username)
        self.assertEqual(CustomUser.objects.get().first_name, self.account.first_name)
        self.assertEqual(CustomUser.objects.get().last_name, self.account.last_name)
        self.assertEqual(CustomUser.objects.get().email, "muzamil@proton.com") #TESTING UPDATED EMAIL    

    # TESTING DELETE ACCOUNT by ID REQUEST
    def test_delete_account(self):
        """
        Test deleting a specific account by ID.

        This method tests the DELETE request to delete a specific account by 
        ID, checking that the response status code is 204 (No Content) and 
        that the account no longer exists.
        """
        self.account = CustomUser.objects.create(username = 'Muzamil',first_name = 'Muhammad', last_name = 'Muzamil', email = 'muzamil@gmail.com')
        view_name = "customusers-detail"
        account_id = self.account.id
        url = reverse(view_name, args=[account_id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        with self.assertRaises(CustomUser.DoesNotExist): #Trying to retrieve the brand with specific ID will raise exception DoesNotExist.
            CustomUser.objects.get(id=account_id)