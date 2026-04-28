from django.shortcuts import render, redirect
from .models import Scrap
from django.db.models import Q # Import Q for complex searching


def scrap_list(request):
    query = request.GET.get('q') # Get the search text from the URL
    if query:
        # Search in title, project_tag, OR the explanation
        all_scraps = Scrap.objects.filter(
            Q(title__icontains=query) | 
            Q(project_tag__icontains=query) |
            Q(explanation__icontains=query)
        ).distinct()
    else:
        all_scraps = Scrap.objects.all().order_by('-created_at')
    
    return render(request, 'scraps/scrap_list.html', {'scraps': all_scraps})


from .forms import ScrapForm # Add this import

# ... keep your scrap_list view as is ...

def add_scrap(request):
    if request.method == "POST":
        form = ScrapForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('scrap_list') # Go back to the home page after saving
    else:
        form = ScrapForm()
    return render(request, 'scraps/add_scrap.html', {'form': form})