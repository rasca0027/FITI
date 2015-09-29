from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    # show group status
    username = request.user.username
    # show group booked time
    schedule = Schedule.objects.filter(booker=request.user)
    # show link to book
    print schedule
    return render(request, 'dashboard.html', {'name': username, 'schedule': schedule })
    #return HttpResponse('sss')

@login_required
def booking(request):
    if request.method == 'GET':
        time_dict = {}
        for prof in Tutor.objects.all():
            time_dict[prof.name] = []
            for time_slot in TimeTable.objects.all():
                if time_slot.id not in Schedule.objects.filter(tutor=prof).values_list('time', flat=True):
                    show_time = time_slot.time.strftime("%Y-%m-%d %H:%M")
                    time_dict[prof.name].append(show_time) 
        return render(request, 'base.html', {'time_dict': time_dict})
    else: # post
        for e in request.POST.items():
            tutor = e[0]
            time = e[1]
            print tutor, time
            if tutor[:4] == 'time':
                print tutor[5:]
                tutor_obj = Tutor.objects.get(name=tutor[5:])
                time_obj = TimeTable.objects.get(time=time)
                # check duplicate
                if len(Schedule.objects.filter(tutor=tutor_obj, time=time_obj)) != 0:
                    return HttpResponse('time already booked, please reload the page and try again.')
                q = Schedule(time=time_obj, tutor=tutor_obj, booker=request.user)
                q.save()
        return HttpResponse('successfully booked!<br><a href="/schedule/">return</a>')

