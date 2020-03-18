import imaplib
import sys
import gmail

IMAP_HOST = 'imap.gmail.com'
IMAP_PORT = 993

EMAIL_ADDRESS = gmail.EMAIL_ADDRESS
EMAIL_PASS = gmail.EMAIL_PASS


def check_email(subject):
    try:
        server = imaplib.IMAP4_SSL(IMAP_HOST, IMAP_PORT)
        server.login(EMAIL_ADDRESS, EMAIL_PASS)
        server.select('"[Gmail]/Sent Mail"')
        search_string = 'SUBJECT "' + subject + '"'
        result, data = server.uid('search', None, search_string)
        uids = [int(s) for s in data[0].split()]
        return uids
    except:
        print("Unexpected error:", sys.exc_info()[0])
        return -1
