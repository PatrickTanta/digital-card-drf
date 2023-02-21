from django.urls import path
from rest_framework.routers import DefaultRouter
from users.api.views import UserApiViewSet, UserDetailView

router_user = DefaultRouter()
router_user.register(r'users', UserApiViewSet, basename='users')

urlpatterns = [
    path('auth/me/', UserDetailView.as_view(), name='user-detail')
]