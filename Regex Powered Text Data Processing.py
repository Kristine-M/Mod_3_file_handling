# Write a Python script to extract all email addresses from a given 
# text file (contacts.txt). The file contains a mix of text and email addresses.

# File Example:
# Contact List:

# John Doe - john.doe@example.com
# Jane Smith - jane.smith@gmail.com

# For inquiries, please contact info@example.com
# Code Example:
import re

# def extract_emails(filename):
#     # Read the file and use regex to find and return all email addresses
# Expected Outcome:
# The script should output a list of all unique email addresses 
# found in the file. Utilize regex to accurately identify email 
# addresses amidst other text.

def extract_emails(filename):
    
    
    
    unique_email = set()
    
    with open(filename, 'r') as file:
        
        for email in file:
            
            line_email = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", email)
            
            
            unique_email.update(line_email)
              
    for new_email in unique_email:
        print(new_email)

filename = input("Enter a file name: ")
email = extract_emails(filename)


        
