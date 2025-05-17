from django.urls import path
from . import views
urlpatterns = [
    path('', views.dashboard_view, name='dashboard'),
    path('complete/<int:appointment_id>/', views.complete_appointment, name='complete_appointment'),
    path('complete/index/', views.list, name='list'),

]
