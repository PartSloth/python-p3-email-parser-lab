import re

class EmailAddressParser:
    def __init__(self, string):
        self.string = string

    def parse(self):
        regex_emails = re.compile(r"[A-z0-9.]+@[A-z.]{1,}")
        filter_string = regex_emails.findall(self.string)
        filter_string.sort()        
        return filter_string