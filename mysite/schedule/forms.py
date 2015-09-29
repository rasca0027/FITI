from django.db import models
from django.forms import ModelForm
from .models import Schedule

class BookingForm(ModelForm):

    class Meta:
        model = Schedule
        fields = ['tutor', 'time']
"""
    def __init__(self, *args, **kwargs):
        super(BookingForm, self).__init__(*args, **kwargs)
        occupied = Schedule.objects.all()
        self.fields['time'].queryset = models.TimeTable.objects.exclude(time=)
"""
