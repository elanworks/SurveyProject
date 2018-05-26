from django.shortcuts import render
from surveys import Test

# Create your views here.
def home_view(request):
	surveys = Test.objects.all().order_by('Date_Needed')
	return render(request, 'home/home_page.html', {'courses':courses})