from django.shortcuts import render
from .forms import StudentDetailsForm, BookForm
from .models import StudentDetails, Book

def home(request):
 return render(request,'home.html')
 
def about(request):
 return render(request,'about.html')
 
def add_student(request):
    if request.method == 'POST':
        form = StudentDetailsForm(request.POST)
        if form.is_valid():
            form.save()
            students = StudentDetails.objects.all()
            return render(request, 'student_list.html', {'students': students, 'success': True})
    else:
        form = StudentDetailsForm()
    return render(request, 'add_student.html', {'form': form, 'success': False})

def student_list(request):
    students = StudentDetails.objects.all()
    return render(request, 'student_list.html', {'students': students})

def edit_student(request, student_id):
    student = StudentDetails.objects.get(id=student_id)
    if request.method == 'POST':
        form = StudentDetailsForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            students = StudentDetails.objects.all()
            return render(request, 'student_list.html', {'students': students, 'success': True})
    else:
        form = StudentDetailsForm(instance=student)
    return render(request, 'edit_student.html', {'form': form, 'success': False})

def delete_student(request, student_id):
    student = StudentDetails.objects.get(id=student_id)
    student.delete()
    return render(request,'student_list.html', {'students': StudentDetails.objects.all(), 'success': True})

# BOOK VIEWS

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            books = Book.objects.all()
            return render(request, 'book_list.html', {'books': books, 'success': True})
    else:
        form = BookForm()
    return render(request, 'add_book.html', {'form': form, 'success': False})

def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

def edit_book(request, book_id):
    book = Book.objects.get(id=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            books = Book.objects.all()
            return render(request, 'book_list.html', {'books': books, 'success': True})
    else:
        form = BookForm(instance=book)

    return render(request, 'edit_book.html', {'form': form, 'success': False})

def delete_book(request, book_id):
    book = Book.objects.get(id=book_id)
    book.delete()
    return render(request,'book_list.html', {'books': Book.objects.all(), 'success': True})