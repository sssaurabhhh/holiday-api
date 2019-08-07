from django.shortcuts import render
from django.http import response, HttpResponse, Http404
from django.views.generic import TemplateView
from django.db.models import Q
# Create your views here.

class Countries(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        return Countries.objects.all()




