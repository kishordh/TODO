
from app.views import home, login, signup,add_todo,signout,delete_todo,change_todo
from django.urls import path

urlpatterns = [
    path('',home, name='home'),
    path('login/', login, name='login'),
    path('signup/', signup, name='logout'),
    path('add-todo/', add_todo, name='add_todo'),
    path('logout/', signout, name='logout'),
    path('delete-todo/<int:id>', delete_todo),
    path('change-status<int:id>/<str:status>', change_todo)
    # path('delete-todo/<int:id>', delete_todo)
]


