from django.db.models import Sum
from django.db.models.functions import Coalesce
from django.shortcuts import get_object_or_404

from account.models import DoerWallet
from core.models import Doer


class DoerWalletMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        # count message and notification
        if request.user.is_authenticated:
            if (request.user.is_doer):
                earning = DoerWallet.objects.filter(doer=get_doer(request)) \
                    .annotate(sum=Coalesce(Sum('amount'), 0)).first()
                if earning is None:
                    request.session['sum_wallet'] = 0
                else:
                    request.session['sum_wallet'] = str(earning.sum)
        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response


class CurrentDoerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        # count message and notification
        if request.user.is_authenticated:
            if (request.user.is_doer):
                request.session['current_doer'] = get_doer(request).name

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response


def get_doer(request):
    return get_object_or_404(Doer, user=request.user)
