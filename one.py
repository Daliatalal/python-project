
def OpenLogs(file):
    f = open('file2.txt', 'r')
    lst_lines = f.readlines()
    lst_output = []
    for log in lst_lines:
        lst_output.append(log.split())
    return lst_output

def parseLogs(lst_output):
    IPs = []
    URIs = []
    AccessMethods = []
    UserAgents = []
    i = 0
    for log in lst_output:
        IPs.append(log[0])
        AccessMethods.append(log[5][1:])
        URIs.append(log[6])
        UserAgents.append(' '.join(log[11:-1]))
        print(" IP: "+IPs[i]+" Access Method: "+AccessMethods[i]+" URI: "+URIs[i]+" UserAgents: "+UserAgents[i])
        i=i+1
    return IPs, URIs, AccessMethods, UserAgents

if __name__ == "__main__":
    lst_output = OpenLogs('file2.txt')
    IPs ,URIs, AccessMethods , UserAgents = parseLogs(lst_output)

    #Unique#
    UIPs = set(IPs)
    UURIs = set(URIs)
    UAccessMethods = set(AccessMethods)