import bs4

import urllib.request

import bs4
import pymysql
import requests
from openpyxl import Workbook
from pyecharts import Pie, Bar,Grid,Line


def pageDown(URL):
    header = {"user-agent":"Mozilla"}
    request = urllib.request.Request(URL,headers = header)
    response = urllib.request.urlopen(request)
    return response.read().decode("utf-8")


def parsePage(page):#解析网页中的职位信息
    soup = bs4.BeautifulSoup(page,"html.parser")
    sellList =soup.find("div",class_="detail-cover").find_all("ul")
    print(len(sellList))
    sell=[]
    for item in sellList[1:]:
        date=item.select(".c1")[0].get_text(strip=True)
        daysell=item.select(".c2")[0].get_text(strip=True)
        sellpersent=item.select(".c3")[0].get_text(strip=True)
        persent=item.select(".c4")[0].get_text(strip=True)
        person=item.select(".c5")[0].get_text(strip=True)
        row={
            "date":date,
            "daysell":daysell,
            "sellpersent":sellpersent,
            "persent":persent,
            "person":person
        }
        sell.append(row)
    return sell

def generate_data(sell):
    date =[]
    daysell = []
    for item in sell:
        date.append(item['date'])
        daysell.append(item['daysell'])
    return  date,daysell

def show_report(data):
    attrs=data[0]
    values=data[1]
    pie = Pie("票房饼图"+"\n", title_pos='auto',width=800,height=800)
    pie.add( " ", attrs, values, is_lable_show=True, is_legend_show=True)
    pie.render("output/票房饼图.html")

def show_report2(data):
    attrs=data[0]
    values=data[1]
    bar = Bar("票房柱状图"+"\n", title_pos='auto',width=800,height=800)
    bar.add( " ", attrs, values, is_lable_show=True, is_legend_show=True)
    bar.render("output/票房柱状图.html")

def show_report3(data):
    attrs=data[0]
    values=data[1]
    line = Line("票房折线图"+"\n", title_pos='auto',width=800,height=800)
    line.add( " ", attrs, values, is_lable_show=True, is_legend_show=True)
    line.render("output/票房折线图.html")


if __name__ == "__main__":
    data=pageDown("http://m.maoyan.com/movie/1228869/box")
    sells = parsePage(data)
    datas = generate_data(sells)
    show_report(datas)
    show_report2(datas)
    show_report3(datas)
    print(sells)