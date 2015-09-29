from django.contrib import admin
from .models import *

admin.site.register(Tutor)
admin.site.register(TimeTable)
# Register your models here.
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('tutor', 'time', 'booker')


admin.site.register(Schedule, ScheduleAdmin)
