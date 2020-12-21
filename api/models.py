from django.db import models

# Create your models here.
class timefhumanRequestResponse(models.Model):
    request = models.TextField()
    timezone = models.TextField(blank=True)
    detected_date_response = models.TextField(blank=True)

    def __str__(self):
        return 'ID: ' + str(self.id) + ' - ' + str(self.request[:80]) + '...'

class spacyRequestResponse(models.Model):
    request = models.TextField()
    entity_detect_response = models.TextField(blank=True)

    def __str__(self):
        return 'ID: ' + str(self.id) + ' - ' + str(self.request[:80]) + '...'

"""class ducklingRequestResponse(models.Model):
    request = models.TextField()
    duckling_response = models.TextField(blank=True)

    def __str__(self):
        return 'ID: ' + str(self.id) + ' - ' + str(self.request[:80]) + '...'"""
