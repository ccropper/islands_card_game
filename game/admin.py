from django.contrib import admin
from game.models import Data

# Register your models here.
@admin.register(Data)
class DataAdmin(admin.ModelAdmin):
    list_display = ('game_state',)
    list_filter = ('game_state',)
    fields = ('game_state',)
