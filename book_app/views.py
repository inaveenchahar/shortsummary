from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.messages import success
from django.utils.text import slugify
from django.contrib.auth import logout
from datetime import date
from .models import TagModel, BookModel
from .forms import AddBookForm, EditBookForm, SuggestionForm


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('book:home')
    else:
        return render(request, '404.html')


def home(request):
    all_tags = TagModel.objects.all()
    all_books = BookModel.objects.filter(book_publish_on__lte=date.today()).filter(publish_status=True)
    query = request.GET.get('q')
    if query:
        all_books = all_books.filter(book_title__icontains=query)
    return render(request, 'home.html', {'all_tags': all_tags, 'all_books': all_books, 'query': query})


def tag_details(request, tag_slug):
    tag = get_object_or_404(TagModel, tag_slug=tag_slug)
    tag_books = BookModel.objects.filter(tag=tag).filter(book_publish_on__lte=date.today()).filter(publish_status=True)
    return render(request, 'tag_details.html', {'tag': tag, 'tag_books': tag_books})


def book_details(request, book_slug):
    book = get_object_or_404(BookModel, book_slug=book_slug)
    return render(request, 'book_details.html', {'book': book})


def add_book(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            bookAdd = AddBookForm(request.POST or None)
            if bookAdd.is_valid():
                instance = bookAdd.save(commit=False)
                instance.book_slug = slugify(instance.book_title)
                instance.added_by = request.user
                instance.save()
                return redirect('book:home')
        else:
            bookAdd = AddBookForm()
        return render(request, 'add_book.html', {'bookAdd': bookAdd})
    else:
        return render(request, '404.html')


def edit_book(request, book_slug):
    if request.user.is_authenticated:
        book = get_object_or_404(BookModel, book_slug=book_slug)
        if request.method == 'POST':
            bookEdit = EditBookForm(request.POST, instance=book)
            if bookEdit.is_valid():
                bookEdit.save()
                return redirect('book:book_details', book.book_slug)
        else:
            bookEdit = EditBookForm(instance=book)
        return render(request, 'edit_book.html', {'bookEdit': bookEdit})
    else:
        return render(request, '404.html')  


def who_why_view(request):
    return render(request, 'who_why.html') 


def suggestion_view(request):
    if request.method == 'POST':
        s_form = SuggestionForm(request.POST or None)
        if s_form.is_valid:
            s_form.save()
            success(request, "Your suggestion has been submitted successfully.")
            return redirect("book:home")
    else:
        s_form = SuggestionForm()
    return render(request, 'suggestion_view.html', {'s_form': s_form})

