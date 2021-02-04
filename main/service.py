import socket
from django.core.exceptions import ObjectDoesNotExist


def get_ip():
    return socket.gethostbyname(socket.gethostname())


def filter_group(request):
    from main.models import Profile
    if Profile.objects.get(user=request.user).group == 'base':
        return Profile.objects.all()[:11]
    elif Profile.objects.get(user=request.user).group == 'premium':
        return Profile.objects.all()[:101]
    elif Profile.objects.get(user=request.user).group == 'vip':
        return Profile.objects.all()
    else:
        print('no')

