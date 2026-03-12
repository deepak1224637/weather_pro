from django.db import models

class Subscriber(models.Model):
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.email