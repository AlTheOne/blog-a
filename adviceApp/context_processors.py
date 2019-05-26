import random

from adviceApp.models import Advice


def random_advices(request):
    """
    Function get object request and return dict with 3 random advices.
    """

    if Advice.objects.count() > 3:
        random_advice = random.sample(list(Advice.objects.all()), k=3)
    else:
        random_advice = Advice.objects.all()
    return {'random_advice': random_advice}