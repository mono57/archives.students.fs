from django.contrib import admin
from app.models import *


class DepartmentModelAdmin(admin.ModelAdmin):
    list_display = ('name', )

admin.site.register(Department, DepartmentModelAdmin)

class CoureOfStudyModelAdmin(admin.ModelAdmin):
    list_display = ('name', )
    exclude = ('student', )

admin.site.register(CourseOfStudy, CoureOfStudyModelAdmin)

class SpecialityModelAdmin(admin.ModelAdmin):
    list_display = ('name', )

admin.site.register(Speciality, SpecialityModelAdmin)

class StudentModelAdmin(admin.ModelAdmin):
    list_display= ('serial_number', 'first_name', 'last_name')

admin.site.register(Student, StudentModelAdmin)

class LevelModelAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'short_name')

admin.site.register(Level, LevelModelAdmin)

class DocumentTypeModelAdmin(admin.ModelAdmin):
    list_display = ('name', )


admin.site.register(DocumentType, DocumentTypeModelAdmin)


class AdmissionFileModelAdmin(admin.ModelAdmin):
    list_display = ('student__first_name',
                    'student__last_name', 'student__serial_number')


# admin.site.register(AdmissionFile, AdmissionFileModelAdmin)

class DocumentModelAdmin(admin.ModelAdmin):
    list_display = ('type', 'file_name', )

admin.site.register(Document, DocumentModelAdmin)
admin.site.register(Semester)
