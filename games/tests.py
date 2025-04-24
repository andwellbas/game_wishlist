from django.test import TestCase
from .models import Game
from django.urls import reverse
# Create your tests here.

class GameModelTest(TestCase):

    def test_create_game(self):
        game = Game.objects.create(
            title="Cyberpunk 2077",
            platform="PC",
            status="wishlist",
            price=59.99
        )
        self.assertEqual(game.title, "Cyberpunk 2077")
        self.assertEqual(game.platform, "PC")
        self.assertEqual(game.status, "wishlist")
        self.assertEqual(float(game.price), 59.99)

    def test_game_list_view(self):
        Game.objects.create(
            title="Cyberpunk 2077",
            platform="PC",
            status="playing",
            price=59.99
        )

        response = self.client.get(reverse('game_list'), {'status': 'playing'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Cyberpunk 2077")