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
    path('faq/', views.faq, name='faq'),

    # Program Views
    path('kids/events/<int:pk>',
         views.ProgramDetail.as_view(),
         name="kids_program_detail"),
    path('teens/events/<int:pk>',
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
    path('events/', views.programs, name='programs'),
    path('events/<int:pk>', views.ProgramDetail.as_view(), name='detail'),
    path('events/<int:pk>/print', views.program_print, name='print'),
    path('events/next-week/', views.programs_next_week, name='next-week'),
    path('events/send_reminders/',
         views.send_reminder_emails, name='send_reminders'),
    path('events/reminders-sent/',
         views.reminder_emails_sent, name='reminders_sent'),
    path('patrons/', views.patrons, name='patrons'),
    path('patrons/<uuid:pk>', views.patron_detail, name='patron'),
    path('patrons/<uuid:pk>/resend_confirmation',
         views.resend_confirmation, name='resend_confirmation'),
    path('patrons/<uuid:pk>/confirmation_resent',
         views.confirmation_resent, name='confirmation_resent')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
