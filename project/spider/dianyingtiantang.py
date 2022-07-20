# Author:wth
from lxml import etree
import requests

BASE_DOMAIN = 'https://www.dytt8.net'
# 1.将目标网站上的页面抓取下来

HEADERS = {
    "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36"
}
# 头文件，负责传送给服务器相关信息
"""
    xpath和python代码不同。不是以0开头p[1]代表第一个paragraph
    nodename选取此节点的所有子节点
    /从当前节点选取直接子节点
    //从当前节点选取子孙节点
    .选取当前节点
    ..选取当前节点的父节点
    @选取属性
    """


def get_detail_url(url):
    # https://www.dytt8.net/html/gndy/dyzz/list_23_1.html
    response = requests.get(url, headers=HEADERS)
    # 通过get从url返回信息，传送头文件

    # requests库，默认会使用自己猜测的编码方式将抓取的网页解码 抓取页面乱码
    text = response.content.decode(encoding='gbk', errors='ignore')
    # 将返回的信息保存到text里面
    html = etree.HTML(text)
    # etree.HTML()可以用来解析字符串格式的HTML文档对象，将传进去的字符串转变成_Element对象。
    # 作为_Element对象，可以方便的使用getparent()、remove()、xpath()等方法。
    detail_urls = html.xpath("//table[@class='tbspan']//a/@href")

    # table节点下class为tbspan属性下的href属性值
    #<a href = "/html/gndy/dyzz/20220614/62703.html"
    '''
<table width="100%" border="0" cellspacing="0" cellpadding="0" class="tbspan" style="margin-top:6px">
<tr> 
<td height="1" colspan="2" background="/templets/img/dot_hor.gif"></td>
</tr>
<tr> 
<td width="5%" height="26" align="center"><img src="/templets/img/item.gif" width="18" height="17"></td>
<td height="26">
	<b>
		
		<a href="/html/gndy/dyzz/20220614/62703.html" class="ulink">2021年悬疑《99.9：刑事专业律师电影版》BD日语中字</a>
	</b>
</td>
</tr>
<tr> 
<td height="20" style="padding-left:3px">&nbsp;</td>
<td style="padding-left:3px">
				<font color="#8F8C89">日期：2022-06-13 00:37:12 
 </font>
		
				</td>
</tr>
<tr> 
<td colspan="2" style="padding-left:3px">◎译 名 99.9:刑事专业律师 电影版 / 99.9不可能的翻案The MOVIE / 电影版 99.9 不可能的翻案(台) ◎片 名 99.9-刑事専門弁護士-THE MOVIE ◎年 代 2021 ◎产 地 日本 ◎类 别 悬疑/犯罪 ◎语 言 日语 ◎字 幕 中文 ◎上映日期 2021-12-30(日本) ◎IMDb评分 6.7/10 fro</td>
</tr>
</table>
    '''
    detail_urls = map(lambda url: BASE_DOMAIN + url, detail_urls)
    # detail_urls 的每一个值都加上BASE_DOMAIN
    return detail_urls


def parse_detail_page(url):
    movie = {}
    response = requests.get(url, headers=HEADERS)
    text = response.content.decode(encoding='gbk', errors='ignore')
    html = etree.HTML(text)
    title = html.xpath("//div[@class='title_all']//font[@color='#07519a']/text()")[0]
    movie['title'] = title

    zoomE = html.xpath("//div[@id='Zoom']")[0]
    imgs = zoomE.xpath("//img/@src")
    cover = imgs[0]
    movie['cover'] = cover
    infos = zoomE.xpath(".//text()")

    def parse_info(info, rule):
        return info.replace(rule, "").strip()

    for index, info in enumerate(infos):
        if info.startswith('◎年　　代'):
            info = parse_info(info, '◎年　　代')
            movie['year'] = info
        elif info.startswith("◎产　　地"):
            info = parse_info(info, "◎产　　地").strip()
            movie['country'] = info
        elif info.startswith("◎类　　别"):
            info = parse_info(info, "◎类　　别").strip()
            movie['category'] = info
        elif info.startswith("◎豆瓣评分"):
            info = parse_info(info, "◎豆瓣评分").strip()
            movie['douban_rating'] = info
        elif info.startswith("◎片　　长"):
            info = parse_info(info, "◎片　　长").strip()
            movie['duration'] = info
        elif info.startswith("◎导　　演"):
            info = parse_info(info, "◎导　　演").strip()
            movie['director'] = info
        elif info.startswith("◎主　　演"):
            info = parse_info(info, "◎主　　演")
            actors = [info]
            for x in range(index + 1, len(infos)):
                actor = infos[x].strip()
                if actor.startswith("◎"):
                    break
                actors.append(actor)
            movie['actors'] = actors
        elif info.startswith("◎简　　介"):
            # info = parse_info(info, "◎简　　介").strip()
            for x in range(index + 1, len(infos)):
                profile = infos[x].strip()
                if profile.startswith("◎") or profile.startswith("【下载地址】"):
                    break
                movie['profile'] = profile
    download_url = html.xpath("//td[@bgcolor='#fdfddf']/a/@href")
    movie['download_url'] = download_url
    return movie


def spider():
    base_rl = "https://www.dytt8.net/html/gndy/dyzz/list_23_{}.html"
    movies = []
    i = 1
    for x in range(1, 8):
        # 第一个for循环控制总共有7页
        url = base_rl.format(x)
        # 将x插入base_rl
        detail_urls = get_detail_url(url)

        for detail_url in detail_urls:
            # 第二个for循环遍历一页中电影详情
            try:
                movie = parse_detail_page(detail_url)
            except:
                continue
            movies.append(movie)
            print("正在爬取第%s部电影" % (i))
            i = i + 1
    # 把数据写入文件
    for i in range(len(movies)):
        try:
            with open('moves.csv', 'a+', encoding='utf-8') as file:
                file.write("标题" + '\t' + movies[i]['title'] + '\n')
                file.write("封面链接" + '\t' + movies[i]['cover'] + '\n')
                file.write("年代" + '\t' + movies[i]['year'] + '\n')
                file.write("产地" + '\t' + movies[i]['country'] + '\n')
                file.write("类别" + '\t' + movies[i]['category'] + '\n')
                file.write("豆瓣评分" + '\t' + movies[i]['douban_rating'] + '\n')
                file.write("片长" + '\t' + movies[i]['duration'] + '\n')
                file.write("导演" + '\t' + movies[i]['director'] + '\n')
                # file.write("主演" + '\t' + movies[i]['actors'][:] + '\n')
                file.write("简介" + '\t' + movies[i]['profile'] + '\n')
                file.write("下载链接" + '\t' + movies[i]['download_url'][0] + '\n')
                file.write("=" * 50)
                file.write("\n")
        except:
            with open('moves.csv', 'a+', encoding='utf-8') as file:
                file.write("=" * 50)
                file.write("\n")
            pass
        print("正在写入第%s部电影" % (i + 1))


if __name__ == '__main__':
    spider()
