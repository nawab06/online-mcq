from django.shortcuts import render
from mcqExam.models import Mcq_exam

def mcqexam(request):
    results=Mcq_exam.objects.all()
    return render(request,'index.html',{"Mcq_exam":results})