from django.shortcuts import render
from.forms import SubForm

def landing(request):
    form = SubForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form = form.save()


    return render(request, 'landing/landing2.html', locals())