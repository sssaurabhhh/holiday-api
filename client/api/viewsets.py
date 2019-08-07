from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication,BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from ..models import *

__all__ = [
    'LeadsViewSet',
    'CommentViewSet'
]

class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    def get_queryset(self):
        return Comments.objects.all()

    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = self.serializer_class(data={'comments': data['comments'] ,
                                                 'entityid': data['entityid'],
                                                 'type': data['type']
                                                 })
        if serializer.is_valid():
            try:
                self.perform_create(serializer)
                headers = self.get_success_headers(serializer.data)
            except Exception as e:
                print("Error Raised:", e)
            return Response(serializer.data,status=status.HTTP_201_CREATED, headers=headers)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        data = request.data
        serializer = self.serializer_class(Comments.objects.get(pk=data['id']), data=data)
        if serializer.is_valid():
            serializer.update()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LeadsViewSet(viewsets.ModelViewSet):
    serializer_class = LeadsSerializer

    def get_queryset(self):
        print("HERE I AM *************")
        return Leads.objects.all()

    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = self.serializer_class(data={'fname':data['fname'] ,
                                                 'lname':data['lname'],
                                                 #'emailid':{data['emailid']},
                                                 'address':data['address'],
                                                 'country':data['country'],
                                                 'deleted':data['deleted'],
                                                 'status':data['status']
                                                 })
        if serializer.is_valid():
            try:
                self.perform_create(serializer)
                headers = self.get_success_headers(serializer.data)
            except Exception as e:
                print("Error Raised:", e)
            return Response(serializer.data,status=status.HTTP_201_CREATED, headers=headers)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        data = request.data
        serializer = self.serializer_class(Leads.objects.get(pk=data['id']), data=data)
        if serializer.is_valid():
            serializer.update()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)