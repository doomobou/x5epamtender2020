import allure
import gmail
import uuid
import steps
import os
import pytest


EMAIL_TO = os.getenv('EMAIL_TO', gmail.EMAIL_ADDRESS)


@allure.feature("Sending email from Gmail")
@pytest.mark.parametrize("email, subject, message, image",
                         [(EMAIL_TO, 'subject ' + str(uuid.uuid4()), 'Test email', None),
                          (EMAIL_TO, 'subject ' + str(uuid.uuid4()), 'Test email2', 'image.png')])
def test_send_email(email, subject, message, image):
    steps.send_email(gmail.EMAIL_ADDRESS, subject, 'message', None)
    found_emails = steps.find_sent_email_by_subject(subject)
    steps.check_found_one_email_by_subject(found_emails)


@allure.feature("Sending email from Gmail")
def test_send_single_email_with_attach_over_limit():
    subject = 'subject ' + str(uuid.uuid4())
    steps.send_email(EMAIL_TO, subject, 'message', 'big_image.jpg')
    found_emails = steps.find_sent_email_by_subject(subject)
    steps.check_no_email_sent_by_subject(found_emails)


@allure.feature("Sending email from Gmail")
def test_send_email_to_incorrect_address():
    subject = 'subject ' + str(uuid.uuid4())
    steps.send_email('incorrect_email', subject, 'message', None)
    found_emails = steps.find_sent_email_by_subject(subject)
    steps.check_no_email_sent_by_subject(found_emails)
