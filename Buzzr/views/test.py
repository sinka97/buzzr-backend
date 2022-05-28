from django.http import HttpResponse
from django.shortcuts import render


def test_webpage(request):
    latest_question_list = ["Is this working?", "Are we working?", "Should we rethink us?"]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'test/index.html', context)
