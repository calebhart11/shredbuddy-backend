from .models import Session
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import SessionSerializer

# Create your views here.
class SessionViewSet(viewsets.ModelViewSet):
    ## The main query for the index route
    queryset = Session.objects.all()
    # set serializer class for serializing output
    serializer_class = SessionSerializer
    #set permissions level with permission class
    permission_classes = [permissions.AllowAny]