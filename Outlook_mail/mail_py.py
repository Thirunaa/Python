# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 16:23:21 2020

@author: welcome
"""

import win32com.client

outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")

inbox = outlook.GetDefaultFolder(6) # "6" refers to the index of a folder - in this case,
                                    # the inbox. You can change that number to reference
                                    # any other folder
messages = inbox.Items
message = messages.GetLast()
#subject = message.Subject
body_content = message.To
print (body_content)