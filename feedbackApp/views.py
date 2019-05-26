import requests

from django.views.generic import View
from django.http import JsonResponse
from django.conf import settings

from feedbackApp.forms import FeedBackMessagesForm


class FeedBackView(View):
    """View for data get and processing feedback form."""

    def post(self, *args, **kwargs):
        data = {}

        # recaptcha_response = self.request.POST.get('g-recaptcha-response')
        # r_data = {
        #     'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
        #     'response': recaptcha_response
        # }

        # r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=r_data)


        # result = r.json()
        # if result['success']:
        #     form_feedback = FeedBackMessagesForm(self.request.POST)
        #     if form_feedback.is_valid():
        #         form_feedback.save()
        #         data['status'] = 'OK'
        #     else:
        #         data['status'] = 'Error: Invalid form'
        # else:
        #     data['status'] = 'Invalid reCAPTCHA. Please try again.'

        form_feedback = FeedBackMessagesForm(self.request.POST)
        if form_feedback.is_valid():
            form_feedback.save()
            data['status'] = 'OK'
        else:
            data['status'] = 'Error: Invalid form'

        return JsonResponse({'data': data})