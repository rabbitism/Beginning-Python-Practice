import urllib.request

fp = urllib.request.urlopen("https://equality.slb.com/MatsTest/test_perform_edit.cfm?action=view&test_taken_id=5095783")
mybytes = fp.read()

mystr = mybytes.decode("utf8")
fp.close()

print(mystr)
