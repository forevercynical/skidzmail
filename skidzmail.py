from httpx import Client as httpx
from ujson import loads

class Client:
    def __init__(self):
        self.session = httpx()
    
    def generateEmail(self):
        """
        Generates a random email address.

        **Returns**
        - `random_email`: A random email address.

        """
        url='https://skidz.me/api/email/email/1'
        r = self.session.get(url=url)
        return r.text

    def retrieveAttachment(self, email):
        """
        Retrieves the attachment from the email.
        
        **Parameters**
        - `email`: The email address to retrieve the attachment from.
        
        **Returns**
        
        - `attachment`: The attachment.
        
        """
        url=f'https://skidz.me/api/messages/{email}/1'
        r = self.session.get(url=url)
        for r in loads(r.text) if isinstance(loads(r.text), list) else []:
            return r['attachments'][0]['url']

    def checkEmail(self, email):
        """
        Checks if the email has any messages.
        
        **Parameters**
        - `email`: The email address to check.

        **Returns**
        - `response`: List of messages.
        """
        url=f'https://skidz.me/api/messages/{email}/1'
        r = self.session.get(url=url)
        return loads(r.text) if isinstance(loads(r.text), list) else []
