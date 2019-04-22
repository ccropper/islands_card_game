from django.shortcuts import render
from django.http import JsonResponse
from django.forms.models import model_to_dict
from game import game
# from game.models import Data


# Create your views here.
def index(request):
    ''' View function for the landing page of the game site.'''
    context = {}

    return render(request, 'index.html', context=context)

# def data(request):
#     # returns the first instance in the Data object as a json response
#     json_data = model_to_dict(Data.objects.first())
#     return JsonResponse(json_data, safe=False)

def play(request):
    '''renders card game'''
    new_game = game.Game()
    context = {
        'game_deck': new_game.game_deck.cards,
        'game_board': new_game.game_board,
    }
    return render(request, 'play.html', context=context)