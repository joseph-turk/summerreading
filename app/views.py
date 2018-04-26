from datetime import datetime

from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.template.loader import get_template
from django.template import Context

from .models import Program
from .models import Adult
from .models import Child
from .models import Registration


# Dates for program registrations
reg_open = datetime(2018, 4, 27, 9)


def home(request):
    '''App home page'''
    return render(request, 'home/index.html')


class ProgramList(generic.ListView):
    '''Shows a list of all programs'''
    template_name = 'programs/index.html'
    context_object_name = 'programs'

    def get_queryset(self):
        return Program.objects.order_by('date')


class ProgramDetail(generic.DetailView):
    '''Shows details for a single program'''
    model = Program
    template_name = 'programs/detail.html'


def register_kids(request):
    '''Shows registration screen for kids'''
    programs = get_list_or_404(Program.objects.order_by(
        'date'), is_teen=False, date__gt=datetime.today())

    is_open = False
    if datetime.now() > reg_open:
        is_open = True

    return render(request,
                  'registrations/create.html',
                  {
                      'programs': programs,
                      'type': 'kids',
                      'is_open': is_open
                  })


def register_teens(request):
    '''Shows registration screen for teens'''
    programs = get_list_or_404(
        Program, is_teen=True, date__gt=datetime.today())

    is_open = False
    if datetime.now() > reg_open:
        is_open = True

    return render(request,
                  'registrations/create.html',
                  {
                      'programs': programs,
                      'type': 'teens',
                      'is_open': is_open
                  })


def add_registration(request):
    '''Handles registration form submission'''

    # Check if registrations are open yet
    if datetime.now() < reg_open:
        if request.POST['registrationtype'] == 'kids':
            programs = get_list_or_404(
                Program, is_teen=False, date__gt=datetime.today())
            return redirect('app:kids_home')
        else:
            programs = get_list_or_404(
                Program, is_teen=True, date__gt=datetime.today())
            return redirect('app:teens_home')
    else:
        # Initialize list of programs to register for
        programs = []

        # Get or create Adult record
        adult, created = Adult.objects.get_or_create(
            name=request.POST['adultname'],
            email=request.POST['adultemail'],
            phone=request.POST['adultphone'],
            photo_release=request.POST['adultphotorelease']
        )

        # Add selected programs to list
        for key in request.POST:
            if key.startswith('program-'):
                program = get_object_or_404(Program, pk=key[8:])
                programs.append(program)

        # Iterate over children from form
        for key in request.POST:
            if key.startswith('childname'):
                child, created = Child.objects.get_or_create(
                    name=request.POST[key],
                    adult=adult
                )

                # Register child for program
                for program in programs:
                    registration, created = Registration.objects.get_or_create(
                        program=program,
                        child=child,
                        is_wait_list=program.is_full
                    )

                    # Update program wait list status if applicable
                    if program.registration_set.count() >= program.capacity:
                        program.is_full = True
                        program.save()

        # Create HTML Template for Email
        email_html = get_template('registrations/confirmation_email.html')
        html_content = email_html.render({'patron': adult})

        # Create Plain Text Template for Email
        email_txt = get_template('registrations/confirmation_email.txt')
        txt_content = email_txt.render({'patron': adult})

        # Send email
        send_mail(subject='Summer Reading Signup Confirmation',
                  message=txt_content,
                  from_email='efpl@test.com',
                  recipient_list=[adult.email],
                  html_message=html_content,
                  fail_silently=False)

        return HttpResponseRedirect(reverse('app:confirmation',
                                            args=[adult.id]))


def confirmation(request, pk):
    '''Shows confirmation information after registration'''
    patron = get_object_or_404(Adult, pk=pk)
    return render(request, 'registrations/confirmation.html', {'patron': patron})


@login_required(login_url='/admin/login/')
def programs(request):
    '''Shows a list of programs'''
    programs = get_list_or_404(Program.objects.order_by('date'))
    return render(request, 'programs/index.html', {'programs': programs})


@login_required(login_url='/admin/login/')
def patrons(request):
    '''Shows a list of patrons'''
    patrons = get_list_or_404(Adult)
    return render(request, 'patrons/index.html', {'patrons': patrons})


@login_required(login_url='/admin/login/')
def patron_detail(request, pk):
    '''Shows details about a single patron'''
    patron = get_object_or_404(Adult, pk=pk)
    return render(request, 'patrons/detail.html', {'patron': patron})


@login_required(login_url='/admin/login/')
def program_print(request, pk):
    '''Shows print view for a single program'''
    program = get_object_or_404(Program, pk=pk)
    return render(request, 'programs/print.html', {'program': program})
