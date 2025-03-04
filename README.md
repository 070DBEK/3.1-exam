# Weather Data Management System

Bu loyiha ob-havo ma'lumotlarini saqlash, ko'rsatish va tahlil qilish uchun Django asosida yaratilgan REST API hisoblanadi.

## Xususiyatlari

- Ob-havo ma'lumotlarini qo'shish, ko'rish, o'zgartirish va o'chirish

- Hududlar bo'yicha ob-havo ma'lumotlarini olish

- Statistik tahlillar (o'rtacha harorat, namlik va boshqalar)

- Kelajak ob-havo bashoratlarini saqlash va ko'rish

- Texnologiyalar

- Backend: Django, Django REST Framework

- Ma'lumotlar bazasi: SQLite 


# O'rnatish:

## 1. Muhitni tayyorlash

        - python -m venv venv 

        - Linux foydalanuvchilari: source venv/bin/activate  

        - Windows foydalanuvchilari: venv\Scripts\activate

## 2. Zarur kutubxonalarni o'rnatish

        - pip install -r requirements.txt

## 3. Ma'lumotlar bazasini yaratish

        - python manage.py makemigrations
        - python manage.py migrate

## 4. Superuser yaratish (ixtiyoriy)

        - python manage.py createsuperuser

## 5. Serverni ishga tushirish

        - python manage.py runserver


