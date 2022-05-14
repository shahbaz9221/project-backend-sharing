from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from userregistration.models import AdminLogin, UserRegistration
# Create your views here.

@api_view(['POST'])
def registration(request):
    if request.method == 'POST':
        try:
            first_name = request.data.get('data').get('first_name')
            last_name = request.data.get('data').get('last_name')
            email = request.data.get('data').get('email')
            location = request.data.get('data').get('location')
        except:
            return Response({'response':'invalid_key_error'})

        try:
            UserRegistration.objects.create(first_name=first_name, last_name=last_name,email=email,location=location)
            return Response({'response': 'true'},status=status.HTTP_200_OK)
        except:
            return Response({'response': 'false'},status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login(request):
    if request.method == 'POST':
        print(request.data)
        try:
            email = request.data.get('email')
            password = request.data.get('password')
        except:
            return Response({'response':'invalid key error'})

        if AdminLogin.objects.filter(email=email,password=password).exists():
            return Response({'response': 'true'},status=status.HTTP_200_OK)
        
        else:
            return Response({'response': 'false'})