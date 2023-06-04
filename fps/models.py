from django.db import models

class Room(models.Model):
    name=models.CharField(default="room",max_length=100)
    port=models.IntegerField(default=7777)

    def __str__(self):
        return self.name+' - '+str(self.port)
