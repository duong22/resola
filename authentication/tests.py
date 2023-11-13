from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from book.models import Book
from rest_framework.test import APITestCase


class AuthenticationViewsetTestCase(APITestCase):

    def test_create_change_password_user(self):
        user = {"email": "test_user@email.com",
                "username": "test_user",
                "password": "test_user_password",
                "password2": "test_user_password",
            }
        response = self.client.post('/authentication/register/', user, format="json")
        self.assertEqual(response.status_code, 201)

        user = {"username": "test_user",
                "password": "test_user_password"}
        response = self.client.post('/authentication/login/', user, format="json")
        self.assertEqual(response.status_code, 200)
        self.assertIn("id", response.data)
        self.assertIn("refresh", response.data)
        self.assertIn("access", response.data)

        user_id = response.data["id"]
        access_token = response.data["access"]
        change_password = {"old_password": "test_user_password",
                            "password": "test_new_password",
                            "password2": "test_new_password",
                        }
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {access_token}")
        response = self.client.put(f'/authentication/change_password/{user_id}/', change_password, format="json")
        self.assertEqual(response.status_code, 200)
