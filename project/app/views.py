from django.shortcuts import render
from .models import Student


#Create your views here.
def home(request):
    return render(request,"home.html")

def variants(request):
    return render(request,"variants.html")

def series(request):
    data={'Model':'BMW 3-Series','Engine':'Twin-turbo',
           'Price':'Rs 6500000','Type':'Sports-sedan'}
    return render(request,'series.html',data)

def registration(request):
    return render(request,'registration.html')

def registerdata(request):
    print(request.FILES)
    print(request.method)
    print(request.POST)
    if request.method == 'POST':
        my_name =  request.POST.get('name')
        my_email =  request.POST.get('email')
        my_contact =  request.POST.get('contact')
        my_image =  request.FILES.get('profileImage')
        my_resume =  request.FILES.get('resume')
        save_data = Student.objects.create(stu_name=my_name,stu_email=my_email,stu_contact=my_contact,stu_image=my_image,stu_resume=my_resume)
        print("Data saved successfully..............")
        all_data = Student.objects.all()
        print(all_data)
        print(all_data.values())
        data = {
            'data':all_data.values()
        }
        return render(request,'new.html',data)





    # print(my_name)
    # print(my_email)
    # print(my_contact)
    # print(my_image)
    # print(my_resume)
    