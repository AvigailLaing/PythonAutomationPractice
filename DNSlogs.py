#Recursively go through all logs in /home/student/Public/log/dnslogs
#and return a sorted list of all the host names queried by the IP address
#8.9.74.225

import re #for RegEx
import pathlib #For working with files 

def lab333(the_data):
    answer = []
    log_path = pathlib.Path("./dnslogs")
    #Path variable points at directory
    for eachfile in log_path.glob("*"): # = All file types
        #Want to go through all files (do *.log for only log files)
        file_content = eachfile.read_text()
        print(f"Reading file: {eachfile.name}")
        ip_and_host = re.findall(r"client (.*?)#.*?: query: (.*?) IN A", file_content)
        for eachip,eachhost in ip_and_host:
            if eachip == the_data:
                answer.append(eachhost)
    return sorted(answer)
        
lab333("8.9.74.225")
#Debug console: little arrow: file_content
#We want client [ip address] and hostname
#client 251.92.84.43#59338: query: u-ads.adap.tv IN A
#re.findall(r"client 251.92.84.43#59338: query: u-ads.adap.tv IN A", file_content)
#shows 0 = that same client 251 entry and len() = 1 (there was 1 entry)
#modify re.findall, put parantheses around the IP address and client name
#re.findall(r"client (251.92.84.43)#59338: query: (u-ads.adap.tv) IN A", file_content)
#now 0 = '251.92.84.43', 'u-ads.adap.tv'
#and len() = 1
#re.findall(r"client .*?#.*?: query: .*? IN A", file_content)
#.*? for IP, port number, and DNS name, and it'll give us all of those entries
#Gives 0 = client 251.92#59338 query:
#re.findall(r"client (.*?)#(.*?): query: (.*?) IN A", file_content)
#Gives 0 = '251.92.84.43', '59338', u-ads.adap.tv