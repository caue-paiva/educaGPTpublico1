from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chat1', views.chat, name='chat1'),
    path('loadChat', views.load_chat, name='loadChat')
]
