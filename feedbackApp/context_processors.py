from feedbackApp.forms import FeedBackMessagesForm


def feedback(request):
	"""Display the form on all pages."""

	form_feedback = FeedBackMessagesForm
	return {'form_feedback': form_feedback}