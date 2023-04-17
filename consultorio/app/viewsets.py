from rest_framework import viewsets
from .serializers import PersonSerializer
from .models import Person


class PersonViewSet(viewsets.ModelViewSet):
    model = Person
    serializer_class = PersonSerializer
    queryset = Person.objects.all()
    filter_fields = ('name', 'age', 'password', 'email', 'address', 'cpf')
