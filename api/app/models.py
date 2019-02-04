from django.db import models


class User(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=100, blank=True, default='')
    last_name = models.CharField(max_length=100, blank=True, default='')
    
    objects = models.Manager()
    
    class Meta:
        managed = True
        ordering = ('created',)
        app_label = 'app'


class Record(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    artist = models.CharField(max_length=100, blank=True, default='')
    genre = models.CharField(max_length=100, blank=True, default='')
    year = models.IntegerField()
    quanity_available = models.IntegerField()

    objects = models.Manager()

    class Meta:
        managed = True
        app_label = 'app'

class UserInventory(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    recordId = models.ForeignKey(Record, on_delete=models.CASCADE)

    objects = models.Manager()

    class Meta:
        managed = True
        app_label = 'app'
