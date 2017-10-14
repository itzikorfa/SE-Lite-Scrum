from django.db import models
from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from covey.models import CoveyMatrix
User = get_user_model()
# Create your models here.


class Todo(models.Model):
    time_matrix = ((1, "important , urgent"),
                   (2, "important , not urgent"),
                   (3, "not important , urgent"),
                   (4, "not important , not urgent"),
                   )
    user = models.ForeignKey(User)
    name = models.CharField(max_length=50, verbose_name="what todo")
    priority = models.IntegerField(validators=[MaxValueValidator(10), MinValueValidator(0)],
                                   default=5)
    description = models.TextField(default='', blank=True)
    task_type = models.ForeignKey(CoveyMatrix, related_name="logcovmat")
    estimated_time = models.IntegerField(validators=[MinValueValidator(0)],null=True,blank=True)
    ETA = models.DateField(null=True,blank=True)
    presentage_complete = models.IntegerField(
        validators=[MaxValueValidator(10), MinValueValidator(0)], verbose_name="%completed", default=0)
    update = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True
                                     , verbose_name='assign at')

    def get_absolute_url(self):
        return reverse("todo:list")


    class Meta:
        ordering = ['priority', 'timestamp']



