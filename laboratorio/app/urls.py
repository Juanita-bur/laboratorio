# laboratorio/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.LaboratorioListView.as_view(), name='laboratorio_list'),
    path('<int:pk>/', views.LaboratorioDetailView.as_view(), name='laboratorio_detail'),
    path('nuevo/', views.LaboratorioCreateView.as_view(), name='laboratorio_create'),
    path('<int:pk>/editar/', views.LaboratorioUpdateView.as_view(), name='laboratorio_update'),
    path('<int:pk>/eliminar/', views.LaboratorioDeleteView.as_view(), name='laboratorio_delete'),
]
