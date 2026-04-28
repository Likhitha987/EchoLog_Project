from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.db.models import Q
from .models import Scrap
from .forms import ScrapForm

@login_required
def scrap_list(request):
    # 1. Start by only getting scraps that belong to the current user
    user_scraps = Scrap.objects.filter(author=request.user)
    
    query = request.GET.get('q')
    if query:
        # 2. Filter WITHIN the user's scraps only
        scraps = user_scraps.filter(
            Q(title__icontains=query) | 
            Q(project_tag__icontains=query) |
            Q(explanation__icontains=query)
        ).distinct().order_by('-created_at')
    else:
        # 3. No search? Just show all of the user's scraps
        scraps = user_scraps.order_by('-created_at')
    
    return render(request, 'scraps/scrap_list.html', {'scraps': scraps})

@login_required
def add_scrap(request):
    if request.method == "POST":
        form = ScrapForm(request.POST)
        if form.is_valid():
            scrap = form.save(commit=False)
            scrap.author = request.user  # The Privacy Stamp
            scrap.save()
            return redirect('scrap_list')
    else:
        form = ScrapForm()
    return render(request, 'scraps/add_scrap.html', {'form': form})

@login_required
def edit_scrap(request, pk):
    # SECURITY: get_object_or_404 with author=request.user prevents URL hacking
    scrap = get_object_or_404(Scrap, pk=pk, author=request.user)
    
    if request.method == "POST":
        form = ScrapForm(request.POST, instance=scrap)
        if form.is_valid():
            form.save()
            return redirect('scrap_list')
    else:
        form = ScrapForm(instance=scrap)
    
    return render(request, 'scraps/add_scrap.html', {
        'form': form,
        'edit_mode': True,
        'scrap': scrap
    })

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('scrap_list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def delete_scrap(request, pk):
    # Security: Ensure the scrap belongs to the user
    scrap = get_object_or_404(Scrap, pk=pk, author=request.user)
    
    if request.method == "POST":
        scrap.delete()
        return redirect('scrap_list')
    
    # If they somehow hit this via GET, just send them home
    return redirect('scrap_list')