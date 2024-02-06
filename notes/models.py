from django.db import models

class NotesModel(models.Model):
    text = models.TextField()

