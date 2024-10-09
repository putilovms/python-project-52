from django.urls import path
from task_manager.users import views


urlpatterns = [
    path('', views.UsersListView.as_view(), name="users"),
    path('create/', views.RegistrationView.as_view(), name="registration"),
    path('<int:pk>/delete/', views.UserDeleteView.as_view(), name="delete"),
    path('<int:pk>/update/', views.UserUpdateView.as_view(), name="update"),
]