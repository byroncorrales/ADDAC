# signals.py
from django.contrib.sites.models import Site
from django.template.loader import render_to_string
from django.core.mail import send_mail
def comment_notifier(sender, **kwargs):
    """ Email admins when a new comment is posted """
    body = kwargs['instance'].name + ", comento" + ": " + kwargs['instance'].comment
    send_mail("Nuevo Comentario en Sitio ADDAC", body, 'no-reply@addac.org.ni', ['byroncorrales@gmail.com','central@addac.org.ni'])