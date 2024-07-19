from django.shortcuts import render, redirect
from .models import Obituary
from django.utils.text import slugify

def submit_obituary(request):
    if request.method == 'POST':
        name = request.POST['name']
        date_of_birth = request.POST['date_of_birth']
        date_of_death = request.POST['date_of_death']
        content = request.POST['content']
        author = request.POST['author']
        slug = slugify(name)

        obituary = Obituary(
            name=name,
            date_of_birth=date_of_birth,
            date_of_death=date_of_death,
            content=content,
            author=author,
            slug=slug
        )
        obituary.save()
        return redirect('view_obituaries')
    return render(request, 'obituary_form.html')

def view_obituaries(request):
    obituaries = Obituary.objects.all()
    return render(request, 'view_obituaries.html', {'obituaries': obituaries})
