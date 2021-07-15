from django.db import models

class Order(models.Model):
    number=models.IntegerField(default=0)

    def __str__(self):
        return self.number

