from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import UsersViewSet, get_token, user_registration

app_name = 'users'

router = DefaultRouter()
router.register('users', UsersViewSet, basename='users')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/auth/signup/', user_registration, name='registration'),
    path('v1/auth/token/', get_token, name='token')
]
