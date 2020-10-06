from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse
from django.views import generic
from merchants.forms import NewForm
from rest_framework import viewsets
from .serializers import MerchantSerializer
import requests
from bs4 import BeautifulSoup

from .models import Merchant

class IndexView(generic.ListView):
    template_name = 'merchants/index.html'
    context_object_name = 'merchants_list'

    def get_queryset(self):
        return Merchant.objects.order_by('name')

class DetailView(generic.DetailView):
    model = Merchant
    template_name = 'merchants/detail.html'

def new(request):
    form = NewForm()
    return render(request, 'merchants/new.html', { 'form': form } )

def create(request):
    form = NewForm(request.POST)
    try:
        new_merchant = form.save()
    except:
        return render(request, 'merchants/new.html', {
            'from': form, 'error_message': "Something went wrong",
        })
    else:
        return HttpResponseRedirect(reverse('merchants:detail', args=(new_merchant.id)))

class MerchantView(viewsets.ModelViewSet):
    queryset = Merchant.objects.all()
    serializer_class = MerchantSerializer
