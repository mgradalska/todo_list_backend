from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from app import views

router = routers.DefaultRouter()
router.register(r'tasks', views.TaskViewSet)
router.register(r'boards', views.BoardViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
]
