from django.db import models
from django.contrib.auth.models import User

class TimeTable(models.Model):
    time = models.DateTimeField('time')

    def __unicode__(self):
        return str(self.time)

class Tutor(models.Model):
    name = models.CharField(max_length=30)
    time_available = models.ManyToManyField(TimeTable, blank=True)

    def __unicode__(self):
        return self.name

class Schedule(models.Model):
    tutor = models.ForeignKey(Tutor, null=True)
    time = models.ForeignKey(TimeTable, null=True)
    booker = models.ForeignKey(User)

    def __unicode__(self):
        return str(self.time)
    
    class Meta:
        unique_together = (('tutor', 'time'),)
