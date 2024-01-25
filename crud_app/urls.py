from django.urls import path
from . import views

urlpatterns = [
    path('', views.UserAPI.insert_emp, name='insert-emp'),
    path("register/", views.register_request, name="register"),
    # path("login/", views.login_request, name="login"),
    path('login/', views.ObtainJWTTokenView.as_view(), name='login'),
    path('show/', views.UserAPI.show_emp, name='show-emp'),
    path('edit/<int:pk>', views.UserAPI.edit_emp, name='edit-emp'),
    path('remove/<int:pk>', views.UserAPI.remove_emp, name='remove-emp')
]