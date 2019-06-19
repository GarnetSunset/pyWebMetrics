def makeSignature():
    import calendar
    import hashlib
    import os
    import time
    from builtins import input
    from base64 import b64decode, b64encode

    try:
        input = raw_input
    except NameError:
        pass
    
    if not os.path.exists('webmetrics.api'):
        apiSec = input("Input the API Secret from WebMetrics\n>")
        while len(apiSec) != 40:
            apiSec = input("Input the API Secret from WebMetrics,\n it must be 40 characters long\n>")
        apiFile = open("webmetrics.api", "w")
        apiFile.write(apiSec)
        apiFile.close()
    else:
        with open('webmetrics.api', 'r') as file:
            apiSec = file.read().replace('\n', '')
            if len(apiSec) != 40:
                while len(apiSec) != 40:
                    apiSec = input("Input the API Secret from WebMetrics,\n it must be 40 characters long\n>")
                apiFile = open("webmetrics.api", "w")
                apiFile.write(apiSec)
                apiFile.close()
    if not os.path.exists('webmetrics.user'):
        userName = input("Input the Username from WebMetrics\n>")
        apiFile = open("/webmetrics.user", "w")
        apiFile.write(apiSec)
        apiFile.close()
    else:
        with open('webmetrics.user', 'r') as file:
            userName = file.read().replace('\n', '')
    epoch = calendar.timegm(time.gmtime())
    epoch = str(epoch)
    combined = userName+apiSec+epoch
    combinedEncoded = combined.encode('utf-8')
    signature = b64encode(hashlib.sha1(combinedEncoded).digest()).decode("utf-8") 
    return signature
