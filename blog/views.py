from django.shortcuts import render, get_object_or_404
from .serializers import DoSerializer
from rest_framework.generics import ListAPIView
from .models import Do

# Create your views here.

def home(request):
    todos=Do.objects.filter(user=request.user)
    context={
        "todos":todos
    }
    return render(request,'home.html',context)


class DoSerializersView(ListAPIView):
    queryset = Do.objects.all()
    serializer_class = DoSerializer


def delete_todo(request,pk=None):
    todo=get_object_or_404(Do,id=pk)
    todo.delet()
    return render('todohome')






