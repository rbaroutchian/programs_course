from django.shortcuts import render, get_object_or_404
from programs.models import Programs
# Create your views here.

def program_list(request):
    programs = Programs.objects.all().order_by('protitle')
    return render(request, 'program_list.html',
                  {'progs': programs})



def index(request):
    return render(request, 'base.html')
