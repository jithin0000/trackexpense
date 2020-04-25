from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render,redirect,get_object_or_404

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView
from .forms import IncomeForm

from income.models import Income
# Create your views here.

class IncomeListView(LoginRequiredMixin,ListView):
    """ list view for income """
    model = Income

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset


class IncomCreateView(LoginRequiredMixin, CreateView):
    """ create view for income """
    form_class = IncomeForm
    template_name="income/income_form.html"
    success_url=reverse_lazy('income_list')

    def form_valid(self, form,*args, **kwargs):
        self.object=form.save(commit=False)
        self.object.user =self.request.user
        self.object.save()
        return redirect(self.get_success_url())

class IncomeDetailView(LoginRequiredMixin, DetailView):
    """ detail view for expense"""
    model = Income
    queryset = Income.objects.all()
    template_name = "income/income_detail.html"


class IncomeUpdateView(LoginRequiredMixin, UpdateView):
    """ update view for income """
    queryset = Income.objects.get_queryset()
    form_class = IncomeForm
    template_name = "income/income_form.html"
    success_url = reverse_lazy('income_list')

@login_required(login_url='/login')
def delete_income(request,pk):
    """ delete income by id ajax request"""

    income = get_object_or_404(Income, pk=pk)
    id = income.id
    income.delete()
    return JsonResponse({"id" : id})


@login_required(login_url='/login')
def get_alll_income(request):
    incomes = Income.objects.all()
    incomes = list(incomes.values())

    newIncome = []
    for i in incomes:
        i["edit"]='<a href="/income/detail/{}"  class="btn btn-primary income-delete">Edit</a>'.format(i['id'])
        newIncome.append(i)

    return JsonResponse(newIncome, safe=False)





