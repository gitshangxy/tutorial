import requests, re, json, pymongo
from multiprocessing import Pool

class JRTTSpider(object):
    def __init__(self):
        self.key_word = '街拍'
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36'}
        self.api = 'https://www.toutiao.com/api/search/content/?aid=24&app_name=web_search&offset=0&format=json&keyword={}&autoload=true&count=20&en_qc=1&cur_tab=1&from=search_tab&pd=synthesis'.format(self.key_word)
        # 创建数据库对象
        self.client = pymongo.MongoClient(host='localhost')
        # 根据数据库对象，创建数据库；非关系型数据库不需要提前创建数据库和表，直接在代码中指定就可以了，会自动创建。但是关系型数据库需要提前将数据库和表创建好，否则无法连接数据库。
        self.db = self.client['jrtt']

    def parse_api(self, offset=0):
        """
        请求并解析列表页的api接口
        :param offset: api接口的请求偏移量
        :return: 返回详情页的url地址
        """
        url = self.api + '&offset=' + str(offset)
        response = requests.get(url=url, headers=self.headers)
        if response.status_code == 200:
            json_dict = json.loads(response.text)
            has_more = json_dict.get('has_more')
            datas = json_dict.get('data')
            for dic in datas:
                if 'abstract' in dic and 'single_mode' not in dic:
                    detail_url = dic['article_url']
                    yield detail_url
            # 在当前页的数据提取完毕之后，开始获取下一个列表页的数据
            # if has_more == 1:
            #     # 有下一页
            #     offset += 20
            #     self.parse_api(offset)
            # else:
            #     # 没有下一页
            #     print('数据已经请求完毕')
        else:
            print('请求接口状态码异常:{}'.format(response.status_code))

    def parse_detail(self, detail_url):
        """
        请求并解析详情页的图片的url地址，并将图片保存至数据库，且将图片下载到本地。
        :param detail_url:
        :return:
        """
        response = requests.get(url=detail_url, headers=self.headers)
        if response.status_code == 200:
            # 经过观察，可以发现在网页源代码中，存在图片的json字符串，是在js代码中的。
            json_str = re.search(re.compile(r'gallery: JSON.parse\("(.*?)"\),', re.S), response.text).group(1).replace('\\', '')
            json_dict = json.loads(json_str)

            self.db['tt'].insert_one(json_dict)
            sub_images = json_dict['sub_images']
            for img_dict in sub_images:
                img_url = img_dict['url']
                print(img_url)

    def download_image(self, img_url):
        content = requests.get(img_url, headers=self.headers).content
        img_name = img_url.split('/')[-1]
        with open(img_name+'jpg', 'wb')as f:
            f.write(content)

if __name__ == '__main__':
    obj = JRTTSpider()
    generator = obj.parse_api()
    for detail_url in generator:
        obj.parse_detail(detail_url)

