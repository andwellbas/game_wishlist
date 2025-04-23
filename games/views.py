from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

from rest_framework import viewsets
from .serializers import GameSerializer
from rest_framework.permissions import IsAuthenticated

from .models import Game, STATUS_CHOICES
from .forms import GameForm


def game_list(request):
    status_filter = request.GET.get("status")
    if status_filter:
        games = Game.objects.filter(status=status_filter)
    else:
        games = Game.objects.all()

    form = GameForm()  # for getting choices

    return render(request, "games/game_list.html", {
        "games": games,
        "status_filter": status_filter,
        "form": form
    })


def add_game(request):
    if request.method == "POST":
        form = GameForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("game_list")
    else:
        form = GameForm()
    return render(request, "games/add_game.html", {"form": form})


def delete_game(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    game.delete()
    return redirect("game_list")


@require_POST
def update_status(request, game_id):
    new_status = request.POST.get("status")
    game = get_object_or_404(Game, id=game_id)
    if new_status in dict(STATUS_CHOICES).keys():
        game.status = new_status
        game.save()
    return redirect("game_list")


class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = [IsAuthenticated]