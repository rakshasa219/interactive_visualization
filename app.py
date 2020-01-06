#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from random import randrange
from flask import Flask, render_template, request
import pandas as pd
import csv, os
# 模块读进来,
app = Flask(__name__)

d2 = pd.read_csv('C:/ST/python/again1/data/suiciderate5.csv') #世界近年各国自杀率
d4 = pd.read_csv('C:/ST/python/again1/data/sun.csv') #世界各国日照率
d5 = pd.read_csv('C:/ST/python/again1/data/compare.csv',encoding="gbk")#全球近年分年龄段自杀率
d6 = pd.read_csv('C:/ST/python/again1/data/suicidebysex.csv',encoding="gbk")#全球近年性别自杀率
d7 = pd.read_csv('C:/ST/python/again1/data/work.csv',encoding="gbk")#全球近年男女参与劳动率


dict = { "世界各国日照率" : d4, "世界近年各国自杀率" : d2 ,"全球近年分年龄段自杀率" : d5, "全球近年男女参与劳动率" : d7,"全球近年性别自杀率":d6}#选择字典

regions_available_loaded = ['世界各国日照率','世界近年各国自杀率','全球近年分年龄段自杀率','全球近年男女参与劳动率','全球近年性别自杀率',]#选框内容


@app.route('/',methods=['GET'])
def run_2():
    
    data_str = d7.to_html()         #数据框
    
    regions_available = regions_available_loaded #下拉选单有内容
    return render_template('results2.html',
                           the_res = data_str,# 表
                           the_select_region=regions_available)   

@app.route('/qw',methods=['POST'])
def run_select() -> 'html':
    
    the_region = request.form["the_region_selected"]  ## 取得用户交互输入
    print(the_region)
    
    data_str = dict[the_region].to_html()#数据表

    #制作图表切换效果
    if the_region =="世界近年各国自杀率":
        with open("C:/ST/python/again1/1.html", encoding="utf8", mode="r") as f:
            plot_all = "".join(f.readlines())  
            
    elif the_region=="世界各国日照率":
        with open("C:/ST/python/again1/2.html", encoding="utf8", mode="r") as f:
            plot_all = "".join(f.readlines())
            
    elif the_region=="全球近年分年龄段自杀率":
        with open("C:/ST/python/again1/3.html", encoding="utf8", mode="r") as f:
            plot_all = "".join(f.readlines())
     
    elif the_region=="全球近年性别自杀率":
        with open("C:/ST/python/again1/4.html", encoding="utf8", mode="r") as f:
            plot_all = "".join(f.readlines())
        
    elif the_region=="全球近年男女参与劳动率":
        with open("C:/ST/python/again1/5.html", encoding="utf8", mode="r") as f:
            plot_all = "".join(f.readlines())
        
   
        
    
    regions_available =  regions_available_loaded  #下拉选单有内容
    return render_template('results2.html',
                            the_plot_all = plot_all,
                            the_res = data_str,
                            the_select_region=regions_available,
                           )

if __name__ == '__main__':
    app.run(port = 8030,debug=True)   # debug=True, 在py使用, 在ipynb不使用

