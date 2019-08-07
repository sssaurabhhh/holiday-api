from rest_framework import serializers
from ..models import *

__all__ = [
    'CommentSerializer',
    'LeadsSerializer'
]

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ('comments',
                  'entityid',
                  'type')

class LeadsSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True)
    class Meta:
        model = Leads
        fields = ('fname', 'lname',
                  'emailid', 'address',
                  'country', 'deleted',
                  'status','comments')