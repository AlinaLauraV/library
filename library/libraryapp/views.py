from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .forms import OwnBookForm, NewBookForm
from .models import Books
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render (request, 'webpages/home.html')
@login_required
def show(request):
    data = {'books':Books.objects.all()}
    return render (request, 'webpages/show.html', data)

def book(request, id):
    book= get_object_or_404(Books, pk=id)
    if request.method == 'POST':
        form = OwnBookForm(request.POST)
        if form.is_valid():
            book.owner = request.user
            book.save()
            return redirect('library-book', id=id)
    else:
        form = OwnBookForm(initial= {'owner':request.user})
    data = {'book': book, 'form': form}
    return render(request, 'webpages/book.html', data)

def not_found_404(request, exception):
    data = { 'err': exception }
    return render(request, 'webpages/404.html', data)

def server_error_500(request):
    return render(request, 'webpages/500.html')

@login_required
def create(request):
    if request.method == 'POST':
        book = NewBookForm(request.POST)
        if book.is_valid():
            id = book.save().id
            return redirect('library-book', id=id)
    else:
        form = NewBookForm()
    data = {'form':form}
    return render(request, 'webpages/new.html', data)
