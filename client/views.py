from django.shortcuts import render
from django.views.generic import ListView
from .models import *

# Create your views here.

class  LeadsView(ListView):

    template_name = 'index.html'
    context_object_name = 'context'

    def get_queryset(self):
        print("In Leads View.")
        context ={}
        context['data'] = Leads.objects.all()
        print(context)
        for x in context['data']:
            print(x.fname)
            print(x.lname)
            print(x.address)
            print()
        return context


class ContactsView(ListView):
    pass


class AccountsView(ListView):
    pass


