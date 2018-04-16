from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views import generic

from .models import Program
from .models import Adult
from .models import Child
from .models import Registration


def home(request):
    programs = get_list_or_404(Program)
    return render(request, 'programs/index.html', {'programs': programs})


class HomeView(generic.ListView):
    template_name = 'home/index.html'
    context_object_name = 'programs'

    def get_queryset(self):
        '''Get next three programs.'''
        return Program.objects.exclude(date__lt=datetime.today()).order_by('date')[:5]


def kids_home(request):
    return render(request, 'home/kids.html')


def teens_home(request):
    return render(request, 'home/teens.html')


class IndexView(generic.ListView):
    template_name = 'programs/index.html'
    context_object_name = 'programs'

    def get_queryset(self):
        '''Return all programs.'''
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


class DetailView(generic.DetailView):
    model = Program
    template_name = 'programs/detail.html'


def register(request, program_id):
    program = get_object_or_404(Program, pk=program_id)
    return render(request, 'programs/register.html', {'program': program})


def grid_register(request):
    programs = get_list_or_404(Program)
    return render(request,
                  'registrations/create.html',
                  {
                      'programs': programs,
                      'type': 'teens'
                  })


def grid_register_kids(request):
    programs = get_list_or_404(Program.objects.order_by(
        'date'), is_teen=False, date__gt=datetime.today())
    return render(request,
                  'registrations/create.html',
                  {
                      'programs': programs,
                      'type': 'kids'
                  })


def grid_register_teens(request):
    programs = get_list_or_404(
        Program, is_teen=True, date__gt=datetime.today())
    return render(request,
                  'registrations/create.html',
                  {
                      'programs': programs,
                      'type': 'teens'
                  })


def add_grid_registration(request):
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

    return HttpResponseRedirect(reverse('app:grid_confirmation',
                                        args=[adult.id]))


def add_registration(request, program_id):
    program = get_object_or_404(Program, pk=program_id)

    wait_list = False
    if program.is_full:
        wait_list = True

    adult, created = Adult.objects.get_or_create(
        name=request.POST['adultname'],
        email=request.POST['adultemail']
    )

    for key in request.POST:
        if key.startswith('childname'):
            child, created = Child.objects.get_or_create(
                name=request.POST[key],
                adult=adult
            )

            registration, created = Registration.objects.get_or_create(
                program=program,
                child=child,
                is_wait_list=wait_list
            )

    if program.registration_set.count() >= program.capacity:
        program.is_full = True
        program.save()

    return HttpResponseRedirect(reverse('app:confirmation', args=(program.id,)))


# Registration Views
# ------------------

class RegistrationCreate(generic.edit.CreateView):
    '''Single Program Registration'''
    model = Registration
    success_url = reverse_lazy('programs')
    fields = ['program', 'child', 'is_wait_list']


@login_required(login_url='/admin/login/')
def patrons(request):
    patrons = get_list_or_404(Adult)
    return render(request, 'patrons/index.html', {'patrons': patrons})


@login_required(login_url='/admin/login/')
def patron_detail(request, pk):
    patron = get_object_or_404(Adult, pk=pk)
    return render(request, 'patrons/detail.html', {'patron': patron})


def confirmed(request, program_id):
    program = get_object_or_404(Program, pk=program_id)
    return render(request, 'programs/confirmation.html', {'program': program})


def grid_confirmation(request, pk):
    patron = get_object_or_404(Adult, pk=pk)
    return render(request, 'registrations/confirmation.html', {'patron': patron})
