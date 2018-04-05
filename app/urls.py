from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views


app_name = 'app'
urlpatterns = [
    # Home Views
    path('', views.HomeView.as_view(), name='home'),
    path('kids/', views.grid_register_kids, name='kids_home'),
    path('teens/', views.grid_register_teens, name='teens_home'),
    # Program Views
    path('programs/', views.IndexView.as_view(), name='programs'),
    path('kids/programs/', views.KidProgramsIndex.as_view(), name='kid_programs'),
    path('teens/programs/', views.TeenProgramsIndex.as_view(), name='teen_programs'),
    path('programs/<int:pk>', views.DetailView.as_view(), name='detail'),
    path('kids/programs/<int:pk>', views.DetailView.as_view(),
         name="kids_program_detail"),
    path('teens/programs/<int:pk>', views.DetailView.as_view(),
         name='teen_program_detail'),
    # Registration Views
    path('programs/<int:program_id>/register', views.register, name='register'),
    path('programs/<int:program_id>/add_registration',
         views.add_registration, name='add_registration'),
    path('programs/<int:program_id>/confirmed',
         views.confirmed, name='confirmation'),
    path('register/', views.grid_register, name='grid_register'),
    path('kids/register/', views.grid_register_kids, name='grid_register_kids'),
    path('teens/register/', views.grid_register_teens, name='grid_register_teens'),
    path('register/add_registration', views.add_grid_registration,
         name='add_grid_registration'),
    path('register/confirmation', views.grid_confirmation,
         name='grid_confirmation'),
    # Admin-Only Views
    path('patrons/', views.PatronsIndex.as_view(), name='patrons'),
    path('patrons/<int:pk>', views.PatronDetail.as_view(), name='patron')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
