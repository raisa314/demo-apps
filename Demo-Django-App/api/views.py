from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from meetups.models import Meetup
from .serializers import MeetupSerializer, RegistrationSerializer
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.schemas import AutoSchema
from drf_yasg.utils import swagger_auto_schema

@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /api',
        'GET /api/meetups',
        'GET /api/meetups/:slug'
    ]

    return Response(routes)

@swagger_auto_schema(methods=['post'], request_body=RegistrationSerializer)
@api_view(['POST',])
def registrationView(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = 'successfully registered new user.'
            data['email'] = account.email
            data['username'] = account.username
            token = Token.objects.get(user=account).key
            data['token'] = token
        else:
            data = serializer.errors
        
        return Response(data)

@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def getMeetups(request):
    meetups = Meetup.objects.all()
    serializer = MeetupSerializer(meetups, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getMeetup(request, id):
    meetup = Meetup.objects.get(id=id)
    serializer = MeetupSerializer(meetup)
    return Response(serializer.data)


