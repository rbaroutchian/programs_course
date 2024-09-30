from django.shortcuts import render
from personnel.models import Personnels

def personnel_list(request):
    p_list = Personnels.objects.all().order_by('per_name')
    return render(request, 'p_temp/personnel_list.html',
                  {'personnels': p_list})

