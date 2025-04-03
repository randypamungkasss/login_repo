from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User

# Create your views here.
class RegisterView(View):
    def get(self, request):
        return render(request, "register.html")

    def post(request):
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        new_user = User.objects.create_user(username=username, email=email, password=password)
        print(new_user)

        return redirect('register')