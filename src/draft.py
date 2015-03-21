#!/usr/bin/python

import httplib2
import socks

from apiclient.discovery import build
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client.tools import run


# Path to the client_secret.json file downloaded from the Developer Console
CLIENT_SECRET_FILE = '../credentials/client_secret_999151699233-pmqq91k82q11v83v90vuifopav9hti6j.apps.googleusercontent.com.json'

# Check https://developers.google.com/gmail/api/auth/scopes for all available scopes
OAUTH_SCOPE = 'https://www.googleapis.com/auth/gmail.modify'

# Location of the credentials storage file
STORAGE = Storage('gmail.storage')

# Start the OAuth flow to retrieve credentials
flow = flow_from_clientsecrets(CLIENT_SECRET_FILE, scope=OAUTH_SCOPE)
http = httplib2.Http(proxy_info = httplib2.ProxyInfo(socks.PROXY_TYPE_SOCKS5, '172.16.26.47', 9050, proxy_rdns = True))

# Try to retrieve credentials from storage or run the flow to generate them
credentials = STORAGE.get()
if credentials is None or credentials.invalid:
  credentials = run(flow, STORAGE, http=http)

# Authorize the httplib2.Http object with our credentials
http = credentials.authorize(http)

# Build the Gmail service from discovery
gmail_service = build('gmail', 'v1', http=http)

"""Create a draft email message in the user's account.
"""

import base64
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
import mimetypes
import os

from apiclient import errors

def CreateDraft(service, user_id, message_body):
  """Create and insert a draft email. Print the returned draft's message and id.

  Args:
    service: Authorized Gmail API service instance.
    user_id: User's email address. The special value "me"
    can be used to indicate the authenticated user.
    message_body: The body of the email message, including headers.

  Returns:
    Draft object, including draft id and message meta data.
  """
  try:
    message = {'message': message_body}
    draft = service.users().drafts().create(userId=user_id, body=message).execute()

    print 'Draft id: %s\nDraft message: %s' % (draft['id'], draft['message'])

    return draft
  except errors.HttpError, error:
    print 'An error occurred: %s' % error
    return None

def CreateMessage(sender, to, subject, message_text):
  """Create a message for an email.

  Args:
    sender: Email address of the sender.
    to: Email address of the receiver.
    subject: The subject of the email message.
    message_text: The text of the email message.

  Returns:
    An object containing a base64url encoded email object.
  """
  message = MIMEText(message_text)
  message['to'] = to
  message['from'] = sender
  message['subject'] = subject
  return {'raw': base64.urlsafe_b64encode(message.as_string())}
subject = 'This is a test mail'
message = 'Check this draft'
EmailMessage = CreateMessage('abhishhek@abc.com','mail@abhishek.ind.in',subject,message)

draftId = CreateDraft(gmail_service,'me',EmailMessage)

print(draftId)
