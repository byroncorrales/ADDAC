# signals.py
from django.contrib.sites.models import Site
from django.template.loader import render_to_string
from django.core.mail import send_mail
def comment_notifier(sender, comment, **kwargs):
    print 'sera que entra'
    """ Email admins when a new comment is posted """
    subject = "New comment by %s on %s" % (
        comment.user_name,
        Site.objects.get_current().domain)
    body = render_to_string(
        "email.txt", {
            'comment': comment})
    send_mail(subject, body, 'no-reply@addac.org.ni', ['byroncorrales@gmail.com'])