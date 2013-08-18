from django.shortcuts import render
def home(request):
	return render(request,'index.html', {'MEDIA_ROOT':'Templates/'})
