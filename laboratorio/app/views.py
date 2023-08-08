from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Laboratorio

class LaboratorioListView(ListView):
    model = Laboratorio

class LaboratorioDetailView(DetailView):
    model = Laboratorio

class LaboratorioCreateView(CreateView):
    model = Laboratorio
    fields = '__all__'

class LaboratorioUpdateView(UpdateView):
    model = Laboratorio
    fields = '__all__'

class LaboratorioDeleteView(DeleteView):
    model = Laboratorio
    success_url = reverse_lazy('laboratorio_list')