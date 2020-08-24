from django.shortcuts import render
from .models import UserToDo
import json
from django.http import JsonResponse, HttpResponse

# Create your views here.
def home(request):
	user = request.user
	userslist = user.usertodo_set.all()
	context = {
		'userslist': userslist,
	}

	return render(request, 'todolist/home.html', context)

def add_to_list(request):
	if request.method == 'POST':
		userInput = request.POST['userInput']
		if request.user.is_authenticated:
			usertodo = UserToDo(user=request.user, listitem=userInput)
			usertodo.save()
			new_item_id = usertodo.id
			data = [userInput, new_item_id]
			print(data)
			return JsonResponse(data, safe=False)

def delete_from_list(request):
	if request.method == 'POST':
		data = request.POST['item_id']
		if request.user.is_authenticated:
			item = UserToDo.objects.get(id=data)
			item.delete()
			return HttpResponse(data)

