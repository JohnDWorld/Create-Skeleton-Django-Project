from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View


# Create your views here.
class HomePageView(View):
    def get(self, request):
        context = {}
        return render(request, "{app_name}/homepage.html", context)
