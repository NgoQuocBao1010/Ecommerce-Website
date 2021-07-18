from django.contrib.auth import get_user_model, authenticate, login
from django.http import JsonResponse

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from .models import Profile
from .serializers import UserSerializer, ProfileSerializer

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


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getProfile(request):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user=request.user)
        serializer = ProfileSerializer(profile, many=False, context={"request": request})

        return Response(serializer.data)
    
    else:
        return JsonResponse(status=status.HTTP_401_UNAUTHORIZED, data={'status':'false', 'message': "You are not authorized to view this profile"})