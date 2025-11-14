# 🏥 RS Django - Sistem Manajemen Data Pasien

<div align="center">

![Django](https://img.shields.io/badge/Django-5.2-092E20?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

**Aplikasi web modern untuk manajemen data pasien rumah sakit**

[Demo](#-preview) • [Fitur](#-fitur-utama) • [Instalasi](#-instalasi) • [Dokumentasi](#-dokumentasi)

</div>

---

## 📖 Tentang Proyek

**RS Django** adalah aplikasi web berbasis Django yang dirancang untuk mempermudah manajemen data pasien di rumah sakit. Proyek ini dibuat sebagai media pembelajaran Django dengan implementasi CRUD (Create, Read, Update, Delete) yang lengkap dan interface yang user-friendly.

### 🎯 Tujuan Proyek
- 📚 Praktik pengembangan web dengan Django framework
- 💾 Implementasi operasi database CRUD
- 🎨 Pengembangan UI/UX yang interaktif dan responsif
- 🔧 Pembelajaran best practices dalam web development

---

## ✨ Fitur Utama

<table>
<tr>
<td width="50%">

### 👤 Manajemen Pasien
- ➕ **Tambah Pasien Baru** - Form input data lengkap
- 📋 **Daftar Pasien** - Tampilan tabel interaktif
- ✏️ **Edit Data** - Update informasi pasien
- 🗑️ **Hapus Data** - Soft/hard delete

</td>
<td width="50%">

### 🎨 Interface & UX
- 📱 **Responsive Design** - Mobile & desktop friendly
- 🎭 **UI Modern** - Template HTML dengan CSS styling
- ⚡ **Fast Loading** - Optimasi performa
- 🔍 **Easy Navigation** - User-friendly interface

</td>
</tr>
</table>

---

## 🖼️ Preview

> 💡 **Tips**: screenshot aplikasi!

```
<img width="1920" height="1080" alt="Screenshot (481)" src="https://github.com/user-attachments/assets/474b9106-c9d8-4187-9b1c-3fd00a0121aa" />
<img width="1920" height="1080" alt="Screenshot (480)" src="https://github.com/user-attachments/assets/554b66c1-d4bf-4b70-b69c-bca707139a06" />
<img width="1920" height="1080" alt="Screenshot (479)" src="https://github.com/user-attachments/assets/367c3972-7c35-43ae-aa8f-b68c0a0d2c71" />


```

---

## 🚀 Instalasi

### Prasyarat
- Python 3.11 atau lebih tinggi
- pip (Python package manager)
- Git

### Langkah Instalasi

1️⃣ **Clone Repository**
```bash
git clone https://github.com/USERNAME/rs-django.git
cd rs-django
```

2️⃣ **Install Dependencies**
```bash
# Untuk sistem dengan package manager
sudo pip install --break-system-packages django mysql-connector-python

# Atau menggunakan virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # Linux/Mac
# atau
venv\Scripts\activate  # Windows
pip install django mysql-connector-python
```

3️⃣ **Setup Database**
```bash
# Membuat tabel di database
python manage.py makemigrations
python manage.py migrate
```

4️⃣ **Jalankan Server**
```bash
python manage.py runserver 0.0.0.0:8010
```

5️⃣ **Akses Aplikasi**

Buka browser dan navigasi ke:
- Local: `http://localhost:8010`
- Network: `http://[IP_ADDRESS]:8010`

---

## 📁 Struktur Proyek

```
rs-django/
│
├── 📂 pibal_project/          # Konfigurasi utama Django
│   ├── settings.py            # ⚙️ Pengaturan aplikasi
│   ├── urls.py                # 🔗 URL routing utama
│   └── wsgi.py                # 🌐 WSGI configuration
│
├── 📂 pasien_app/             # Aplikasi manajemen pasien
│   ├── 📂 migrations/         # 📊 File migrasi database
│   ├── 📂 templates/          # 🎨 Template HTML
│   ├── 📂 static/             # 🖼️ CSS, JS, Images
│   ├── models.py              # 🗄️ Model database
│   ├── views.py               # 👁️ Business logic
│   ├── urls.py                # 🔗 App URL routing
│   └── admin.py               # 👨‍💼 Django admin config
│
├── db.sqlite3                 # 💾 Database SQLite
├── manage.py                  # 🛠️ Django management script
└── README.md                  # 📖 Dokumentasi ini

```

---

## 🔧 Konfigurasi

### Database Default (SQLite)

Proyek ini menggunakan SQLite sebagai database default untuk kemudahan development. Tidak perlu setup database server!

### Migrasi ke MySQL/MariaDB (Opsional)

Jika ingin menggunakan MySQL/MariaDB untuk production:

1. **Buat Database**
```sql
CREATE DATABASE rs_django CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

2. **Update `settings.py`**
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'rs_django',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

3. **Jalankan Migrasi**
```bash
python manage.py migrate
```

---

## 💻 Teknologi yang Digunakan

| Kategori | Stack |
|----------|-------|
| **Backend** | Python 3.11, Django 5.2 |
| **Frontend** | HTML5, CSS3, JavaScript |
| **Database** | SQLite (default), MySQL/MariaDB (opsional) |
| **Server** | Django Development Server, WSGI |

---

## 📚 Dokumentasi

### Model Pasien

```python
class Pasien(models.Model):
    nama = models.CharField(max_length=100)
    umur = models.IntegerField()
    alamat = models.TextField()
    # ... field lainnya
```

### URL Endpoints

| Method | Endpoint | Deskripsi |
|--------|----------|-----------|
| GET | `/` | Halaman daftar pasien |
| GET | `/tambah/` | Form tambah pasien |
| POST | `/tambah/` | Simpan data pasien baru |
| GET | `/edit/<id>/` | Form edit pasien |
| POST | `/edit/<id>/` | Update data pasien |
| POST | `/hapus/<id>/` | Hapus data pasien |

---

## ⚠️ Catatan Penting

- 🔒 **Jangan commit `db.sqlite3`** jika berisi data sensitif
- 🔐 Gunakan **environment variables** untuk kredensial database di production
- 🚀 Untuk production, gunakan server seperti **Gunicorn + Nginx**
- 📦 Gunakan **virtual environment** untuk isolasi dependencies
- 🔄 Backup database secara berkala

---

## 🤝 Kontribusi

Kontribusi sangat diterima! Silakan:

1. Fork repository ini
2. Buat branch fitur (`git checkout -b fitur-baru`)
3. Commit perubahan (`git commit -m 'Menambah fitur baru'`)
4. Push ke branch (`git push origin fitur-baru`)
5. Buat Pull Request

---

## 📝 Roadmap

- [ ] Sistem autentikasi user
- [ ] Export data ke PDF/Excel
- [ ] Dashboard analytics
- [ ] REST API integration
- [ ] Unit testing
- [ ] Docker containerization

---

## 📄 Lisensi

Proyek ini dilisensikan di bawah [MIT License](LICENSE) - bebas untuk digunakan dan dimodifikasi.

---

## 👨‍💻 Developer

Dibuat dengan ❤️ untuk belajar Django

**Pertanyaan atau saran?** Silakan buat [issue](https://github.com/USERNAME/rs-django/issues) baru!

---

<div align="center">

**⭐ Jangan lupa beri star jika proyek ini bermanfaat! ⭐**

</div>
