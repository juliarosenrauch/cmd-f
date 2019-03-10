from django.http import HttpResponse, HttpResponseRedirect # noqa: 401
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Report

class IndexView(generic.ListView):
    template_name = 'reports/index.html'
    context_object_name = 'latest_report_list'

    def get_queryset(self):
        """Return the last five published reports."""
        return Report.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Report
    template_name = 'reports/detail.html'
