from django.shortcuts import render, redirect
from .models import Course

# Create your views here.
def index(request):
	context = {
	'courses': Course.objects.all()
	}
	return render(request, 'course/index.html', context)

def process(request):
	Course.objects.create(name=request.POST['name'], description=request.POST['description'])
	return redirect('/')


def confirm(request, id):
	request.session['current_row']=id
	row = Course.objects.filter(id=id)[0]
	context = {
	'name': row.name,
	'description': row.description
	}
	return render(request, 'course/delete.html', context)

def delete(request):
	if request.method == 'POST':
		if request.POST['confirm']== 'yes':
			Course.objects.filter(id=request.session['current_row']).delete()
		return redirect('/')
	