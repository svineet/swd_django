





from django.contrib.auth.models import User
from main.models import Student
from django.shortcuts import render
from django.http import HttpResponse
import datetime


def index(request):

    for name, login, hostel, room, bitsId, bDay, phone, email, address, parentName, parentPhone, parentEmail, admit, gender, bloodGroup in profiles:
        rev_login = login[0:5] + '0' + login[5:]
        try:
            user = User.objects.get(username = rev_login)
            rev_bDay = datetime.datetime.strptime(bDay, '%d-%b-%y').strftime('%Y-%m-%d')
            rev_admit = datetime.datetime.strptime(admit, '%d/%m/%Y').strftime('%Y-%m-%d')
            profile = Student.objects.create(user=user, name=name, bitsId=bitsId, gender=gender, bDay=rev_bDay, phone=phone, email=email, address=address, bloodGroup=bloodGroup, admit=rev_admit, parentName=parentName, parentPhone=parentPhone, parentEmail=parentEmail)
            profile.save()
        except Exception as e:
            print(rev_login+ ' ' + str(e))
            continue

    return HttpResponse("Done")