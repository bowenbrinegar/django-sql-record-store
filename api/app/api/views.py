from rest_framework import generics, viewsets
from django.db.models import Q
from app.models import User, Record
from .serializers import UserSerializer, RecordSerializer

class UserCreateView(generics.CreateAPIView):
    lookup_field = 'pk'
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all()

class UserAllView(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-created')
    serializer_class = UserSerializer

class UserLookupView(viewsets.ModelViewSet):
    serializer_class = UserSerializer

    def get_queryset(self):
        qs = User.objects.all()
        query = self.request.GET['q']
        if query is not None:
            qs = qs.filter(Q(first_name__icontains=query)|Q(last_name__icontains=query)).distinct()
        return qs

class UserRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all()

class RecordCreateView(generics.CreateAPIView):
    lookup_field = 'pk'
    serializer_class = RecordSerializer

    def get_queryset(self):
        return Record.objects.all()

class RecordAllView(viewsets.ModelViewSet):
    queryset = Record.objects.all().order_by('-created')
    serializer_class = RecordSerializer  

class RecordRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = RecordSerializer

    def get_queryset(self):
        return Record.objects.all()