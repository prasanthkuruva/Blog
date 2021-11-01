from django.shortcuts import redirect, render
from .models import BlogModel,UserModel
from .forms import Userform,Blogform
# Create your views here.

def SignUp(request):
    if request.method == 'POST':
        form = Userform(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('createpost')
    return render(request,'signup.html',{'form':Userform})
def Post(request):
    posts = BlogModel.objects.all().order_by('date_added')
    x = posts.query
    # print(x.title)
    return render(request,'view.html',{'posts':posts})

def creatpost(request):
    if request.method == 'POST':
        form = Blogform(request.POST)

        if form.is_valid(): 
            form.save(commit=True)
            return redirect('view')
    return render(request,'create.html',{'form':Blogform})

def Login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        print(email)
        emails = UserModel.objects.values_list('email',flat=True)
        print(emails)
        # x = [x for x in emails.query]
        # print(x)
        if email in emails:
            return redirect('createpost')
    return render(request,'login.html')
