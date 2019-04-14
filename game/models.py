from django.db import models

# Create your models here.

class Data(models.Model):
    '''
    a model to represent data about the current state of the game
    '''
    GAME_STATE_CHOICES = (
        ('r', 'Ready to play'),
        ('p', 'In progress'),
        ('w', 'Won'),
        ('l', 'Lost')
    )
    game_state = models.CharField(
        max_length=1,
        choices=GAME_STATE_CHOICES,
        blank=True,
        default='r'
    )

    def __str__(self):
        return f'{self.game_state}'




