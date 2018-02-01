from django.shortcuts import render

def SearchHome(request):
	context = {
		"admin" : "Md Jewele Islam"
		}
	return render(request, "home/home.html", context)