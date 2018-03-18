from django.urls import path
from . import views


app_name = 'app'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('programs/', views.IndexView.as_view(), name='programs'),
    path('programs/<int:pk>', views.DetailView.as_view(), name='detail'),
    path('programs/<int:program_id>/register', views.register, name='register'),
    path('programs/<int:program_id>/add_registration',
         views.add_registration, name='add_registration'),
    path('programs/<int:program_id>/confirmed',
         views.confirmed, name='confirmation'),
    path('patrons/', views.PatronsIndex.as_view(), name='patrons'),
    path('patrons/<int:pk>', views.PatronDetail.as_view(), name='patron')
]
