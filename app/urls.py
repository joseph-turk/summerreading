from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views


app_name = 'app'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('kids/', views.KidProgramsIndex.as_view(), name='kid_programs'),
    path('teens/', views.TeenProgramsIndex.as_view(), name='teen_programs'),
    path('programs/', views.IndexView.as_view(), name='programs'),
    path('programs/<int:pk>', views.DetailView.as_view(), name='detail'),
    path('programs/<int:program_id>/register', views.register, name='register'),
    path('programs/<int:program_id>/add_registration',
         views.add_registration, name='add_registration'),
    path('programs/<int:program_id>/confirmed',
         views.confirmed, name='confirmation'),
    path('patrons/', views.PatronsIndex.as_view(), name='patrons'),
    path('patrons/<int:pk>', views.PatronDetail.as_view(), name='patron')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)