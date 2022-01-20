
from django.core.files.storage import FileSystemStorage
from django.core.mail import send_mail

from django.http import HttpResponse
from django.shortcuts import render, redirect

from mainpro.settings import EMAIL_HOST_USER
from .forms import RestForm, EmployeeForm


# Create your views here.
from .models import Rest_Reg, Ngo_Reg, Admin_Reg, Employee



def index(request):

    reg=RestForm()
    return render(request,'index.html',{'form':reg})

#restaurent

# def login(request):
#
#     log=LoginForm()
#     return render(request,'restaurant/restregitration.html', {'form': log})

def add_res(request):

    if request.method == "POST":

        upload_file1 = request.FILES['image']
        fs = FileSystemStorage()
        fname1 = upload_file1.name
        fdata1 = fs.save(fname1, upload_file1)
        uploaded_url1 = fs.url(fdata1)

        upload_file2 = request.FILES['info']
        fs = FileSystemStorage()
        fname2 = upload_file2.name
        fdata2 = fs.save(fname2, upload_file2)
        uploaded_url2 = fs.url(fdata2)

        obj=Rest_Reg(name=request.POST.get("fname"),
                     username=request.POST.get("user"),
                     postcode=request.POST.get("post"),
                     address=request.POST.get("add"),
                     registration_number=request.POST.get("reg"),
                     phone=request.POST.get("phone"),
                     email=request.POST.get("email"),
                     password=request.POST.get("pwd"),
                     images=uploaded_url1,
                     info=uploaded_url2)
        obj.save()
        return render(request, 'restaurant/restregitration.html')

    return render(request, 'restaurant/restregitration.html')

def update_email(request):

    if request.method=='POST':

        res = Rest_Reg.objects.get(id=request.POST.get('rid'))
        res.email=request.POST.get('email')
        res.phone=request.POST.get('phone')
        res.save()
        obj=Rest_Reg.objects.all()
        return render(request, 'restaurant/viewrestaurants.html',{'form':obj})
    return render(request,'restaurant/updateemail.html',)



def update_res(request):

    if request.method=='POST':
        obj=Rest_Reg.objects.filter(id=request.POST.get('rid'))
        return render(request,'restaurant/viewrestaurants.html',{'form':obj})

    obj1=Rest_Reg.objects.all()

    return render(request,'restaurant/viewrestaurants.html',{'form':obj1})



def update_ngo(request):
    # if request.method == 'POST':
    #     obj = Rest_Reg.objects.filter(id=request.POST.get('nid'))
    #     return render(request, 'ngo/view.html', {'form': obj})
    #
    # obj1 = Rest_Reg.objects.all()
    #
    # return render(request, 'restaurant/viewrestaurants.html', {'form': obj1})

    return render(request,'ngo/updatengo.html')


def view_rest(request):

    obj2=Rest_Reg.objects.all()

    return render(request, 'admin/viewrestaurants.html',{'res':obj2})



def list_ngo(request):
    if request.method == 'POST':
        obj=Ngo_Reg.objects.filter(address=request.POST.get('adrs'))

        return render(request,'restaurant/viewngoR.html',{'listngo':obj})
    obj4=Ngo_Reg.objects.all()

    return render(request, 'restaurant/viewngoR.html',{'listngo':obj4})



def logout_res(request):
    try:
        request.session['sid'].delete()
        return render(request,'index.html')
    except:
        return render(request, 'index.html')


def add_ngo(request):

    if request.method == "POST":


        upload_file1=request.FILES['pic']
        fs=FileSystemStorage()
        fname1=upload_file1.name
        fdata1=fs.save(fname1,upload_file1)
        uploaded_url1=fs.url(fdata1)

        upload_file2=request.FILES['docs']
        fs=FileSystemStorage()
        fname2=upload_file2.name
        fdata2=fs.save(fname2,upload_file2)
        uploaded_url2=fs.url(fdata2)

        obj1=Ngo_Reg(name=request.POST.get("fname"),
                     institution_name=request.POST.get("insti"),
                     address=request.POST.get("add"),
                     postcode=request.POST.get("pcode"),
                     email=request.POST.get("email"),
                     phone=request.POST.get("phone"),
                     username=request.POST.get("user"),
                     password=request.POST.get("pwd"),
                     images=uploaded_url1,
                     info=uploaded_url2)

        obj1.save()
        return render(request, 'ngo/viewrestN.html')
    return render(request,'ngo/ngoregistration.html')


def send_emailngo(request):
    print('one')

    if request.method == 'POST':

        print('two')
        subject = request.POST.get('sub')
        message=request.POST.get('msg')
        loc=request.POST.get('adrs')
        print(subject)
        print(message)
        print(loc)

        ngo_obj=Ngo_Reg.objects.filter(address=request.POST.get('adrs'))

        for ngo in ngo_obj:

            res=str(ngo.email)

            print(res)
            
            obj=Rest_Reg.objects.get(username=request.session['sid'])
            from_mail='Regards,\n{}\n{}\n{}'.format(obj.name,obj.email,obj.phone)
            msg='hai {}'.format(ngo.name)+'\n'+message+'\n'+from_mail
            send_mail(subject,msg,EMAIL_HOST_USER,[res],fail_silently=False)
            from_mail=msg=""

        return render(request, 'restaurant/ngoemail.html')
    return render(request, 'restaurant/ngoemail.html')

def ngo_email(request):

    if request.method == 'POST':

        obj = Ngo_Reg.objects.filter(address=request.POST.get('adrs'))

        return render(request, 'restaurant/ngoemail.html', {'listngo':obj,'loc':request.POST.get('adrs')})

        obj4 = Ngo_Reg.objects.all()

        return render(request, 'restaurant/ngoemail.html', {'listngo': obj4})

    return render(request, 'restaurant/ngoemail.html')

def rest_email(request):

    if request.method=='POST':

        obj=Rest_Reg.objects.filter(address=request.POST.get('adrs'))
        return render(request,'ngo/emailtorest.html',{'listrest':obj,'loc':request.POST.get('adrs')})

        obj3=Rest_Reg.objects.all()
        return render(request,'ngo/emailtorest.html',{'listrest':obj3})
    return render(request, 'ngo/emailtorest.html')

def send_emailrest(request):

    if request.method=='POST':

        subject=request.POST.get('sub')
        message=request.POST.get('msg')
        loc=request.POST.get('adrs')
        print(subject)
        print(message)
        print(loc)


        rest_obj=Rest_Reg.objects.filter(address=request.POST.get('adrs'))

        for rest in rest_obj:
            rec=str(rest.email)
            print(rec)

            obj=Ngo_Reg.objects.get(username=request.session['sid'])

            fromemail='Regards,\n{}\n{}\n{}'.format(obj.name,obj.email,obj.phone)

            msg='hai{}'.format(rest.name)+'\n'+message+'\n'+fromemail

            send_mail(subject,msg,EMAIL_HOST_USER,[rec],fail_silently= False)

        return render(request,'ngo/emailtorest.html')

    return render(request,'ngo/emailtorest.html')


def emp_email(request):


    if request.method == 'POST':

        obj1 = Employee.objects.filter(address=request.POST.get('adrs'))

        return render(request, 'ngo/emp_email.html', {'listemployee': obj1,'loc': request.POST.get('adrs')})

        obj = Employee.objects.all()

        return render(request, 'ngo/emp_email.html', {'listemployee': obj})

    return render(request, 'ngo/emp_email.html')


def employee_list(request):

    if request.method == 'POST':

        obj1=Employee.objects.filter(address=request.POST.get('adrs'))

        return render(request,'ngo/employeelist.html',{'listemployee':obj1})

    obj=Employee.objects.all()

    return render(request,'ngo/employeelist.html',{'listemployee':obj})

def send_emailemp(request):
    print('one')

    if request.method == 'POST':
        print('two')

        subject=request.POST.get('sub')
        message=request.POST.get('msg')
        loc=request.POST.get('adrs')
        print(loc)

        emp_obj=Employee.objects.filter(address=request.POST.get('adrs'))

        for emp in emp_obj:
            rec = str(emp.email)

            obj=Ngo_Reg.objects.get(username=request.session['sid'])

            from_email='Regards,\n{}\n{}\n{}'.format(obj.name,obj.email,obj.phone)

            msg='hai{}'.format(emp.name)+'\n'+message+'\n'+from_email

            send_mail(subject,msg,EMAIL_HOST_USER,[rec],fail_silently= False)

        return render(request,'ngo/emp_email.html')

    return render(request,'ngo/emp_email.html')

def view_ngo(request):

    obj3=Ngo_Reg.objects.all()

    return render(request, 'admin/viewngo.html',{'ngo':obj3})


def list_rest(request):

    if request.method == "POST":
        obj = Rest_Reg.objects.filter(address=request.POST.get('adrs'))

        return render(request,'ngo/viewrestN.html',{'listrest': obj})

    obj5=Rest_Reg.objects.all()

    return render(request,'ngo/viewrestN.html',{'listrest': obj5})

def employee_reg(request):

    emp=EmployeeForm
    return render(request,'ngo/empregistration.html',{'form':emp})


def employee_add(request):

    if request.method =="POST":

        emp=Employee(name=request.POST.get('name'),
                     address=request.POST.get('address'),
                     phone=request.POST.get('phone'),
                     email=request.POST.get('email'))
        emp.save()
    emp = EmployeeForm
    return render(request,'ngo/empregistration.html',{'form':emp})




def del_ngodata(request):

    dt=Ngo_Reg.objects.all()

    if request.method=='POST':

        Ngo_Reg.objects.get(id=request.POST.get('nid')).delete()

    return render(request,'admin/viewngo.html',{'ngo':dt})

def logout_ngo(request):

    try:
        request.session ['sid'].delete()
        return render(request,'index.html')

    except:
        return render(request, 'index.html')



#admin

def admin_view(request):
    return render(request,'admin/adminview.html')

def rest_base(request):
    return render(request,'restaurant/restaurentbase.html')


def delete_resdata(request):

    dt = Rest_Reg.objects.all()

    if request.method == 'POST':

        Rest_Reg.objects.get(id=request.POST.get('rid')).delete()

        return render(request,'admin/viewrestaurants.html',{'res': dt})

    return render(request, 'admin/viewrestaurants.html',{'res': dt})



def index_login(request):

        utype = request.POST.get('utype')

        user = request.POST.get('uname')

        pd = request.POST.get('pword')

        # print('utype:{} uname:{} pword:{}'.format(utype,user,pd))

        if utype == 'Admin':
            try:

                if Admin_Reg.objects.get(Username=user) is not None:
                    a = Admin_Reg.objects.get(Username=user)
                    if pd == a.Password:
                        request.session['sid'] = a.Username
                        return render(request,'admin/adminview.html')

                    else:
                        # return render(request,'index.html',{'msg':'incorrect password'})
                        return HttpResponse('incorrect password')

            except:
                return render(request, 'index.html',{'msg':'username doesnt exist'})

        elif utype == 'Restaurants':
            try:

                if Rest_Reg.objects.get(username=user) is not None:

                    r=Rest_Reg.objects.get(username=user)
                    if pd == r.password:
                        request.session['sid'] = r.username

                        return redirect ('/list_ngo/')

                    else:

                        return HttpResponse('incorrect password')
            except:

                return render(request, 'index.html',{'msg':'username doesnt exist'})

        else:
            try:
                if Ngo_Reg.objects.get(username=user) is not None:

                    n=Ngo_Reg.objects.get(username=user)

                    if pd == n.password:
                        request.session['sid'] = n.username
                        return redirect('/list_rest/')

                    else:
                        return HttpResponse ('incorrect password')
            except:
                return render(request, 'index.html', {'msg': 'username doesnt exist'})

def logout_admin(request):
    try:
        request.session['sid'].delete()
        return render(request,'index.html')
    except:
        return render(request, 'index.html')





















