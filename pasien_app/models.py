from django.db import models

class Pasien(models.Model):
    nama = models.CharField(max_length=100)
    umur = models.IntegerField()
    alamat = models.TextField(blank=True)

    def __str__(self):
        return self.nama

