# coding=utf-8
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

from .models import SiteMailReceive


@login_required
@require_http_methods(["PATCH"])
def sitemail_markall(request):
    SiteMailReceive.objects.exclude(
        status=SiteMailReceive.DELETED
    ).filter(receiver=request.user).update(status=SiteMailReceive.READ)
    return JsonResponse({'message': u'ok'}, status=200)
