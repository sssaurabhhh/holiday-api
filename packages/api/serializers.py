from rest_framework import serializers
from ..models import *


class PackageSerializers(serializers.ModelSerializer):
    class Meta:
        model = Packages

        fields = ('name', 'startdate', 'enddate', 'packagecode', 'country')


class CountrySerializers(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('cname',
                  'countrycode',
                  'status')