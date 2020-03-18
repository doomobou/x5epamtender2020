import gmail
import imap
import allure


@allure.step('Send email to {0} with subject "{1}", message body "{2}" and attachment {3}')
def send_email(address_to, subject, message, attachment):
    gmail.send_email(address_to, subject, message, attachment)


@allure.step('Find email with subject "{0}" in Sent Items')
def find_sent_email_by_subject(subject):
    return imap.check_email(subject)


@allure.step('Check that exactly 1 email was found')
def check_found_one_email_by_subject(found_emails):
    assert found_emails is not None and len(found_emails) == 1, \
        'Error: Email with that subject was not found in Sent Items'


@allure.step('Check that email was not sent')
def check_no_email_sent_by_subject(found_emails):
    assert found_emails is None or len(found_emails) == 0, \
        'Error: Email with that subject was found in Sent Items, expected to be absent'
