from django.urls import path, reverse

from app.views import landing, stats, index, landing_alter

urlpatterns = [
    path('', index, name='index'),
    path('landing/', landing, name='landing'),
    path('stats/', stats, name='stats'),
    path('landing_alternate/', landing_alter, name='landing_alternate')
]
