from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm


# 🏠 Главная
def index(request):
    return render(request, 'index.html')

# 🧾 Услуги
def services(request):
    return render(request, 'services.html')

# 📬 Контакты с формой
def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f"[ОБРАТНАЯ СВЯЗЬ] Имя: {name}, Email: {email}, Сообщение: {message}")
        return HttpResponse("Спасибо за сообщение!")
    return render(request, 'contacts.html')


# 🔐 Авторизация
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


# 🚪 Выход
def logout_view(request):
    logout(request)
    return redirect('index')


# 🧾 Регистрация
def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})
