from django.shortcuts import render, redirect, get_object_or_404
from .models import Pasien

def index(request):
    data_pasien = Pasien.objects.all()
    return render(request, 'index.html', {'data_pasien': data_pasien})

def tambah_pasien(request):
    if request.method == 'POST':
        nama = request.POST['nama']
        umur = request.POST['umur']
        alamat = request.POST['alamat']
        Pasien.objects.create(nama=nama, umur=umur, alamat=alamat)
        return redirect('index')
    return render(request, 'tambah.html')

def edit_pasien(request, id):
    pasien = get_object_or_404(Pasien, id=id)
    if request.method == 'POST':
        pasien.nama = request.POST['nama']
        pasien.umur = request.POST['umur']
        pasien.alamat = request.POST['alamat']
        pasien.save()
        return redirect('index')
    return render(request, 'edit.html', {'pasien': pasien})

def hapus_pasien(request, id):
    pasien = get_object_or_404(Pasien, id=id)
    pasien.delete()
    return redirect('index')

