

from django.shortcuts import render , redirect
from Cattle import settings
from django.contrib import messages
from django.contrib.auth import logout
from django.core.mail import send_mail
from .forms import contactform, buyerform, sellerform, cattleform,buyerresetform, sellerresetform
from .models import buyer, seller, cattler, registration
from django.db.models import Q
from myapp import Checksum
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from django.http import HttpResponse


def index(request):
    user = request.session.get('user')
    return render(request, 'index.html',{'user':user})

def about(request):
    return render(request, 'about.html')

def aboutbuyer(request):
    return render(request, 'aboutbuyer.html')

def contactusbuyer(request):
    if request.method == 'POST':
        conform = contactform(request.POST)
        if conform.is_valid():
            conform.save()
            email_subject = f'New contact {conform.cleaned_data["number"]} number add your {conform.cleaned_data["name"]}'
            email_message = conform.cleaned_data['massage']
            to_email = [conform.cleaned_data['email']]
            send_mail(email_subject, email_message, settings.EMAIL_HOST_USER, to_email)
            messages.info('your contact is email send succesfully')
            return redirect('index')
        else:
            
            print(conform.errors)               
    return render(request, 'contactbuyer.html')

def indexbuyer(request):
    user = request.session.get('user')
    return render(request, 'indexbuyer.html',{'user':user})



def contactus(request): 
    if request.method == 'POST':
        conform = contactform(request.POST)
        if conform.is_valid():
            conform.save()
            email_subject = f'New contact {conform.cleaned_data["number"]} number add your {conform.cleaned_data["name"]}'
            email_message = conform.cleaned_data['massage']
            to_email = [conform.cleaned_data['email']]
            send_mail(email_subject, email_message, settings.EMAIL_HOST_USER, to_email)
            messages.info('your contact is email send succesfully')
            return redirect('index')
        else:
            
            print(conform.errors)               
    return render(request, 'contact.html')

def signup(request):
    if request.method == 'POST':
        cname = request.POST.get('cname')
        email= ""
        
        if cname == 'buyer':
            buser = buyerform(request.POST)
            if buser.is_valid():
                email = buser.cleaned_data.get('email')
                try:
                    em = buyer.objects.get(email=email)
                    print("Username is already exists!")
                    messages.error(request,"Username is already exists!")
                except buyer.DoesNotExist:
                    buser.save()
                    print("buyer singup succesfully")
                    return redirect('indexbuyer')
            else:
                print(buser.errors)
        elif cname == 'seller':
            suser = sellerform(request.POST)
            if suser.is_valid():
                email = suser.cleaned_data.get('email')
                try:
                    em = seller.objects.get(email=email)
                    print("Username is already exists!")
                    messages.error(request,"Username is already exists!")
                except seller.DoesNotExist:
                    suser.save()
                    print("seller singup succesfully")
                    return redirect('index')
            else:
                print(suser.errors)
            
    return render(request, 'signup.html')

def signin(request):
    if request.method == 'POST':
        cname = request.POST.get('cname')
        if cname == 'buyer':
            try:
                bemail = request.POST['email']
                pas = request.POST['password']
                user = buyer.objects.filter(email=bemail, password=pas)
                uid = buyer.objects.get(email = bemail)
                if user:
                    print("Login Successfully!")
                    request.session['user']=bemail #session creation
                    request.session['uid']=uid.id
                    return redirect('indexbuyer')
                else:
                    print("Error! email or Password does not match.") 
                    messages.error(request,"Error! email or Password does not match.")
            except buyer.DoesNotExist:
                messages.error(request,"email and password in not exists!")
                return redirect('signin')

        if cname == 'seller':
            try:
                bemail = request.POST['email']
                pas = request.POST['password']
                user = seller.objects.filter(email=bemail, password=pas)
                uid = seller.objects.get(email = bemail)
                if user:
                    print("Login Successfully!")
                    request.session['user']=bemail #session creation
                    request.session['uid']=uid.id
                    return redirect('index')
                else:
                    print("Error! email or Password does not match.") 
                    messages.error(request,"Error! email or Password does not match.")
            except seller.DoesNotExist:
                messages.error(request,"email and password in not exists!")
                return redirect('signin')
            
        
    return render(request, 'signin.html')

def resetpassword(request):
    if request.method == 'POST':
        cname = request.POST.get('cname')
        if cname == 'buyer':
            try:
                bemail = request.POST['email']
                
                user = buyer.objects.filter(email=bemail)
                
                if user:
                    print("Login Successfully!")
                    request.session['cname'] = cname
                    request.session['resetemail']=bemail
                    return redirect('newpassword')
                else:
                    print("Error! Username or Password does not match.") 
                    messages.error(request,"Error! email does not exists.")
            except buyer.DoesNotExist:
                messages.error(request,"email and password in not exists!")
                return redirect('resetpassword')
            
        if cname == 'seller':
            try:
                bemail = request.POST['email']
                
                user = seller.objects.filter(email=bemail)
                if user:
                    print("Login Successfully!")
                    request.session['cname'] = cname
                    request.session['resetemail']=bemail
                    return redirect('newpassword')
                else:
                    print("Error! email or Password does not match.") 
                    messages.error(request,"Error! email or Password does not match.")
            except seller.DoesNotExist:
                messages.error(request,"email and password in not exists!")
                return redirect('resetpassword')
            
    return render(request, 'resetpassword.html')


def userlogout(request):
    logout(request)
    return redirect('index')


def addcattledata(request):
    user = request.session.get('user')
    id = request.session.get('uid')
    if request.method == 'POST':
        addcattle = cattleform(request.POST, request.FILES)
        if addcattle.is_valid():
            addcattle.save()
            print("Cattle Detaile added successfully")
            return redirect('cattledatashow')
        else:
            print(addcattle.errors)
    
    return render(request, 'addcattledata.html',{'user':user, 'id':seller.objects.get(email=user)})



    

def cattledatashowbuyer(request):
    data = cattler.objects.all()
    search = request.GET.get('search')  
    
    if search:
        products = cattler.objects.filter(name__icontains=search)
        return render(request, 'cattledatashowbuyer.html',{'data':data, 'productsof':products})      
    else:
        print("No information to show")
        return render(request, 'cattledatashowbuyer.html',{'data':data})

def cattledatashow(request):
    data = cattler.objects.all()
    query = request.GET.get('query')  
    
    if query:
        products = cattler.objects.filter(name__icontains=query)
        return render(request, 'cattledatashow.html',{'data':data, 'productsof':products})      
    else:
        print("No information to show")
        return render(request, 'cattledatashow.html',{'data':data})

def cattledetail(request, stid):
    id=cattler.objects.get(id=stid)         
    
    return render(request,'cattledetail.html',{'stdata':cattler.objects.get(id=stid)})


def cattledetailbuyer(request, stid):
    id=cattler.objects.get(id=stid)         
    
    return render(request,'cattledetailbuyer.html',{'stdata':cattler.objects.get(id=stid)})

def newpassword(request):
    email = request.session.get('resetemail')
    cname = request.session.get('cname')
    if request.method == 'POST':
        if cname == 'buyer':
            uid = buyer.objects.get(email=email)
            resetpas = buyerresetform(request.POST)
            if resetpas.is_valid():
                resetpas = buyerresetform(request.POST, instance=uid)
                resetpas.save()
                return redirect('signin')
            else:
                print(resetpas.errors)
            
        elif cname == 'seller':
            uid = seller.objects.get(email=email)
            resetpas = sellerresetform(request.POST)
            if resetpas.is_valid():
                resetpas = sellerresetform(request.POST, instance=uid)
                resetpas.save()
                return redirect('signin')
            else:
                print(resetpas.errors)
      
    return render(request, 'newpassword.html')



def registrationcheck(request):
    if request.method=="POST":
        typec = request.POST.get('typec', '') 
        name = request.POST.get('name', '')
        mobile = request.POST.get('mobile', '')
        email = request.POST.get('email', '')
        amount = request.POST.get('amount', '')
        address = request.POST.get('address', '')
        order = registration(typec=typec, name=name, mobile=mobile, email=email, amount=amount, address=address)
        order.save()
        
        param_dict = {

            'MID': 'OvhfNE13656302390739',
            'ORDER_ID': str(order.registration_id),
            'TXN_AMOUNT': str(amount),
            'CUST_ID': email,
            'INDUSTRY_TYPE_ID': 'Retail',
            'WEBSITE': 'WEBSTAGING',
            'CHANNEL_ID': 'WEB',
            'CALLBACK_URL':'http://127.0.0.1:8000/handlerequest/',

        }
        param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict, settings.MERCHANT_KEY)
        return render(request, 'paytm.html', {'param_dict': param_dict})
    return render(request, 'registration.html')


@csrf_exempt
def handlerequest(request):
    # paytm will send you post request here
    form = request.POST
    response_dict = {}
    for i in form.keys():
        response_dict[i] = form[i]
        if i == 'CHECKSUMHASH':
            checksum = form[i]

    verify = Checksum.verify_checksum(response_dict, settings.MERCHANT_KEY, checksum)
    if verify:
        if response_dict['RESPCODE'] == '01':
            print('order successful')
        else:
            print('order was not successful because' + response_dict['RESPMSG'])
    return render(request, 'paymentstatus.html', {'response': response_dict})