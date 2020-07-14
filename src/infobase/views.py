from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .models import Entry, make_entry
from .forms import EntryForm

from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='accounts:login')
def entry_list_view(request):
    queryset = Entry.objects.all()
    objlist = []
    held_day = currday = p_sum = c_sum = x = 0
    while x < len(queryset): # build list with daily totals
        if queryset[x].user != request.user:
            x += 1
            continue
        currday = queryset[x].timestamp.day
        if held_day != currday: # if we detect a new day, we must calculate the totals for the previous day
            if not held_day == 0:
                tmp = make_entry(c_sum, p_sum, held_day)
                objlist.append(tmp)
                p_sum = 0
                c_sum = 0
            held_day = currday
            test = 0
        c_sum += queryset[x].c_amount
        p_sum += queryset[x].p_amount
        objlist.append(queryset[x])
        x += 1
        test += 1
    tmp = make_entry(c_sum, p_sum, held_day) # calculate the totals for the last day in data/current day
    objlist.append(tmp)
    context = {
        "entry_list": objlist
    }
    return render(request, "entries.html", context)

@login_required(login_url='accounts:login')
def entry_create_view(request): # receive user inputs and create an Entry in the database
    if not request.user.is_authenticated:
        raise Http404
    my_form = EntryForm(request.POST or None)
    if my_form.is_valid():
        instance = my_form.save(commit=False)
        instance.user = request.user
        instance.save()
        return redirect('..')
    context = {
        'form': my_form
    }
    return render(request, "entry_create.html", context)
