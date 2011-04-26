# signals.py
from django.contrib.sites.models import Site
from django.template.loader import render_to_string
from django.core.mail import mail_managers

def comment_notifier(sender, comment, **kwargs):

    """ Email admins when a new comment is posted """

    if not comment.is_public:
        subject = "New comment by %s on %s" % (
            comment.user_name,
            Site.objects.get_current().domain)
        body = render_to_string(
            "email.txt", {
                'comment': comment})
        mail_managers(subject, body, fail_silently=False, connection=None)