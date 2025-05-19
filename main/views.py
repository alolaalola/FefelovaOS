from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm, ContactForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import News
from .forms import ReviewForm
from django.utils import timezone
from .models import Review



def news(request):
    news_list = News.objects.order_by('-date')
    return render(request, 'news.html', {'news_list': news_list})

# 🏠 Главная
def index(request):
    return render(request, 'index.html')

def sitemap(request):
    return render(request, 'sitemap.html')


def portfolio(request):
    return render(request, 'portfolio.html')

def custom_404(request, exception):
    return render(request, '404.html', status=404)

def testimonials(request):
    reviews = Review.objects.filter(is_approved=True).order_by('-date')  # Только одобренные
    success = False

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.date = timezone.now()
            review.save()
            success = True
    else:
        form = ReviewForm()

    return render(request, 'testimonials.html', {
        'reviews': reviews,
        'form': form,
        'success': success
    })

# 🧾 Услуги
def services(request):
    return render(request, 'services.html')

# 📬 Контакты с формой обратной связи
def contacts(request):
    success = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            success = True
    else:
        form = ContactForm()
    return render(request, 'contacts.html', {'form': form, 'success': success})

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




@login_required
def profile_view(request):
    return render(request, 'profile.html')


