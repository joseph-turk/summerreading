from datetime import datetime

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
    return render(request, 'home/index.html', {'programs': programs})


class HomeView(generic.ListView):
    template_name = 'home/index.html'
    context_object_name = 'programs'

    def get_queryset(self):
        '''Get next three programs.'''
        return Program.objects.exclude(date__lt=datetime.today()).order_by('date')[:5]


class IndexView(generic.ListView):
    template_name = 'programs/index.html'
    context_object_name = 'programs'

    def get_queryset(self):
        '''Return all programs.'''
        return Program.objects.order_by('date')


class DetailView(generic.DetailView):
    model = Program
    template_name = 'programs/detail.html'


def register(request, program_id):
    program = get_object_or_404(Program, pk=program_id)
    return render(request, 'programs/register.html', {'program': program})


def add_registration(request, program_id):
    program = get_object_or_404(Program, pk=program_id)

    wait_list = False
    if program.is_full:
        wait_list = True

    adult, created = Adult.objects.get_or_create(
        name=request.POST['adultname'],
        email=request.POST['adultemail'],
        notify=False
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


class RegistrationCreate(generic.edit.CreateView):
    model = Registration
    success_url = reverse_lazy('programs')
    fields = ['program', 'child', 'is_wait_list']


class PatronsIndex(generic.ListView):
    template_name = 'patrons/index.html'
    context_object_name = 'patrons'

    def get_queryset(self):
        '''Return all patrons.'''
        return Adult.objects.order_by('id')


class PatronDetail(generic.DetailView):
    model = Adult
    template_name = 'patrons/detail.html'


def confirmed(request, program_id):
    program = get_object_or_404(Program, pk=program_id)
    return render(request, 'programs/confirmation.html', {'program': program})
