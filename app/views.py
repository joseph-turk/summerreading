from datetime import datetime

from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.template.loader import get_template
from django.template import Context

from .models import Program
from .models import Adult
from .models import Child
from .models import Registration


# GET: /
def home(request):
    return render(request, 'home/index.html')


# GET: /programs
class ProgramList(generic.ListView):
    template_name = 'programs/index.html'
    context_object_name = 'programs'

    def get_queryset(self):
        return Program.objects.order_by('date')


class KidProgramsIndex(generic.ListView):
    template_name = 'programs/index.html'
    context_object_name = 'programs'

    def get_queryset(self):
        '''Return all kids programs.'''
        return Program.objects.exclude(is_teen=True).order_by('date')


class TeenProgramsIndex(generic.ListView):
    template_name = 'programs/index.html'
    context_object_name = 'programs'

    def get_queryset(self):
        '''Return all teen programs.'''
        return Program.objects.exclude(is_teen=False).order_by('date')


class ProgramDetail(generic.DetailView):
    model = Program
    template_name = 'programs/detail.html'


def register_kids(request):
    programs = get_list_or_404(Program.objects.order_by(
        'date'), is_teen=False, date__gt=datetime.today())
    return render(request,
                  'registrations/create.html',
                  {
                      'programs': programs,
                      'type': 'kids'
                  })


def register_teens(request):
    programs = get_list_or_404(
        Program, is_teen=True, date__gt=datetime.today())
    return render(request,
                  'registrations/create.html',
                  {
                      'programs': programs,
                      'type': 'teens'
                  })


def add_registration(request):
    programs = []

    adult, created = Adult.objects.get_or_create(
        name=request.POST['adultname'],
        email=request.POST['adultemail'],
        phone=request.POST['adultphone']
    )

    for key in request.POST:
        if key.startswith('program-'):
            program = get_object_or_404(Program, pk=key[8:])
            programs.append(program)

    for key in request.POST:
        if key.startswith('childname'):
            child, created = Child.objects.get_or_create(
                name=request.POST[key],
                adult=adult
            )

            for program in programs:
                registration, created = Registration.objects.get_or_create(
                    program=program,
                    child=child,
                    is_wait_list=program.is_full
                )

                if program.registration_set.count() >= program.capacity:
                    program.is_full = True
                    program.save()

    # Create HTML Template for Email
    email_html = get_template('registrations/confirmation_email.html')
    html_content = email_html.render({'patron': adult})

    send_mail(subject='Summer Reading Signup Confirmation',
              message='If it works, this message was sent with the API, rather than just SMTP.',
              from_email='efpl@test.com',
              recipient_list=[adult.email],
              html_message=html_content,
              fail_silently=False)

    return HttpResponseRedirect(reverse('app:confirmation',
                                        args=[adult.id]))


@login_required(login_url='/admin/login/')
def patrons(request):
    patrons = get_list_or_404(Adult)
    return render(request, 'patrons/index.html', {'patrons': patrons})


@login_required(login_url='/admin/login/')
def patron_detail(request, pk):
    patron = get_object_or_404(Adult, pk=pk)
    return render(request, 'patrons/detail.html', {'patron': patron})


def confirmation(request, pk):
    patron = get_object_or_404(Adult, pk=pk)
    return render(request, 'registrations/confirmation.html', {'patron': patron})
