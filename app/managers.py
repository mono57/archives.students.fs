from django.db import models


class StudentManager(models.Manager):
    def get_recents(self, paginate_by=6):
        return super().get_queryset().order_by('created_at')[:paginate_by]
