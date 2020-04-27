from django.urls import path

from .views import register_user, login_user, exit_to_app


urlpatterns = [ 
        
        path('', login_user, name='login'),
        path('register', register_user, name='register'),
        path('logout', exit_to_app, name='logout')

        ]
