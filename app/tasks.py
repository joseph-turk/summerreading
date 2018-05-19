from datetime import datetime, timedelta

from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, get_list_or_404
from django.template.loader import get_template

from .models import Program
from .models import Adult
from .models import Child
from .models import Registration


def send_reminder_email(patron_id):
    '''Resends a patrons confirmation email'''
    adult = get_object_or_404(Adult, pk=patron_id)

    # Create HTML Template for Email
    email_html = get_template('registrations/reminder_email.html')
    html_content = email_html.render({'patron': adult})

    # Create Plain Text Template for Email
    email_txt = get_template('registrations/reminder_email.txt')
    txt_content = email_txt.render({'patron': adult})

    # Send email
    send_mail(subject='Summer Library Event Reminder',
              message=txt_content,
              from_email='registrations@efplsummersignup.com',
              recipient_list=[adult.email],
              html_message=html_content,
              fail_silently=False)
