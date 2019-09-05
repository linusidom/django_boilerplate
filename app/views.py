def views_template(app_name, dst):

	app_model = app_name[:-1].title()
	app_name_short = app_name[:-1]

	content=f"""
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import (TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin
from {app_name}.models import {app_model}"""

	if app_name == 'accounts':
		content += f"""
from {app_name}.forms import {app_model}Form, {app_model}UpdateForm"""
	else:
		content += f"""
from {app_name}.forms import {app_model}Form"""


	content += f"""
	
class IndexTemplateView(TemplateView):
	template_name='{app_name}/index.html'
	
class {app_model}DeleteView(DeleteView):
	model = {app_model}
	success_url = reverse_lazy('{app_name}:{app_name_short}_list')"""

	if app_name == 'accounts':
		content += f"""
		
class {app_model}ListView(ListView):
	model = {app_model}
	
	def get_queryset(self):
		return {app_model}.objects.filter(username=self.request.user)
		
class {app_model}DetailView(DetailView):
	model = {app_model}
	
	def get_queryset(self):
		return {app_model}.objects.filter(username=self.request.user)
		
def signup(request):
	if request.method == 'POST':
		form = AccountForm(request.POST)
		if form.is_valid():
			account = form.save(commit=False)
			try:
				Account.objects.get(username__iexact=account.email)
				return render(request, 'accounts/invalid_form.html')
			except account.DoesNotExist:
				account.username = account.email
				account.save()
				return redirect('user_login')
	else:
		form = AccountForm()
	return render(request, 'accounts/signup.html', {{'form': form}})

def update_account(request, pk):
	if request.method == 'POST':
		form = AccountUpdateForm(request.POST, instance=request.user)
		if form.is_valid():
			account = form.save(commit=False)
			account.username = account.email
			account.save()
			messages.add_message(request, messages.INFO, 'Success, Account Updated!')
			return redirect('accounts:account_detail', pk=pk)
		else:
			return HttpResponse(form.errors)
	else:
		form = AccountUpdateForm(instance=request.user)
	return render(request, 'accounts/account_form.html', {{'form': form}})"""
	
	else:
		content += f"""

class {app_model}ListView(ListView):
	model = {app_model}
	
class {app_model}DetailView(DetailView):
	model = {app_model}
	
class {app_model}CreateView(CreateView):
	model = {app_model}
	form_class = {app_model}Form
	
class {app_model}UpdateView(UpdateView):
	model = {app_model}
	form_class = {app_model}Form"""

	f = open(dst, 'w')
	f.write(content)
	f.close()