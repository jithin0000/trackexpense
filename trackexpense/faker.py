from faker import Faker
from customuser.models import MyUser
from expense.models import Expense
from income.models import Income
import random

cFaker = Faker()

def create_expense():
    user = MyUser.objects.get(id=2)

    expense = Expense.objects.create(
        user = user,
        name = cFaker.name(),
        amount = random.randint(45,5687),
        created_on = cFaker.date_time_this_year()
        
    )



def create_income():
    user = MyUser.objects.get(id=2)
    income = Income.objects.create(
        user = user,
        name = cFaker.name(),
        amount = random.randint(45,5687),
        created_on = cFaker.date_time_this_year()
        
    )


for i in range(45):
    create_expense()

for i in range(45):
    create_income()


