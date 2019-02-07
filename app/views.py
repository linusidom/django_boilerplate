def views_template(app_name, dst):

	content="\
from django.shortcuts import render, redirect\n\
from django.urls import reverse_lazy\n\
from django.contrib import messages\n\
from django.views.generic import (TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView)\n\
from django.contrib.auth.mixins import LoginRequiredMixin\n\
from "+app_name+".models import "+app_name[0:-1].title()+"\n"

	if app_name == 'accounts':
		content += "\
from "+app_name+".forms import "+app_name[0:-1].title()+"Form, "+app_name[0:-1].title()+"UpdateForm\n\
\n"
	else:
		content += "from "+app_name+".forms import "+app_name[0:-1].title()+"Form\n\
\n"


	content += "\
class IndexTemplateView(TemplateView):\n\
	template_name='"+app_name+"/index.html'\n\
	\n\
class "+app_name[0:-1].title()+"DeleteView(LoginRequiredMixin, DeleteView):\n\
	model = "+app_name[0:-1].title()+"\n\
	success_url = reverse_lazy('"+app_name+":"+app_name[0:-1]+"_list')\n\n"

	if app_name == 'accounts':
		content += "\
class "+app_name[0:-1].title()+"ListView(LoginRequiredMixin, ListView):\n\
	model = "+app_name[0:-1].title()+"\n\
	\n\
	def get_queryset(self):\n\
		return "+app_name[0:-1].title()+".objects.filter(username=self.request.user)\n\
		\n\
class "+app_name[0:-1].title()+"DetailView(LoginRequiredMixin, DetailView):\n\
	model = "+app_name[0:-1].title()+"\n\
	\n\
	def get_queryset(self):\n\
		return "+app_name[0:-1].title()+".objects.filter(username=self.request.user)\n\
		\n\
def signup(request):\n\
	if request.method == 'POST':\n\
		form = AccountForm(request.POST)\n\
		if form.is_valid():\n\
			account = form.save(commit=False)\n\
			try:\n\
				Account.objects.get(username__iexact=account.email)\n\
				return render(request, 'accounts/invalid_form.html')\n\
			except account.DoesNotExist:\n\
				account.username = account.email\n\
				account.save()\n\
				return redirect('user_login')\n\
	else:\n\
		form = AccountForm()\n\
	return render(request, 'accounts/signup.html', {'form': form})\n\
\n\
def update_account(request, pk):\n\
	if request.method == 'POST':\n\
		form = AccountUpdateForm(request.POST, instance=request.user)\n\
		if form.is_valid():\n\
			account = form.save(commit=False)\n\
			account.username = account.email\n\
			account.save()\n\
			messages.add_message(request, messages.INFO, 'Success, Account Updated!')\n\
			return redirect('accounts:account_detail', pk=pk)\n\
		else:\n\
			return HttpResponse(form.errors)\n\
	else:\n\
		form = AccountUpdateForm(instance=request.user)\n\
	return render(request, 'accounts/account_form.html', {'form': form})"
	
	else:
		content += "\
class "+app_name[0:-1].title()+"ListView(LoginRequiredMixin, ListView):\n\
	model = "+app_name[0:-1].title()+"\n\
	\n\
	def get_queryset(self):\n\
		return "+app_name[0:-1].title()+".objects.filter(user=self.request.user)\n\
		\n\
class "+app_name[0:-1].title()+"DetailView(LoginRequiredMixin, DetailView):\n\
	model = "+app_name[0:-1].title()+"\n\
	\n\
	def get_queryset(self):\n\
		return "+app_name[0:-1].title()+".objects.filter(user=self.request.user)\n\
		\n\
class "+app_name[0:-1].title()+"CreateView(LoginRequiredMixin, CreateView):\n\
	model = "+app_name[0:-1].title()+"\n\
	form_class = "+app_name[0:-1].title()+"Form\n\
	\n\
	def form_valid(self, form):\n\
		form.instance.user = self.request.user\n\
		return super("+app_name[0:-1].title()+"CreateView, self).form_valid(form)\n\
		\n\
class "+app_name[0:-1].title()+"UpdateView(LoginRequiredMixin, UpdateView):\n\
	model = "+app_name[0:-1].title()+"\n\
	form_class = "+app_name[0:-1].title()+"Form"

	f = open(dst, 'w')
	f.write(content)
	f.close()