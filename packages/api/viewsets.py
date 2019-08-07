from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication,BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from ..models import *


__all__ = [
    'CountryViewSet'
]

class CountryViewSet(viewsets.ModelViewSet):

    serializer_class = CountrySerializers

    def get_queryset(self):

        return Country.objects.all()

    def create(self, request, *args, **kwargs):

        request = request.data
        print(request)

        serializer = self.serializer_class(data={'cname':request['cname'],
                                                 'countrycode':request['countrycode'],
                                                 'status':request['status']
                                                 })
        if serializer.is_valid():
            try:
                self.perform_create(serializer)
                headers = self.get_success_headers(serializer.data)
            except Exception as e:
                print("Error Raised:", e)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        data = request.data
        serializer = self.serializer_class(Country.objects.get(pk=data['id']), data=data)
        if serializer.is_valid():
            serializer.update()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
