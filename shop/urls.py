from .views import dashboard, detail
from django.urls import path

urlpatterns = [
    path('', dashboard),
    path('detail/', detail)
]
