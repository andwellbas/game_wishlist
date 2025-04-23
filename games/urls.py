from django.urls import path, include
from . import views

from .views import GameViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token


router = DefaultRouter()
router.register(r'games', GameViewSet)


urlpatterns = [
    path("", views.game_list, name="game_list"),
    path("add/", views.add_game, name="add_game"),
    path("delete/<int:game_id>/", views.delete_game, name="delete_game"),
    path("update-status/<int:game_id>/", views.update_status, name="update_status"),

    path("api/", include(router.urls)),
    path('api/login/', obtain_auth_token, name='api_token_auth'),
]