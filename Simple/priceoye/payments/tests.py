from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from payments.models import Payment, Invoice
from accounts.models import CustomUser
from orders.models import Order, OrderDetail
from shop.models import Product
from brands.models import Brand
from categories.models import Category

# TESTS for PAYMENT APIs - INCOMPLETE
# class PaymentTest(APITestCase):
#     #POST REQUEST
#     def test_post_payment(self):
#         self.customer = CustomUser.objects.create(
#             username = 'Muzamil',
#             first_name = 'Muhammad',
#             last_name = "Muzamil",
#             email = 'muzamil@gmail.com'
#         )
#         view_name = 'Payments-list'
#         url = reverse(view_name)
#         data = {
#             'amount' : '10000.00',
#             'timestamp': 'Sun,17 Dec 2023 13:54:32 GMT',
#             'success': True,
#             'user': f'{self.customer.id}'
#         }
#         reponse = self.client.post(url, data, format = 'json')
#         self.assertEqual(reponse.status_code, status.HTTP_201_CREATED)

#     #GET REQUEST LIST
#     def test_get_payment_list(self):
#         self.customer = CustomUser.objects.create(
#             username = 'Muzamil',
#             first_name = 'Muhammad',
#             last_name = "Muzamil",
#             email = 'muzamil@gmail.com'
#         )
#         view_name = 'Payments-list'
#         url = reverse(view_name)
#         data = {
#             'amount' : '10000.00',
#             'timestamp': 'Sun,17 Dec 2023 13:54:32 GMT',
#             'success': True,
#             'user': f'{self.customer.id}'
#         }
#         reponse = self.client.post(url, data, format = 'json')
#         reponse = self.client.get(url)
#         self.assertEqual(reponse.status_code, status.HTTP_200_OK)
#         self.assertEqual(len(reponse.data), 1)

#     #GET REQUEST
#     def test_get_payment_list(self):
#         self.customer = CustomUser.objects.create(
#             username = 'Muzamil',
#             first_name = 'Muhammad',
#             last_name = "Muzamil",
#             email = 'muzamil@gmail.com'
#         )
#         self.payment = Payment.objects.create(
#             amount = 10000,
#             timestamp = 'Sun,17 Dec 2023 13:54:32 GMT',
#             success = True,
#             user = self.customer 
#         )
#         payment_id = self.payment.id
#         view_name = 'Payments-detail'
#         url = reverse(view_name, args=[payment_id])
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data['success'], True)
        
# TEST CASES FOR INVOICE APIs - COMPLETE
class InvoiceTest(APITestCase):
    # SETTING UP TEMP OBJECTS
    def setUp(self):
        # Create a superuser for testing
        self.superuser = CustomUser.objects.create_superuser('admin', 'admin@example.com', 'adminpassword')
        login_success = self.client.login(email='admin@example.com', password='adminpassword')
        # Check if the login was successful
        self.assertTrue(login_success)
        self.category = Category.objects.create(name = 'Mobiles')
        self.brand = Brand.objects.create(name = 'Apple')
        self.product = Product.objects.create(
            name = 'iPhone 15 Pro',
            description = 'NEW',
            price = 500000,
            stock_quantity = 20,
            brand = self.brand,
            category = self.category,
        )
        
        self.customer = CustomUser.objects.create(
            username = 'Muzamil',
            first_name = 'Muhammad',
            last_name = 'Muzamil',
            email = 'muzamil@gmail.com'
        )

        self.order = Order.objects.create(
            # order_details = self.order_details,
            order_date = 'Sun,17 Dec 2023 13:54:32 GMT',
            total_amount = self.product.price + 1000,
            user = self.customer,
        )
        self.order_details = OrderDetail.objects.create(
            quantity = 1,
            subtotal = self.product.price,
            order = self.order,
            product = self.product,
        )

        self.payment = Payment.objects.create(
            amount = self.order.total_amount,
            timestamp = 'Sun,17 Dec 2023 13:54:32 GMT',
            success = True,
            user = self.customer
        )

    #TEST POST REQUEST
    def test_post_invoice(self):
        view_name = 'Invoice-list'
        url = reverse(view_name)
        data = {
            'amount' : f'{self.payment.amount}',
            'order' : f'{self.order.id}',
            'payment' : f'{self.payment.id}'
        }
        response = self.client.post(url, data, response = "json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    #TEST GET REQUEST LIST
    def test_get_invoice_list(self):
        view_name = 'Invoice-list'
        url = reverse(view_name)
        data = {
            'amount' : f'{self.payment.amount}',
            'order' : f'{self.order.id}',
            'payment' : f'{self.payment.id}'
        }
        self.client.post(url, data, response = "json")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    #TEST GET REQUEST by ID
    def test_get_invoice(self):
        self.invoice = Invoice.objects.create(
            amount = 500000.0,
            order = self.order,
            payment = self.payment
        )
        invoice_id = self.invoice.id
        view_name = 'Invoice-detail'
        url = reverse(view_name, args=[invoice_id])
        self.client.get(url)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # self.assertEqual(response.data['amount'], f'{float(self.invoice.amount)}')
        self.assertEqual(response.data['order'], self.order.id)
        self.assertEqual(response.data['payment'], self.payment.id)

    #TEST PUT REQUEST by ID
    def test_put_invoice(self):
        self.invoice = Invoice.objects.create(
            amount = 500000.0,
            order = self.order,
            payment = self.payment
        )
        data = {
            'amount' : 510000.0,
            'order' : f'{self.order.id}',
            'payment' : f'{self.payment.id}'
        }
        invoice_id = self.invoice.id
        view_name = 'Invoice-detail'
        url = reverse(view_name, args=[invoice_id])
        response = self.client.put(url, data, format = 'json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # self.assertEqual(response.data['amount'], f'{float(self.invoice.amount)}')
        self.assertEqual(response.data['order'], self.order.id)
        self.assertEqual(response.data['payment'], self.payment.id)

    #TEST DELETE REQUEST by ID
    def test_delete_invoice(self):
        self.invoice = Invoice.objects.create(
            amount = 500000.0,
            order = self.order,
            payment = self.payment
        )
        invoice_id = self.invoice.id
        view_name = 'Invoice-detail'
        url = reverse(view_name, args=[invoice_id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        with self.assertRaises(Invoice.DoesNotExist):
            Invoice.objects.get(id = invoice_id)