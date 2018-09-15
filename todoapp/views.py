from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from .forms import TodoForm
# Create your views here.
def index(request):
	#get all the objects by id (it will be sequential)
	todo_list = Todo.objects.order_by('id')

	#create an empty form
	form = TodoForm()

	#if form is submitted, we save it to the console and redirect to
	#home
	if request.method == 'POST':

		form = TodoForm(request.POST)
		if form.is_valid():
			#if we get cleaned data, save it to the database
			list_form = form.save(commit=False)
			list_form.complete = False
			list_form.save()
			return redirect('home')
	#if the form is empty or no post request has been done, just
	#send empty form to the template
	return render(request, 'todoapp/index.html', {'todo_list':todo_list, 'form':form})

def completeaddTodo(request, todo_id):
	#takes in all the form data from the form
	item = get_object_or_404(Todo, pk=todo_id)
	item.complete = True
	item.save()
	return redirect('home')

def deleteComplete(request):
	#search the database that has the complete attribute as True
	#then delete (note we can acheive all this using filter function and
	# delet() method in one line)
	Todo.objects.filter(complete__exact=True).delete()
	return redirect('home')

def deleteall(request):
	#delet all objects
	Todo.objects.all().delete()
	return redirect('home')

def edit(request, todo_id=None):
	todo = get_object_or_404(Todo, pk=todo_id)
	form = TodoForm(instance=todo)
	if request.method == 'POST':
		form = TodoForm(instance=todo, data=request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')
	return render(request, 'todoapp/edit_list.html', {'form':form})