from django.shortcuts import render,redirect
from labs.models import Labs
from labs.models import Labs_payment
from dept import views as deptviews
from dept.models import Departments
from django.core.mail import send_mail
from login import models as loginmodels
from appointment import models as aptmodels
from django.contrib import messages
from vaccines.models import Vaccines_payment
# Create your views here.

def tests(request):
    obj1 = Labs.objects.get(testID=1)
    obj2 = Labs.objects.get(testID=2)
    obj3 = Labs.objects.get(testID=3)
    obj4 = Labs.objects.get(testID=4)
    obj5 = Labs.objects.get(testID=5)
    obj6 = Labs.objects.get(testID=6)
    obj7 = Labs.objects.get(testID=7)
    obj8 = Labs.objects.get(testID=8)
    obj9 = Labs.objects.get(testID=9)
    obj10 = Labs.objects.get(testID=10)
    obj11 = Labs.objects.get(testID=11)
    obj12 = Labs.objects.get(testID=12)
    obj13 = Labs.objects.get(testID=13)
    obj14 = Labs.objects.get(testID=14)
    obj15 = Labs.objects.get(testID=15)
    obj16 = Labs.objects.get(testID=16)
    obj17 = Labs.objects.get(testID=17)
    obj18 = Labs.objects.get(testID=18)
    obj19 = Labs.objects.get(testID=19)
    obj20 = Labs.objects.get(testID=20)
    obj21 = Labs.objects.get(testID=21)
    obj22 = Labs.objects.get(testID=22)
    obj23 = Labs.objects.get(testID=23)
    obj24 = Labs.objects.get(testID=24)
    obj25 = Labs.objects.get(testID=25)
    context = {
        'object1': obj1,
        'object2': obj2,
        'object3': obj3,
        'object4': obj4,
        'object5': obj5,
        'object6': obj6,
        'object7': obj7,
        'object8': obj8,
        'object9': obj9,
        'object10': obj10,
        'object11': obj11,
        'object12': obj12,
        'object13': obj13,
        'object14': obj14,
        'object15': obj15,
        'object16': obj16,
        'object17': obj17,
        'object18': obj18,
        'object19': obj19,
        'object20': obj20,
        'object21': obj21,
        'object22': obj22,
        'object23': obj23,
        'object24': obj24,
        'object25': obj25
    }
    return render(request, 'labs/labs1.html', context)

def booking(request):
    if request.method=='GET':
        if request.GET.get("Thyroid"):
            test = Labs.objects.filter(testID=1)
            return render(request, 'labs/payment.html', {'t_lst': test})
        elif request.GET.get("VIT D & B12"):
            test = Labs.objects.filter(testID=2)
            return render(request, 'labs/payment.html', {'t_lst': test})
        elif request.GET.get("VITAL CARE VITAMIN AND MINERAL CARE"):
            test = Labs.objects.filter(testID=3)
            return render(request, 'labs/payment.html', {'t_lst': test})
        elif request.GET.get("VITAL BONE CARE"):
            test = Labs.objects.filter(testID=4)
            return render(request, 'labs/payment.html', {'t_lst': test})
        elif request.GET.get("LIVER FUNCTION CARE"):
            test = Labs.objects.filter(testID=5)
            return render(request, 'labs/payment.html', {'t_lst': test})
        elif request.GET.get("LIVER AND KIDNEY PROFILE"):
            test = Labs.objects.filter(testID=6)
            return render(request, 'labs/payment.html', {'t_lst': test})
        elif request.GET.get("OSTEOSCREEN PANEL"):
            test = Labs.objects.filter(testID=7)
            return render(request, 'labs/payment.html', {'t_lst': test})
        elif request.GET.get("Thyro SCREEN PANEL"):
            test = Labs.objects.filter(testID=8)
            return render(request, 'labs/payment.html', {'t_lst': test})
        elif request.GET.get("VITAL CARE DIABETES"):
            test = Labs.objects.filter(testID=9)
            return render(request, 'labs/payment.html', {'t_lst': test})
        elif request.GET.get("VITAL CARE HEART"):
            test = Labs.objects.filter(testID=10)
            return render(request, 'labs/payment.html', {'t_lst': test})
        elif request.GET.get("LIPID SCREEN"):
            test = Labs.objects.filter(testID=11)
            return render(request, 'labs/payment.html', {'t_lst': test})
        elif request.GET.get("HYPERTENSION PROFILE"):
            test = Labs.objects.filter(testID=12)
            return render(request, 'labs/payment.html', {'t_lst': test})
        elif request.GET.get("GLUCOSE FASTING"):
            test = Labs.objects.filter(testID=13)
            return render(request, 'labs/payment.html', {'t_lst': test})
        elif request.GET.get("COMPLETE BLOOD COUNT"):
            test = Labs.objects.filter(testID=14)
            return render(request, 'labs/payment.html', {'t_lst': test})
        elif request.GET.get("COMPLETE URINE EXAM"):
            test = Labs.objects.filter(testID=15)
            return render(request, 'labs/payment.html', {'t_lst': test})
        elif request.GET.get("BILIRUBIN TOTAL"):
            test = Labs.objects.filter(testID=16)
            return render(request, 'labs/payment.html', {'t_lst': test})
        elif request.GET.get("HOMOCYSTEIN SERUM"):
            test = Labs.objects.filter(testID=17)
            return render(request, 'labs/payment.html', {'t_lst': test})
        elif request.GET.get("FREE T3 & T4"):
            test = Labs.objects.filter(testID=18)
            return render(request, 'labs/payment.html', {'t_lst': test})
        elif request.GET.get("ULTRASONOGRAPHY"):
            test = Labs.objects.filter(testID=19)
            return render(request, 'labs/payment.html', {'t_lst': test})
        elif request.GET.get("HEMOGLOBIN A1C"):
            test = Labs.objects.filter(testID=20)
            return render(request, 'labs/payment.html', {'t_lst': test})
        elif request.GET.get("VITAL CARE ANEMIA "):
            test = Labs.objects.filter(testID=21)
            return render(request, 'labs/payment.html', {'t_lst': test})
        elif request.GET.get("CALCIUM SERUM"):
            test = Labs.objects.filter(testID=22)
            return render(request, 'labs/payment.html', {'t_lst': test})
        elif request.GET.get("ALLERGY SCREENING"):
            test = Labs.objects.filter(testID=23)
            return render(request, 'labs/payment.html', {'t_lst': test})
        elif request.GET.get("MASTER CHECK DIAMOND "):
            test = Labs.objects.filter(testID=24)
            return render(request, 'labs/payment.html', {'t_lst': test})
        elif request.GET.get("MASTER CHECK GOLD"):
            test = Labs.objects.filter(testID=25)
            return render(request, 'labs/payment.html', {'t_lst': test})


def payment(request):
    if request.method == "POST":
        try:
            fname = request.POST['firstname']
            email = request.POST['email']
            add = request.POST['address']
            city = request.POST['city']
            testname = request.POST.get('testname')
            price = request.POST['price']
            state = request.POST['state']
            pincode = request.POST['Pincode']
            cardname = request.POST['cardname']
            creditcard_num = request.POST['cardnumber']
            expiry_month = request.POST['expmonth']
            expiry_year = request.POST['expyear']
            cvv = request.POST['cvv']
            R = Labs_payment()
            R.patientID = request.user
            R.fname=fname
            R.Add=add
            R.city=city
            R.testname=testname
            R.price=price
            R.state=state
            R.pincode=pincode
            R.cardname=cardname
            R.cardnumber=creditcard_num
            R.exp_month=expiry_month
            R.exp_year=expiry_year
            R.cvv= cvv
            R.save()
            body = 'Dear {0},\nYour {1} test has been succsessfully booked\n Regards,\nTeam Aselpius'.format(fname, testname)
            send_mail('Diagnostic test paid', body,
                  'aslepius9@gmail.com', [request.user.email, ], fail_silently=False)
            details_lst = loginmodels.Register.objects.filter(email=request.user.id)
            appointment_lst = aptmodels.Appointment.objects.filter(status=0, patientID=request.user.id, )
            labs_lst = Labs_payment.objects.filter(patientID=request.user.id, )
            vaccines_lst = Vaccines_payment.objects.filter(patientID=request.user.id, )
            return render(request, 'mypage/myhomepage.html',{'d_lst': details_lst, 'a_lst': appointment_lst, 'l_lst': labs_lst, 'v_lst': vaccines_lst})
        except:
            messages.info(request,'Payment unsuccessful. Please try again later')
            return redirect('tests')
    else:
        return render(request, 'labs/payment.html')
            


def labs_confirm(request):
    if request.method == "POST":
        bookingID = request.POST.get('bookingID')
        print('1',bookingID)
        obj_delete = Labs_payment.objects.filter(bookingID= bookingID)
        l_dict = {'bookingID': obj_delete}
        print(l_dict)
    return render(request, 'labs/confirmcancel.html', l_dict)

'''This function enables the patient to cancel the test'''
def labs_cancel(request):
    if request.method == "POST":
        bookingID = request.POST.get('bookingID')
        obj_delete = Labs_payment.objects.get(bookingID= bookingID)
        obj_delete.delete()
        print("SUCCESS")
        return render(request, 'labs/cancellab.html')
    else:
        return render(request, 'labs/labs1.html')





