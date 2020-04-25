from django.urls import path

from .views import ExpenseListView, ExpenseCreateView,get_all_expense,ExpenseUpdateView,ExpenseDetailView,delete_expense




urlpatterns = [
        
        path('', ExpenseListView.as_view(), name='expense_home'),
        path('new', ExpenseCreateView.as_view(), name='expense_create'),
        path('all', get_all_expense, name='all_expense'),
        path('update/<int:pk>', ExpenseUpdateView.as_view(), name='update_expense'),
        path('detail/<int:pk>', ExpenseDetailView.as_view(), name='expense_detail'),
        path('delete/<int:pk>', delete_expense, name='expense_delete'),


        ]
