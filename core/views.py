import io

import requests
from django.shortcuts import render

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Paragraph
from django.http import FileResponse

# Create your views here.
from core.models import SamGovtData


def search_data(request):
    response = requests.get(
        'https://api.sam.gov/prod/opportunities/v2/search?limit=1&api_key=stSXTDCgQR9K7ls8IBYXCHj3KAxOIGOfv7BS8UFD'
        '&postedFrom=01/05/2023&postedTo=01/05/2023&ptype=k&deptname=general')
    result = response.json()
    for data in result['opportunitiesData']:
        print(data['noticeId'])
        SamGovtData.objects.get_or_create(
            noticeId=data['noticeId'],
            title=data['title'],
            solicitationNumber=data['solicitationNumber'],
            fullParentPathName=data['fullParentPathName'],
            fullParentPathCode=data['fullParentPathCode'],
            postedDate=data['postedDate'],
            archiveDate=data['archiveDate'],
            typeOfSetAsideDescription=data['typeOfSetAsideDescription'],
            typeOfSetAside=data['typeOfSetAside'],
            responseDeadLine=data['responseDeadLine'],
            naicsCode=data['naicsCode'],
            classificationCode=data['classificationCode'],
            active=data['active'],
            award=data['award'],
            fax=data['pointOfContact'][0]['fax'],
            type=data['pointOfContact'][0]['type'],
            email=data['pointOfContact'][0]['email'],
            phone=data['pointOfContact'][0]['phone'],
            fullName=data['pointOfContact'][0]['fullName'],
            description=data['description'],
            organizationType=data['organizationType'],
            # officeAddress=data['officeAddress'],
            zipcode=data['officeAddress']['zipcode'],
            city=data['officeAddress']['city'],
            countryCode=data['officeAddress']['countryCode'],
            state=data['officeAddress']['state'],
            placeOfPerformance=data['placeOfPerformance'],
            additionalInfoLink=data['additionalInfoLink'],
            uiLink=data['uiLink'],
            links=data['links'])
    context = {'result': result['opportunitiesData']}
    return render(request, 'search.html', context)

# def some_view(request):
#     buffer = io.BytesIO()
#     x = canvas.Canvas(buffer)
#     x.drawString(100, 100, "Let's generate this pdf file.")
#     x.showPage()
#     x.save()
#     buffer.seek(0)
#     return FileResponse(buffer, as_attachment=True, filename='attempt1.pdf')


# SamGovtData.objects.get_or_create(
#     'noticeId'
#     'title'
#     'solicitationNumber'
#     'fullParentPathName'
#     'fullParentPathCode'
#     'postedDate'
#     'archiveDate'
#     'typeOfSetAsideDescription'
#     'typeOfSetAside'
#     'responseDeadLine'
#     'naicsCode'
#     'classificationCode'
#     'active'
#     'award'
#     'fax'
#     'type'
#     'email'
#     'phone'
#     'fullName'
#     'description'
#     'organizationType'
#     'officeAddress'
#     'zipcode'
#     'city'
#     'countryCode'
#     'state'
#     'placeOfPerformance'
#     'additionalInfoLink'
#     'uiLink'
#     'resourceLinks')
