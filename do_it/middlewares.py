import logging

from django.db.models import Sum
from django.db.models.functions import Coalesce
from django.shortcuts import get_object_or_404

from account.models import DoerWallet
from core.models import Doer, Staff

logger = logging.getLogger(__name__)

class DoerWalletMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            if (request.user.is_doer):
                earning = DoerWallet.objects.filter(doer_id=get_doer(request)) \
                    .values('doer__user_id') \
                    .annotate(sum=Coalesce(Sum('point'), 0))

                sumPoint = 0
                if len(earning) > 0:
                    sumPoint = earning[0]['sum']

                request.session['sum_wallet'] = str(sumPoint)
        response = self.get_response(request)
        return response


class CurrentUserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            if request.user.is_superuser:
                pass
            elif request.user.is_doer:
                request.session['current_user'] = get_doer(request).name
            elif request.user.is_staff:
                request.session['current_user'] = get_staff(request).name
            else:
                pass

        response = self.get_response(request)
        return response


def get_doer(request):
    return get_object_or_404(Doer, user=request.user)


def get_staff(request):
    return get_object_or_404(Staff, user=request.user)
