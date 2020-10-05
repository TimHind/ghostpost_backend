from corsheaders.signals import check_request_enabled

from api.models import Joke

def cors_allow_mysites(sender, request, **kwargs):
    return Joke.objects.filter(host=request.host).exists()

check_request_enabled.connect(cors_allow_mysites)