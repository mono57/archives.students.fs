from django.db.models.signals import post_save
import uuid

from app.models import Student

def post_save_student_gen_uid(sender, instance, created, **kwargs):
    if created and not instance.uid:
        instance.uid = uuid.uuid4()
        instance.save()


post_save.connect(post_save_student_gen_uid, sender=Student)