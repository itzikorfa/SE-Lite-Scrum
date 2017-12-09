from django.db import models
"""
covey untiles class help to create the analyse
"""
class CoveyMatrix(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        unique_together = ('name',)