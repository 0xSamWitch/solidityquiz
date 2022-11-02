from django.conf import settings

def constants(request):
    return {
        'SOLIDITY_VERSION': settings.SOLIDITY_VERSION,
        'TOP_WARNING': settings.TOP_WARNING,
    }
