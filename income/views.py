from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render,redirect,get_object_or_404

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
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
        i["edit"]='<a href="/income/update/{}"  class="btn btn-primary income-delete">Update</a>'.format(i['id'])
        newIncome.append(i)

    return JsonResponse(newIncome, safe=False)



import datetime
from django.db.models import Q

def todayIncomeFilter(request):
    today = datetime.date.today()
    return Income.objects.filter(user = request.user).filter( Q(created_on__year = today.year) & Q(created_on__month = today.month) & Q(created_on__day = today.day))



def weekIncomeFilter(request):
    last_7_days = datetime.date.today() - datetime.timedelta(days=7)
    return Income.objects.filter( user = request.user ).filter(created_on__gte= last_7_days)

def income_month_filter(request):
    today = datetime.date.today()
    return Income.objects.filter(user =request.user).filter( Q(created_on__year = today.year) & Q(created_on__month = today.month) )






