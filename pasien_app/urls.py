from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),          # Daftar pasien
    path('tambah/', views.tambah_pasien, name='tambah_pasien'),
    path('edit/<int:id>/', views.edit_pasien, name='edit_pasien'),
    path('hapus/<int:id>/', views.hapus_pasien, name='hapus_pasien'),
]

