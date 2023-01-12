from django.db import models


#
# # Create your models here.
# from django.db import models
#
#
class SamGovtData(models.Model):
    noticeId = models.CharField(max_length=255, null=True)
    title = models.CharField(max_length=255, null=True)
    solicitationNumber = models.CharField(max_length=255, null=True)
    fullParentPathName = models.CharField(max_length=500, null=True)
    fullParentPathCode = models.CharField(max_length=1000, null=True)
    postedDate = models.DateField()
    archiveDate = models.DateField()
    typeOfSetAsideDescription = models.CharField(max_length=500, null=True)
    typeOfSetAside = models.CharField(max_length=80, null=True)
    responseDeadLine = models.DateField()
    naicsCode = models.CharField(max_length=255, null=True)
    classificationCode = models.CharField(max_length=255, null=True)
    active = models.CharField(max_length=80, null=True)
    award = models.CharField(max_length=80, null=True)

    # point of contact data
    fax = models.CharField(max_length=255, null=True)
    type = models.CharField(max_length=80, null=True)
    email = models.CharField(max_length=255, null=True)
    phone = models.CharField(max_length=255, null=True)
    fullName = models.CharField(max_length=500, null=True)
    description = models.CharField(max_length=500, null=True)
    organizationType = models.CharField(max_length=500, null=True)

    # office address
    zipcode = models.CharField(max_length=255,null=True)
    city = models.CharField(max_length=200,null=True)
    countryCode = models.CharField(max_length=20,null=True)
    state = models.CharField(max_length=300,null=True)
    placeOfPerformance = models.CharField(max_length=300, null=True)
    additionalInfoLink = models.URLField(null=True)
    uiLink = models.URLField(null=True)
    links = models.URLField(null=True)

    def __str__(self):
        return self.noticeId
