# -*- coding: utf-8 -*-
"""
This module implements all views 

Example:

Attributes:

Todo:

"""

import logging

from django.http import HttpResponseRedirect  # HttpResponse, Http404
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Choice, Question

LOGGER = logging.getLogger('app')


class IndexView(generic.ListView):
    """
    IndexView:
    """
    template_name = 'app/index.html'
    context_object_name = 'latest_question_list'

    LOGGER.debug('IndexView |')

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]


    """
    ResultsView:
    """
    
    data = {}
    LOGGER.debug('ResultsView | data=' + str(data))

    model = Question
    template_name = 'app/results.html'

class ExamplesView(generic.TemplateView):
    """
    ExamplesView:
    """

    data = {}
    LOGGER.debug('ExamplesView | data=' + str(data))

    template_name = 'app/examples.html'


class ExampleView(generic.TemplateView):
    """
    ExampleView:
    """

    data = {}
    LOGGER.debug('ExampleView | data=' + str(data))

    template_name = 'examples/album/index.html'


class HelpView(generic.ListView):
    """
    HelpView:
    """
    template_name = 'app/help.html'
    context_object_name = 'latest_question_list'

    LOGGER.debug('IndexView |')

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

def index(request):
    """
    """
    LOGGER.debug('index | ')

    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}

    return render(request, 'app/index.html', context)

def help(request):
    """
    """
    LOGGER.debug('help | ')

    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}

    return render(request, 'app/help.html', context)


def redirect_to_home(request):
    return redirect('/app')

def show_example(request, name=None):
    """
    """
    LOGGER.debug('show_example | name=' + name)

    data = { 'name': name}

    return render(request, 'examples/' + name + '/index.html', data)
