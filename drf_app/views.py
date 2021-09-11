  
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import ThingsSerializer
from .models import Things
from .permissions import IsOwnerOrReadOnly

# Create your views here.

class ThingsList(generics.ListCreateAPIView):
    permission_classes=(IsAuthenticatedOrReadOnly,)
    queryset = Things.objects.all()
    serializer_class = ThingsSerializer

class ThingsDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Things.objects.all()
    serializer_class = ThingsSerializer