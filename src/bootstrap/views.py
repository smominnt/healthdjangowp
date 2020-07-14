# from django.views import generic
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import BmrEntry
from .models import Tdee

# from .models import Demo

@login_required(login_url='accounts:login')
def index_view(request):
    return render(request, "index.html", {})

@login_required(login_url='accounts:login')
def result_view(request): # used to get the result of a calculation based on stored data
    try:
        queryset = Tdee.objects.get(user=request.user)
    except:
        return redirect('bootstrap:calc')

    bmr = queryset.bmr
    val = 1.0
    objlist = []
    for x in range(6):
        objlist.append(bmr*val)
        val += 0.2
    context = {
        "result": objlist
    }
    return render(request, "tdee_result.html", context)

@login_required(login_url='accounts:login')
def calc_view(request): # validate user input and calculate tdee using mathematical formula
    my_form = BmrEntry(request.POST or None)
    instance = my_form.save(commit=False)
    height = instance.feet * 12 + instance.inches
    bmr = 0
    if my_form.CHOICES:
        bmr = 66.47 + 6.24 * instance.weight + 12.7 * height - 6.755 * instance.age
    else:
         bmr = 655.1 + 4.35 * instance.weight + 4.7 * height - 4.7 * instance.age
    instance.bmr = bmr
    instance.user = request.user
    tmp = ""
    try:
        tmp = Tdee.objects.get(user=request.user)
    except:
        print("catch")
        # do nothing
    if my_form.is_valid():
        if (tmp):
            tmp.weight = instance.weight
            tmp.feet = instance.feet
            tmp.inches = instance.inches
            tmp.age = instance.age
            tmp.bmr = instance.bmr
            tmp.save()
        else:
            instance.save()
        return redirect('.')


    context = {
        'form': my_form
    }
    return render(request, "tdee_calc.html", context)




# class IndexView():
#     template_name = 'index.html'
#     context_object_name = 'demo_list'
#     # def get_queryset(self):
#     #     return Demo.objects.all().order_by('id')
