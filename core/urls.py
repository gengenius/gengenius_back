from rest_framework import routers
from django.urls import path, include
from .import views
from .views import ping

router = routers.DefaultRouter()
router.register('teacher_users', views.TeacherUserViewSet, basename='teacher_user')
router.register('users', views.UserViewSet, basename='user')
urlpatterns=router.urls

urlpatterns = [
    path('ping/', ping),  # Add the ping endpoint
 ] + router.urls  # Combine router URLs with other URL patterns