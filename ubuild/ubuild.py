from .models import logs,urls

def log(view_function):
	def _wrapped_view_func(request, *args, **kwargs): 
		if request.META.get("HTTP_REFERER"):
			headder=  request.META
			requestMethod= headder.get('REQUEST_METHOD')
			remoteAddr= headder.get('REMOTE_ADDR')
			httpRefer= headder.get('HTTP_REFERER') 

			log= logs(requestMethod=requestMethod,remoteAddr=remoteAddr,httpRefer=httpRefer,headder=headder)
			log.save()

			url= urls.objects.get_or_create(httpRefer=httpRefer)
			url[0].count+=1
			url[0].save()
		return view_function(request)     
	return _wrapped_view_func
