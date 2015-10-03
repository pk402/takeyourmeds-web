import pytz
import datetime

from takeyourmeds.utils.test import TestCase

class SmokeTest(TestCase):
    def test_index(self):
        self.assertHTTP200('reminders:index', login=True)

    def test_create(self):
        self.assertHTTP200('reminders:create', login=True)

    def test_delete(self):
        instance = self.user.reminders.create()

        self.assert_(self.user.reminders.exists())
        self.assertHTTP302('reminders:delete', instance.pk, login=True)
        self.failIf(self.user.reminders.exists())

class TestCron(TestCase):
    def test_cron(self):
        ten_min_ago = datetime.datetime.now(pytz.utc) - \
            datetime.timedelta(minutes=10)

        reminder = self.user.reminders.create(
            message="test",
            telnumber='123',
        )

        reminder.times.create(
            cronstring="* * * * *",
            last_run=ten_min_ago,
        )
