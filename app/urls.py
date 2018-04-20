import uuid
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views


app_name = 'app'
urlpatterns = [
    # Home Views
    path('', views.home, name='home'),
    path('kids/', views.register_kids, name='kids_home'),
    path('teens/', views.register_teens, name='teens_home'),

    # Program Views
    path('kids/programs/<int:pk>',
         views.ProgramDetail.as_view(),
         name="kids_program_detail"),
    path('teens/programs/<int:pk>',
         views.ProgramDetail.as_view(),
         name='teen_program_detail'),

    # Registration Views
    path('register/add_registration',
         views.add_registration,
         name='add_registration'),
    path('register/confirmation/<uuid:pk>',
         views.confirmation,
         name='confirmation'),

    # Admin-Only Views
    path('programs/', views.programs, name='programs'),
    path('programs/<int:pk>', views.ProgramDetail.as_view(), name='detail'),
    path('programs/<int:pk>/print', views.program_print, name='print'),
    path('patrons/', views.patrons, name='patrons'),
    path('patrons/<uuid:pk>', views.patron_detail, name='patron')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
