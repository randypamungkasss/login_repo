from django.shortcuts import render, redirect
from django.views import View

# Create your views here.
class RegisterView(View):
    def get(self, request):
        return render(request, "register.html")

    def post(request):
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        return redirect('register')