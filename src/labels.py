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

"""Get a list of Labels from the user's mailbox.
"""

from apiclient import errors

def ListLabels(service, user_id):
  """Get a list all labels in the user's mailbox.

  Args:
    service: Authorized Gmail API service instance.
    user_id: User's email address. The special value "me"
    can be used to indicate the authenticated user.

  Returns:
    A list all Labels in the user's mailbox.
  """
  try:
    response = service.users().labels().list(userId=user_id).execute()
    labels = response['labels']
    for label in labels:
      print 'Label id: %s - Label name: %s' % (label['id'], label['name'])
    return labels
  except errors.HttpError, error:
    print 'An error occurred: %s' % error

labels = ListLabels(gmail_service,'me')
print(labels)
