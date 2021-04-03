from .models import License
from .serializer import LicenseSerializer
from django.shortcuts import get_object_or_404


class LicenseUtil:

    def __init__(self,userId=None, licenseId=None):
        if userId is not None:
            self.userId=userId
        elif licenseId is not None:
            self.licenseId=licenseId

    def getLicenseJo(self):
        license= get_object_or_404(License,userId=self.userId)
        serializer= LicenseSerializer(license)
        return serializer.data

    def updateUsedSize(self,newFileSize,isAdd):
        license=get_object_or_404(License,userId=self.userId)
        if isAdd and license.usedSpace+newFileSize <= license.totalSpace:
            license.usedSpace= license.usedSpace+newFileSize
        if not isAdd and license.usedSpace-newFileSize > 0:
            license.usedSpace=license.usedSpace-newFileSize
        license=license.save()
        return license
    def updateLicense(self,**kargs):
        license=License.objects.filter(userId=self.userId).update(**kargs)
    def checkSizeExist(self, newFileSize):
        license = get_object_or_404(License, userId=self.userId)
        if license.usedSpace + newFileSize <= license.totalSpace:
            return True
        else:
            return False



