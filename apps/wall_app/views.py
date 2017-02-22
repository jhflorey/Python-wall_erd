from django.shortcuts import render
# # from .models import User


# # Create your views here.
# def index(request):
# 	print(User.objects.all())
# 	User.objects.create(first_name='Jessica', last_name='Florey', password='codingdojo17')
# 	print(User.objects.all())
# 	u = User.objects.get(id=1)
# 	print(u.first_name)
# 	u.first_name = 'Michael'
# 	u.save()
# 	j = User.objects.get(id=1)
# 	print(j.first_name)
# 	print(User.objects.get(first_name='Jessica'))
# 	
def index(request):
	return render(request, 'wall_app/index.html')