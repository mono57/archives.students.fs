from app.models import Department

def departments(request):
    kwargs = {
        'departments': Department.objects.all()
    }
    return kwargs