from django.shortcuts import render, redirect

from .models import Question, Answer


def index(request):
    context = {
        'questions': Question.objects.all(),
    }
    return render(request, 'index.html', context)


def detail(request, id):
    context = {
        'question': Question.objects.get(id=id),
    }
    return render(request, 'detail.html', context)


def create(request):
    if request.method == 'POST':
        Question.objects.create(content=request.POST.get('content'))
        return redirect('question:index')
    else:
        return render(request, 'form.html')


def answer_create(request, question_id):
    if request.method == 'POST':
        Answer.objects.create(
            question=Question.objects.get(id=question_id),
            content=request.POST.get('content')
        )
        return redirect('question:detail', question_id)
    else:
        return render(request, 'detail.html')


def answer_delete(request, question_id, answer_id):
    Answer.objects.get(id=answer_id).delete()
    return redirect('question:detail', question_id)
