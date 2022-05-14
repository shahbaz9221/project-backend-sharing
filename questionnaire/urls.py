from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('get_all_questions/',views.get_all_questions, name='get_all_questions'),
    path('get_all_users/',views.get_all_users, name='get_all_users'),
    path('add_or_delete_question/',views.add_or_delete_question, name='add_or_del_questions'),
    path('update_time/',views.update_time, name='update_time')
   

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
