from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Posty
from django.utils import timezone
from django.shortcuts import redirect
from .forms import PostForm, UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login




def index(request):
    posty = Posty.objects.filter(data_publikacji__lte=timezone.now()).order_by("data_publikacji")
    return render(request, "Blog1/index.html", {"posts": posty})


@login_required
def nowy(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post  = form.save(commit=False)
            post.data_publikacji = timezone.now()
            post.save()
            return redirect('Blog1:wpis', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'Blog1/edycja.html', {'form': form})


def wpis(request, pk):
    post = get_object_or_404(Posty, pk=pk)
    return render (request, 'Blog1/wpis.html', {'post':post})

@login_required
def edycja(request, pk):
    post = get_object_or_404(Posty, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post  = form.save(commit=False)
            post.data_publikacji = timezone.now()
            post.save()
            return redirect('Blog1:wpis', pk= post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'Blog1/edycja.html', {'form': form})

def rejestracja_view(request):
    next = request.GET.get('next')
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('passsword')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        if next:
            return redirect(next)
        return redirect('/')
    else:
        form = UserRegisterForm()

    return render(request, "Blog1/rejestracja.html", {'form': form,})