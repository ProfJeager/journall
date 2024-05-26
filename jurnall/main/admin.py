from django.contrib import admin
from .models import Articles, UploadFile, Certificate


admin.site.register(Articles)
admin.site.register(Certificate)
admin.site.register(UploadFile)
