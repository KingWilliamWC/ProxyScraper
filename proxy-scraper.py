""""
  _____                                  _____                                      
 |  __ \                                / ____|                                     
 | |__) |_ __  ___ __  __ _   _  ______| (___    ___  _ __  __ _  _ __    ___  _ __ 
 |  ___/| '__|/ _ \\ \/ /| | | ||______|\___ \  / __|| '__|/ _` || '_ \  / _ \| '__|
 | |    | |  | (_) |>  < | |_| |        ____) || (__ | |  | (_| || |_) ||  __/| |   
 |_|    |_|   \___//_/\_\ \__, |       |_____/  \___||_|   \__,_|| .__/  \___||_|   
                           __/ |                                 | |                
                          |___/                                  |_|                
                        
                        Made By William Wolseley-Charles
"""
__author__ = "William Wolseley-Charles"
__copyright__ = "Copyright 2021, William Wolseley-Charles Propietary property"
__credits__ = ["William Wolseley-Charles", "Symir Aliu"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "William Wolseley-Charles"
__email__ = "17WWolseley-charles@worcs.tgacademy.org.uk"
__status__ = "Development"

import argparse
import requests

def call_proxy(limit, serveType, port, output_file):
    base_url = 'https://www.proxyscan.io/api/proxy'
    urlAddedParam = False
    urlParamAdd = "?"
    if(serveType != "*"):
        base_url += "type={}".format(serveType)
        urlAddedParam = True
        urlParamAdd = "&"
    if(port != 0 and port > 0):
        urlParamAdd = "&"
        if(urlAddedParam):
            base_url += "&port={}".format(port)
        else:
            base_url += "?port={}".format(port)
    
    results = []
    if(limit <= 20):
        base_url += '{}limit={}'.format(urlParamAdd,limit)
        urlParamAdd = "&"
        request = requests.get(base_url)
        data = request.json()
        if(len(data) > 0):
            for proxy in data:
                results.append("{}:{}".format(proxy['Ip'], proxy['Port']))
    else:
        for i in range(int(limit / 20)):
            new_url = base_url
            new_url += '{}limit=20'.format(urlParamAdd)
            request = requests.get(new_url)
            data = request.json()
            if(len(data) > 0):
                for proxy in data:
                    results.append("{}:{}".format(proxy['Ip'], proxy['Port']))
        base_url += '{}limit={}'.format(urlParamAdd,limit % 20)
        request = requests.get(base_url)
        data = request.json()
        if(len(data) > 0):
            for proxy in data:
                results.append("{}:{}".format(proxy['Ip'], proxy['Port']))

    
    if(len(results) > 0):
        if(len(results) < limit):
            print("Unable to fill limit, only got: {} proxies".format(len(results)))
        print("Saving to file: {}".format(output_file))
        with open(output_file, "w+") as text_file:
            text_file.write("{}".format(results[0]))
            del results[0]
            for result in results:
                text_file.write("\n{}".format(result))
    else:
        print("Unable to find any proxies with the current paramters, please try again or change them")


def parseArguments():
    parser = argparse.ArgumentParser(description="Scrapes proxies and outputs to a file", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-limit', action='store', metavar='[1-3000]', type=int, help='limit on the amount of proxies to scrape', default=10)
    parser.add_argument('-type', action='store', metavar='http,https,socks4,socks5', type=str, help='protocol of the serving proxy', default='*')
    parser.add_argument('-port', action='store', metavar='[any number]', type=int, help='port of the serving proxy, defaults to all', default=0)
    parser.add_argument('-output', action='store', metavar='[output_file_name.txt]', type=str, help='where the results will be stored txt file', default='results.txt')
    args = parser.parse_args()
    call_proxy(args.limit, args.type, args.port, args.output)
if __name__ == "__main__":
    print("""
  _____                                  _____                                      
 |  __ \                                / ____|                                     
 | |__) |_ __  ___ __  __ _   _  ______| (___    ___  _ __  __ _  _ __    ___  _ __ 
 |  ___/| '__|/ _ \\ \/ /| | | ||______|\___ \  / __|| '__|/ _` || '_ \  / _ \| '__|
 | |    | |  | (_) |>  < | |_| |        ____) || (__ | |  | (_| || |_) ||  __/| |   
 |_|    |_|   \___//_/\_\ \__, |       |_____/  \___||_|   \__,_|| .__/  \___||_|   
                           __/ |                                 | |                
                          |___/                                  |_|                
                        
                        Made By William Wolseley-Charles
""")
    print("for help, type -h")
    parseArguments()