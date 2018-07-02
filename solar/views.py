from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from .tasks import my_task

# Create your views here.
class HomeView(View):
    def get(self, request, format=None):
        my_task.delay()
        return HttpResponse(content="<h1>It Works!</h1>", status=200)
