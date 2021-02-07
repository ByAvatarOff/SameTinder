from django.contrib.gis.geoip2 import GeoIP2
import http.client

from django.contrib.gis.geos import Point
from geoip2.errors import AddressNotFoundError


def get_ip():
    conn = http.client.HTTPConnection("ifconfig.me")
    conn.request("GET", "/ip")
    t = conn.getresponse().read()
    return t.decode('utf-8')


def get_location():
    geo = GeoIP2()
    try:
        lng, lat = geo.lat_lon(get_ip())
        point = Point(lng, lat)
        return point
    except AddressNotFoundError:
        return None


def filter_group(request):
    from main.models import Profile
    if Profile.objects.get(user=request.user).group.lower() == 'base':
        return Profile.objects.all()[:11]
    elif Profile.objects.get(user=request.user).group.lower() == 'premium':
        return Profile.objects.all()[:101]
    elif Profile.objects.get(user=request.user).group.lower() == 'vip':
        return Profile.objects.all()
    else:
        print('no')


