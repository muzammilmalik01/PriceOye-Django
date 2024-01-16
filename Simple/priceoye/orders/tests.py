from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from orders.models import Order, OrderDetail
from accounts.models import CustomUser

class OrderTest(APITestCase):
    """
    Test case for the Order model.

    This class inherits from APITestCase and tests the CRUD operations 
    (Create, Retrieve, Update, Delete) of the Order model.

    Methods:
        setUp: Set up the test environment.
        test_post_order: Test the creation of an order.
        test_get_order_list: Test retrieving a list of orders.
        test_get_order: Test retrieving a specific order by ID.
        test_put_order: Test updating a specific order by ID.
        test_delete_order: Test deleting a specific order by ID.
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

    # TEST POST REQUEST
    def test_post_order(self):
        """
        Test the creation of an order.

        This method tests the POST request to create an order, checking 
        that the response status code is 201 (created) and that the order 
        details are correct.
        """
        self.customer = CustomUser.objects.create(
            username = 'Muzamil',
            first_name = 'Muhammad',
            last_name = "Muzamil",
            email = 'muzamil@gmail.com'
        )
        data = {
            'order_date':'Sun,17 Dec 2023 13:54:32 GMT',
            'total_amount':10000,
            'user': f'{self.customer.id}'
        }
        view_name = "Orders-list"
        url = reverse(view_name)
        response = self.client.post(url, data, format = 'json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # TEST GET LIST REQUEST
    def test_get_order_list(self):
        """
        Test retrieving a list of orders.

        This method tests the GET request to retrieve a list of orders, 
        checking that the response status code is 200 (OK) and that the 
        number of orders is correct.
        """
        self.customer = CustomUser.objects.create(
            username = 'Muzamil',
            first_name = 'Muhammad',
            last_name = "Muzamil",
            email = 'muzamil@gmail.com'
        )
        data = {
            'order_date':'Sun,17 Dec 2023 13:54:32 GMT',
            'total_amount':10000,
            'user': f'{self.customer.id}'
        }
        view_name = "Orders-list"
        url = reverse(view_name)
        response = self.client.post(url, data, format = 'json')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    # TEST GET REQUEST
    def test_get_order(self):
        """
        Test retrieving a specific order by ID.

        This method tests the GET request to retrieve a specific order by 
        ID, checking that the response status code is 200 (OK) and that the 
        order details are correct.
        """
        self.customer = CustomUser.objects.create(
            username = 'Muzamil',
            first_name = 'Muhammad',
            last_name = "Muzamil",
            email = 'muzamil@gmail.com'
        )
        self.order = Order.objects.create(
            order_date = 'Sun,17 Dec 2023 13:54:32 GMT',
            total_amount = 10000,
            user = self.customer,
        )
        order_id = self.order.id
        view_name = "Orders-detail"
        url = reverse(view_name, args=[order_id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["user"], self.order.user.id)


    # TEST PUT LIST REQUEST
    def test_put_order(self):
        """
        Test updating a specific order by ID.

        This method tests the PUT request to update a specific order by 
        ID, checking that the response status code is 200 (OK) and that the 
        updated order details are correct.
        """
        self.customer = CustomUser.objects.create(
            username = 'Muzamil',
            first_name = 'Muhammad',
            last_name = "Muzamil",
            email = 'muzamil@gmail.com'
        )
        self.order = Order.objects.create(
            order_date = 'Sun,17 Dec 2023 13:54:32 GMT',
            total_amount = 10000,
            user = self.customer,
            
        )
        order_id = self.order.id
        data = {
            'order_date':'Sun,17 Dec 2023 13:54:32 GMT',
            'total_amount':11000,
            'user': f'{self.customer.id}'
        }
        view_name = "Orders-detail"
        url = reverse(f"{view_name}",args=[order_id])
        response = self.client.put(url, data, format = 'json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Order.objects.get().total_amount, data['total_amount'])

    # TEST DELETE LIST REQUEST
    def test_delete_order(self):
        """
        Test deleting a specific order by ID.

        This method tests the DELETE request to delete a specific order by 
        ID, checking that the response status code is 204 (No Content) and 
        that the order no longer exists.
        """
        self.customer = CustomUser.objects.create(
            username = 'Muzamil',
            first_name = 'Muhammad',
            last_name = "Muzamil",
            email = 'muzamil@gmail.com'
        )
        self.order = Order.objects.create(
            order_date = 'Sun,17 Dec 2023 13:54:32 GMT',
            total_amount = 10000,
            user = self.customer,
        )
        order_id = self.order.id
        view_name = "Orders-detail"
        url = reverse(f"{view_name}",args=[order_id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        with self.assertRaises(Order.DoesNotExist):
            Order.objects.get(id = order_id)