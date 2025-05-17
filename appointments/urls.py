from django.urls import path
import appointments.views as views
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
import appointments.views as views
from django.conf.urls.static import static
from django.conf import settings

from appointments.views import download_exel

urlpatterns = [
    path('', views.home, name='home'),  # Домашняя страница
    path('doctors/', views.doctors_list, name='doctors_list'),  # Список докторов
    path('doctor/<int:doctor_id>/', views.doctor_detail, name='doctor_detail'),  # Страница врача и запись
    path('make_appointment/<int:doctor_id>/', views.make_appointment, name='make_appointment'),
    # Успешная запись
    path('doctors_by_specialization/<int:spec_id>/', views.doctors_by_specialization, name='doctors_by_specialization'),
    path('contact', views.contact, name='contact'),
    path('download_exel', download_exel, name = 'download_exel'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)