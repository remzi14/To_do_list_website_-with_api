from django.urls import path
from .views import home,DoSerializersView,delete_todo


urlpatterns=[
    path('',home,name='saxifa'),
    path('v1/do/list',DoSerializersView.as_view()),
    path('delete/<int:pk>/',delete_todo,name='delete_todo'),

]



