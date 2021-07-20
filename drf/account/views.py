from django.contrib.auth import get_user_model, authenticate, login
from django.http import JsonResponse

from django.conf import settings
from django.core.mail import send_mail, EmailMessage, EmailMultiAlternatives
from django.template import Context
from django.template.loader import get_template, render_to_string
from django.utils.html import strip_tags

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from .models import Profile
from .serializers import UserSerializer, UserRegisSerializer, ProfileSerializer

User = get_user_model()

@api_view(['POST'])
def loginApi(request):
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        email = serializer.validated_data.get('email')
        password = serializer.validated_data.get('password')

        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            print(f"[SERVER] Login successfully from {user}\n")
            token = Token.objects.get(user=user)

            return Response({"auth_token": token.key}, status=status.HTTP_200_OK)
        else:
            return JsonResponse(status=status.HTTP_401_UNAUTHORIZED, data={'status':'false', 'message': "Invalid email or password"})
    
    else:
        return JsonResponse(status=status.HTTP_401_UNAUTHORIZED, data={'status':'false', 'message': "Invalid email or password"})


@api_view(['POST'])
def register(request):
    serializer = UserRegisSerializer(data=request.data)

    if serializer.is_valid():
        user =  serializer.save()
        print(f"User {user} is created\n")
    
    else:
        print(serializer.errors)
        return JsonResponse(status=status.HTTP_401_UNAUTHORIZED, data={'errors': serializer.errors})
    
    return JsonResponse(status=status.HTTP_200_OK, data={'message': "User is created"})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getProfile(request):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user=request.user)
        serializer = ProfileSerializer(profile, many=False, context={"request": request})

        return Response(serializer.data)
    
    else:
        return JsonResponse(status=status.HTTP_401_UNAUTHORIZED, data={'status':'false', 'message': "You are not authorized to view this profile"})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def updateProfile(request):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user=request.user)
        serializer = ProfileSerializer(profile, data=request.data)

        if serializer.is_valid():
            serializer.save()
        else:
            print("Error")
        
        return JsonResponse(status=status.HTTP_200_OK)
    
    else:
        return JsonResponse(status=status.HTTP_401_UNAUTHORIZED, data={'message': "You are not authorized to view this profile"})
    

@api_view(['GET'])
def sendEmail(request):
    # subject = 'Sending Email'
    # message = f'Hi Quoc Bao, testing.'
    # email_from = settings.EMAIL_HOST_USER
    # recipient_list = ["baoB1809677@student.ctu.edu.vn", ]
    # send_mail( subject, message, email_from, recipient_list )

    email_from = settings.EMAIL_HOST_USER
    recipient_list = ["baoB1809677@student.ctu.edu.vn", ]

    template = get_template("welcome.html")
    message = render_to_string('welcome.html', {})
    text_content = strip_tags(message)

    subject = "Welcome to Footco"

    msg = EmailMultiAlternatives(subject, text_content, email_from, to=recipient_list)
    msg.attach_alternative(message, "text/html")
    msg.send()

    return JsonResponse(status=status.HTTP_200_OK, data={'message': "email is sent"})