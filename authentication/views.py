from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth.models import User
from .serializers import RegisterSerializer, ChangePasswordSerializer, LogoutSerializer, LoginSerializer
from rest_framework import generics
from rest_framework_simplejwt.views import TokenObtainPairView


class RegisterView(generics.CreateAPIView):
	queryset = User.objects.all()
	permission_classes = (AllowAny,)
	serializer_class = RegisterSerializer


class ChangePasswordView(generics.UpdateAPIView):

	queryset = User.objects.all()
	permission_classes = (IsAuthenticated,)
	serializer_class = ChangePasswordSerializer


from rest_framework.response import Response
from rest_framework import status

class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer

class LogoutView(generics.GenericAPIView):
	permission_classes = (IsAuthenticated,)
	serializer_class = LogoutSerializer

	def post(self, request):
		serializer = self.serializer_class(data=request.data)
		serializer.is_valid(raise_exception=True)
		serializer.save()

		return Response(status=status.HTTP_205_RESET_CONTENT)

