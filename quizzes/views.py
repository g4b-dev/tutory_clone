from django.shortcuts import render, redirect
from .models import Quiz
from .forms import QuizForm

def index(request):
    quizzes = Quiz.objects.all()
    return render(request, 'quizzes/index.html', {'quizzes': quizzes})

def create_quiz(request):
    if request.method == 'POST':
        form = QuizForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = QuizForm()
    return render(request, 'quizzes/create_quiz.html', {'form': form})

def quiz_detail(request, pk):
    quiz = Quiz.objects.get(pk=pk)
    return render(request, 'quizzes/quiz_detail.html', {'quiz': quiz})
