import urllib.request

fp = urllib.request.urlopen("https://reports.cpl.ems.slb.com/mfg/cpl/threaddb/thread_Details.cfm?ID=641")
mybytes = fp.read()

mystr = mybytes.decode("utf8")
fp.close()

print(mystr)
