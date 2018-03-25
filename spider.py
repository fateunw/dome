import requests

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36Name'}
# 驼峰命名法
# 获取百度的搜索信息
def getBdMsg(keyword):
    res = requests.get('https://www.baidu.com/s?&wd={}'.format(keyword),headers=headers).text
    # print(res)
    return(res.replace('//www.baidu.com/img/baidu_jgylogo3.gif','static/images/github.png'))

if __name__ == '__main__':
    getBdMsg('python')