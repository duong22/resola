from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from book.models import Book
from rest_framework.test import APITestCase


class UserTestsData:
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(
            email="test_user@email.com",
            username="test_user",
            password="test_user_password",
        )

class BookViewsetTestCase(APITestCase, UserTestsData):

    @classmethod
    def setUpTestData(cls):
        UserTestsData.setUpTestData()
        cls.token = RefreshToken.for_user(user=cls.user)

    def test_list_book(self):
        response = self.client.get('/book/')
        self.assertEqual(response.status_code, 200)

    def test_create_book(self):
        data = {"title": "Finders Keepers", 
                "author": "Natalie Barelli", 
                "publish_date": "2023-8-26", 
                "ISBN": "9780648731252", 
                "price": 3.27}

        # Checking that the request failed without credentials
        response = self.client.post('/book/', data, format="json")
        self.assertEqual(response.status_code, 401)

        # Checking that the request success with credentials
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.token.access_token}")
        response = self.client.post('/book/', data, format="json")
        self.assertEqual(response.status_code, 201)
