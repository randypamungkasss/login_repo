from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from .models import Todo
from django.views import View
from django.contrib import messages

# Create your views here.
class IndexView(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        todos = Todo.objects.filter(actor=request.user)
        context = {
        "todos":todos
        }
        return render(request, "index.html", context)
    
    def post(self, request):
        title = request.POST.get("title")
        content = request.POST.get("content")

        if not title and not content:
            messages.error(request, "Isi semua kolom")
        else:
            Todo.objects.create(title=title, content=content, actor=request.user)
        return redirect('index')

class DetailView(View):
    def get(self, request, id):
        todo = Todo.objects.get(id=id)
        context = {
        "todo":todo
        }
        return render(request, "detail_view.html", context)
    
class DeleteView(View):
    def post(self, request, id):
        todo = Todo.objects.get(id=id)
        todo.delete()
        return redirect('index')

def index_view(request):
    todos = Todo.objects.all()
    context = {
        "todos":todos
    }
    return render(request, "index.html", context)

def detail_view(request, id):
    todo = Todo.objects.get(id=id)
    context = {
        "todo":todo
    }
    return render(request, "detail_view.html", context)
