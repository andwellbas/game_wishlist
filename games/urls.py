from django.urls import path
from . import views


urlpatterns = [
    path("", views.game_list, name="game_list"),
    path("add/", views.add_game, name="add_game"),
    path("delete/<int:game_id>/", views.delete_game, name="delete_game"),
    path("update-status/<int:game_id>/", views.update_status, name="update_status"),

    path("api/games/", views.game_list_api, name="game_list_api")
]