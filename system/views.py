from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required as lg
from django.contrib.auth.models import User
from django.views.generic import TemplateView, FormView, ListView
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import *
# Create your views here.

@lg(login_url='account:login')
def home(request):
    if request.user.is_superuser:
        user = User.objects.count()
        return render(request, 'all/page.html', {"usercount": user})
    else:
        return redirect(reverse('system:dashboard'))


class Dashboard(LoginRequiredMixin, TemplateView):
    template_name = 'all/dshboard.html'
    login_url = 'account:login'


class CreateNaame(LoginRequiredMixin, FormView):
    form_class = CreateNaame
    template_name = 'namenegari/create.html'
    login_url = 'account:login'
    
    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            event = form.save(commit=False)
            event.author = request.user
            event.save()
            return redirect('system:namenegari')


class ListNaame(LoginRequiredMixin, ListView):
    model = NameeNegari
    template_name = 'namenegari/list.html'
    login_url = 'account:login'
