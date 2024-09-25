from django.db import models 

class Joke(models.Model):
    joke_text = models.TextField()
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return f'Joke {self.number}'
