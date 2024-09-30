from django.urls import path

import prog_detail.views
from . import views
from django.conf import settings
from django.conf.urls.static import static
from prog_detail.models import Program_detail


urlpatterns = [
    path('course', views.program_list, name='program_list'),
    path('<slug:slug>', prog_detail.views.program_detail_view, name='detail'),
    path('', views.index, name='index')



]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
