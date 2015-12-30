# coding=utf-8
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

from .models import SiteMailReceive
import logging
logger = logging.getLogger(__name__)

@login_required
@require_http_methods(["PATCH"])
def sitemail_markall(request):
    """
    更新邮件状态 api 标记为全部已读
    :param request:
    :return:
    """
    try:
        logger.info(u'对用户:%s 进行邮件全部标记已读动作'%(request.user.id))
        SiteMailReceive.objects.exclude(
            status=SiteMailReceive.DELETED
        ).filter(receive_id=request.user.id).update(status=SiteMailReceive.READ)
    except Exception as e :
        logger.error(e.message)
        return JsonResponse({'message': u'%s'%(e.message)}, status=200)
    return JsonResponse({'message': u'ok'}, status=200)
