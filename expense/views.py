from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView

from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
from .models import Expense 
from django.urls import reverse_lazy
from .forms import ExpenseForm

class ExpenseListView(LoginRequiredMixin,ListView):
    """ list view for expense """
    model = Expense

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset

class ExpenseCreateView(LoginRequiredMixin,CreateView):
    """ expense create view """
    form_class=ExpenseForm
    template_name='expense/expense_form.html'

    def form_valid(self, form, *args, **kwargs):
        """ add user to user field """
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return redirect('expense_home')


class ExpenseUpdateView(LoginRequiredMixin, UpdateView):
    """ update view for income """
    queryset = Expense.objects.get_queryset()
    form_class = ExpenseForm
    template_name = "expense/expense_form.html"
    success_url = reverse_lazy('expense_home')

@login_required(login_url='/')
def get_all_expense(request):
    expenses = Expense.objects.all()
    expenses = list(expenses.values())

    newExpense = []
    for i in expenses:
        i["edit"]='<a href="/expense/detail/{}"  class="btn btn-primary income-delete">Detail</a>'.format(i['id'])
        newExpense.append(i)

    return JsonResponse(newExpense, safe=False)


class ExpenseDetailView(LoginRequiredMixin, DetailView):
    """ detail view for expense"""
    model = Expense
    queryset = Expense.objects.all()
    template_name = "expense/expense_detail.html"


@login_required(login_url='/')
def delete_expense(request,pk):
    expense = get_object_or_404(Expense, pk=pk)
    expense.delete()
    return JsonResponse({ "message" : "item deleted"}, safe=False)

