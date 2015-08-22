from django.shortcuts import render
import os
from django.http import HttpResponse
from autourl import settings

# Create your views here.

def display(request):
	#url_params = ['GET', 'POST', 'PUT', 'DELETE']
	appname = [ app for app in settings.INSTALLED_APPS if not "django" in app ]
	return render(request,'ubuild/home.html',{'url_params': url_params})

def create(request):
	if request.method == 'POST':
		url_endpoint = request.POST['url']
		url_method = request.POST['method']
		app_name = request.POST['appname']

		CreateAutourl(url_endpoint, url_method, app_name)

class CreateAutourl(object):
	def __init__(self, url_endpoint, url_method, app_name)
		self.url_endpoint = url_endpoint
		self.url_method = url_method
		self.app_name = app_name

	def write_url_file(self):
		if os.path.exists(settings.BASE_DIR + '/' + app_name + '/' + urls.py):
			file_path = settings.BASE_DIR + '/' + app_name + '/' + urls.py
			file_handle = open(file_path, 'w')
			file_content = "\n url(r'^" + self.url_endpoint+ "/$', '"+ self.app_name + ".views." + self.url_endpoint + "')"
		else:
			file_path = settings.BASE_DIR + '/' + app_name + '/' + urls.py
			file_handle = open(file_path, 'w')
			file_content = "from django.conf.urls import include, url \n.urlpatterns = [ \n "

		file_handle.write(file_content)






