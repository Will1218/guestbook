from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from .models import Message

# Create your views here.
class MessageList(ListView):
    model = Message

class MessageDetail(DetailView):
    model = Message

class MessageCreate(CreateView):
    model = Message
    field = '__all__'
    sucess_url = reverse_lazy('msg_list')
