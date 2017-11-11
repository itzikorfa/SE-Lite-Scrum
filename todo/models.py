from django.db import models
from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from covey.models import CoveyMatrix
User = get_user_model()
# Create your models here.


class Todo(models.Model):

    user = models.ForeignKey(User)
    name = models.CharField(max_length=50, verbose_name="what todo")
    priority = models.IntegerField(validators=[MaxValueValidator(10), MinValueValidator(0)],
                                   default=5)
    description = models.TextField(default='', blank=True)
    task_type = models.ForeignKey(CoveyMatrix, related_name="logcovmat")
    estimated_time = models.IntegerField(validators=[MinValueValidator(0)],null=True,blank=True)
    ETA = models.DateField(null=True,blank=True)
    presentage_complete = models.IntegerField(
        validators=[MaxValueValidator(100), MinValueValidator(0)], verbose_name="%completed", default=0)
    update = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True
                                     , verbose_name='assign at')
    task_completed = models.BooleanField(default=False, verbose_name="completed")

    def get_absolute_url(self):
        return reverse("todo:list")


    class Meta:
        ordering = ['priority', 'timestamp']



class TodoLog(models.Model):
    todo = models.ForeignKey(Todo, related_name="todolog")
    log = models.TextField()
    presentage_complete = models.IntegerField(
        validators=[MaxValueValidator(100), MinValueValidator(0)], verbose_name="%completed", default=0)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True
                                     , verbose_name='log at')
    update = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return "[{}] {}".format(self.timestamp  ,self.log)

    def get_absolute_url(self):
        return reverse("todo:detail", kwargs={"pk": self.todo.pk})