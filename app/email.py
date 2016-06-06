from flask.ext.mail import Message
from flask import current_app
from flask import render_template
from threading import Thread
from . import mail


def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)


def send_email(to, subject, template, **kwargs):
    app = current_app._get_current_object()
    msg = Message(subject=app.config['FLASK_MAIL_SUBJECT_PREFIX'] + ' ' + subject,
                  recipients=[to],
                  sender='xuanxuancmon@yeah.net')
    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    thr = Thread(target=send_async_email, args=[app, msg])
    thr.start()
    return thr
