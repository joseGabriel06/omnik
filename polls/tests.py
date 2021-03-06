import datetime
from django.utils import timezone
from django.test import TestCase

from .models import Poll

class PollModelTest(TestCase):
    def test_was_published_recently_with_future_poll(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_poll = Poll(pub_date=time)
        self.assertIs(future_poll.was_published_recently(), False)
