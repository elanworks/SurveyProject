from django.shortcuts import render
from django.http import HttpResponse
from . import forms

def index(request):
	#return HttpResponse("Please Fill out a Survey")
	surveys= surveys.objects.all()
	return render(request, 'surveys/testlist.html', {'surveys':surveys, 'form':form})

def surveydetail(request, survey_id):
	return HttpResponse("You are taking Survey %s" % survey.Title)

def questionresults(request, survey_id, question_id):
	response = "These are the Results from question %s"
	return HttpResponse(response % question_id)

def surveyresults(request, survey_id):
	response = "These are the Results from Survey %s"
	return HttpResponse(response % survey_id)

def takesurvey(request, survey_id):
	return HttpResponse()
