"""
h1)-The Spam Detector (Search in Stream) -linear search

A cybersecurity intern at a startup is building a basic spam filter. Incoming emails are checked against 
a blacklist of known spam sender IDs. The blacklist has no order.

"""

b_id=['s101','s102','s103','s104','s105','s119','s116']

def spamFilter(id):
    f=0
    for i in range(len(b_id)):
        if b_id[i]==id:
            f=1
            break
    return f
id=input("Enter  sender IDs:")
if spamFilter(id):
    print("Spam  Sender") 
else:
    print("Safe sender")


