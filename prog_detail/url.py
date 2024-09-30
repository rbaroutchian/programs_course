from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name = 'details'

urlpatterns = [
    path('<str:slug>/', views.program_detail_view, name='detail')




]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
