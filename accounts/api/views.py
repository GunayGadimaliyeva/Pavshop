from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


from rest_framework_simplejwt.tokens import RefreshToken

# for subscription:
from rest_framework import generics
from .serializers import SubscriberEmailSerializer
from accounts.models import SubscriberEmail


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        token['first_name'] = user.first_name
        token['email_address'] = user.first_name
        token['staff_status'] = user.first_name




        # ...

        return token



class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class SubscriberEmailView(generics.ListCreateAPIView):
    serializer_class = SubscriberEmailSerializer
    queryset = SubscriberEmail.objects.all()