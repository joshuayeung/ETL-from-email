from datetime import datetime, timedelta
import pytz
from exchangelib import DELEGATE, IMPERSONATION, Account, Credentials, ServiceAccount, \
    EWSDateTime, EWSTimeZone, Configuration, NTLM, GSSAPI, CalendarItem, Message, \
    Mailbox, Attendee, Q, ExtendedProperty, FileAttachment, ItemAttachment, \
    HTMLBody, Build, Version, FolderCollection

# You can also get the local timezone defined in your operating system
tz = EWSTimeZone.localzone()

# Specify your credentials. Username is usually in WINDOMAIN\username format, where WINDOMAIN is
# the name of the Windows Domain your username is connected to
credentials = Credentials(username='', password='')

ews_url = ''
ews_auth_type = 'NTLM'
primary_smtp_address = ''

config = Configuration(service_endpoint=ews_url, credentials=credentials, auth_type=ews_auth_type)

# An Account is the account on the Exchange server that you want to connect to.
account = Account(
    primary_smtp_address=primary_smtp_address,
    config=config, autodiscover=False,
    access_type=DELEGATE,
)

def send(account=account, subject=subject, body=body, recipients=recipients, attachments=[]):
    """
    Send an email.

    Parameters
    ----------
    account : Account object
    subject : str
    body : str
    recipients : list of str
        Each str is an email adress
    attachments : list of str
        Each str is a path of file

    Examples
    --------
    >>> send_email(account, 'Subject line', 'Hello!', ['info@example.com'])
    """
    to_recipients = []
    for recipient in recipients:
        to_recipients.append(Mailbox(email_address=recipient))
    # Create message
    m = Message(account=account,
                subject=subject,
                body=body,
                to_recipients=to_recipients)

    # Read attachment
    # attachments : list of tuples or None
    # (filename, binary contents)
    files = []
    for file in attachments:
        with open(file, 'rb') as f:
            content = f.read()
        files.append((file, content))

    # attach files
    for attachment_name, attachment_content in files or []:
        file = FileAttachment(name=attachment_name, content=attachment_content)
        m.attach(file)
    m.send()

subject = 'Testing'
body = 'Works!'
recipients = ['someone@example.com']

if __name__ == "__main__":
    # Send email
    send(account, subject, body, recipients)
