import io

import requests
from django.shortcuts import render

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Paragraph
from django.http import FileResponse, HttpResponseRedirect

# Create your views here.
from core.forms import SamGovtForm
from core.models import SamGovtData


def search_data(request):
    form = SamGovtForm
    response = requests.get(
        'https://api.sam.gov/prod/opportunities/v2/search?limit=1&api_key=stSXTDCgQR9K7ls8IBYXCHj3KAxOIGOfv7BS8UFD'
        '&postedFrom=01/05/2023&postedTo=01/05/2023&ptype=k&deptname=general')
    result = response.json()
    for data in result['opportunitiesData']:
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
    context = {'result': result['opportunitiesData'], 'form': form}
    return render(request, 'search.html', context)


# def some_view(request):
#     buffer = io.BytesIO()
#     x = canvas.Canvas(buffer)
#     x.drawString(100, 100, "Let's generate this pdf file.")
#     x.showPage()
#     x.save()
#     buffer.seek(0)
#     return FileResponse(buffer, as_attachment=True, filename='attempt1.pdf')


def sam_govt_search_form(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SamGovtForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            ptype = form.cleaned_data['ptype']
            naicsCode = form.cleaned_data['naicsCode']
            postedDate = form.cleaned_data['postedDate']
            postedDate = (postedDate.strftime('%m/%d/%Y'))
            print(postedDate)
            postedto = form.cleaned_data['postedto']
            postedto = (postedto.strftime('%m/%d/%Y'))
            print(postedto)

            response = requests.get(
                'https://api.sam.gov/prod/opportunities/v2/search?limit=1&api_key=stSXTDCgQR9K7ls8IBYXCHj3KAxOIGOfv7BS8UFD'
                f'&postedFrom={postedDate}&postedTo={postedto}&ptype={ptype}')
            result = response.json()
            for data in result['opportunitiesData']:
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
            context = {'form': form}
            return render(request, 'search_from.html', context)

            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:

        # if a GET (or any other method) we'll create a blank form
    else:
        form = SamGovtForm()

    return render(request, 'search_from.html', {'form': form})
