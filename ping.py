from pypinger import pyping

hostname = "www.google.com"
r = pyping(hostname)
if r == 0:
    print("Success")
else:
    print("Failed with {}".format(r))