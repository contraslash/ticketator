#priority views: list, create, delete

from core.models import Priority, PriorityForm
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse, Http404


#List tickets
def list_priorities(request, state_id=None):
	if request.user.is_superuser == True:
		user_list = Priority.objects.all().order_by("-id")
		return render(request, 'core/priorities/list_priorities.html', locals())
	else:
		raise Http404

def manage_priority(request, priority_id=None):
	if request.user.is_superuser == True:
		#Try to locate the object to use it as an instance and if not, create a new one to use it in a new form.
		#common_data = common_ticket_data()
		if priority_id:
			actual_priority=get_object_or_404(Priority,pk=priority_id)
		else:
			actual_priority=Priority()
		#POST mode
		if request.method == 'POST':
			form = PriorityForm(request.POST, instance=actual_priority)
			if form.is_valid():
				form.save()
				return redirect("/settings/priorities")
		else:
		#Non-POST mode, show only
			form = PriorityForm(instance=actual_priority)
		return render(request, 'core/priorities/create_edit_priority.html', locals())
	else:
		raise Http404



