#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/12/22 0022 23:14
# @Author : Every spring Xu ( Mr.Xu Fengchun)
# @Email :<thomsenw005@gmail.com>
# @File : Unziprar_newyasuofile.py
# @desc : 解压zip rar文件到 A文件夹 然后删除其中的一个文件，在复制一个文件到 A文件夹 然后在压缩文件
#参考文章 https://mp.weixin.qq.com/s?__biz=MzUzODYwMDAzNA==&mid=2247506078&idx=2&sn=2a1f10fd58a3c17785403aaf8e4de84b&chksm=fad7af93cda0268580325936d99e1af3833b56e717cc15ddc583a5a3c873a5dc92bc90a16b3e&mpshare=1&scene=23&srcid=1222GZKXK5rIdGnj6Ae0vEAl&sharer_sharetime=1640186257868&sharer_shareid=31c094efd72d81d39286a0527dba8ba3#rd
#        https://www.cnblogs.com/dancesir/p/12765545.html


# file/2022/文件夹0113-文件夹0128是进行了把下载下来的压缩包里面文件删除，然后复制自己的文件到文件夹然后重新压缩了的

import rarfile

#rar解压的时候 路径需要决定路径  C:/xxx/xxx
def unrar(filename):
    rar = rarfile.RarFile(filename)
    print(rar.extractall())
    exit()
    if not os.path.isdir(filename + "_dir"):
        os.mkdir(filename + "_dir")
    os.chdir(filename + "_dir")
    rar.extractall()
    rar.close()


import  zipfile

def unzip(filename):
    zip_file = zipfile.ZipFile(filename)
    # 类似tar解除打包，建立文件夹存放解压的多个文件
    if not os.path.isdir(filename + "_dir"):
        os.mkdir(filename + "_dir")
    for names in zip_file.namelist():
        zip_file.extract(names, filename + "_dir/")
    zip_file.close()

from  pathlib import Path

# 压缩包(zip)是汉子中文的时候 使用的解压方法
#使用 zipfile 解压含有中文文件名的 zip 文件 会出现乱码
#https://cloud.tencent.com/developer/article/1087289
def chinese_unzip(filename):
    # zip_file = zipfile.ZipFile(filename)

    # 类似tar解除打包，建立文件夹存放解压的多个文件
    if not os.path.isdir(filename + "_dir"):
        os.mkdir(filename + "_dir")

    with zipfile.ZipFile(filename, 'r') as f:
        for fn in f.namelist():

            extracted_path = Path(f.extract(fn, filename + "_dir/"))
            extracted_path.rename(filename + "_dir/"+fn.encode('cp437').decode('gbk'))
    f.close()


#https://www.vectorhq.com/download/equalizer-psd-455612
def zipDir(dirpath, outFullName, name):
    """
    压缩指定文件夹
    :param dirpath: 目标文件夹路径
    :param outFullName: 压缩文件保存路径+xxxx.zip
    :return: 无
    """
    zip = zipfile.ZipFile(outFullName, "w", zipfile.ZIP_DEFLATED)
    for path, dirnames, filenames in os.walk(dirpath):
        # print(path,dirnames,filenames)
        # 去掉目标跟路径，只对目标文件夹下边的文件及文件夹进行压缩
        fpath = path.replace(dirpath,'')
        # print(fpath)
        for filename in filenames:
            # print(os.path.join(path, filename))
            # print(os.path.join(name + fpath, filename))

            #这个会把要压缩的文件所在的文件夹也压缩进去
            #zip.write(os.path.join(path, filename), os.path.join(name + fpath, filename))

            #这个有没那么多的层级结构，只把文件里里面的文件压缩进去
            #http://www.4k8k.xyz/article/sun_wangdong/79157682
            zip.write(os.path.join(path, filename), filename)
    zip.close()


from pyefun import *
from shutil import copy
import glob
import os
import  common

path=r'./file/2022/0129'  #这里修改要解压的文件夹  然后再此文件里下 新建 new_yasuozip目录 用于存放重新压缩后的zip文件存放
file_lst=glob.glob(path+'/*')

filename_lst=[os.path.basename(i) for i in file_lst]

print(filename_lst)

for filename in filename_lst:
    if '.' in filename:
        suffix = filename.split('.')[-1]

        if suffix == 'zip':

            yaunshifilename = 文本_取左边(filename, '.zip')
            print('默认的压缩包文件名', yaunshifilename)
            file_pat=path+'/'+filename
            print('zip',file_pat)
            unzip(file_pat)

            #删除解压后文件夹里面的指定文件
            remove_file=file_pat+"_dir"+'/vectorhq.com.url'
            # print(remove_file)
            if os.path.exists(remove_file):
                os.remove(remove_file)
                print("文件删除完毕")

            save_filepath=file_pat+"_dir"
            des=copy(r'./file/2022/Free PSD Files free download,Unlimited Download - free psd download.url',save_filepath)

            os.remove(file_pat) #删除压缩包.zip

            #压缩文件
            new_zip_filepath=path+'/new_yasuozip/'+yaunshifilename+'.zip'
            zipDir(save_filepath, new_zip_filepath, yaunshifilename)

            shutil.rmtree(path + '/' + yaunshifilename + '.zip' + '_dir')  # 删除解压后的文件夹和文件夹里文件
            print('*******文件重新压缩完毕*******')

        if suffix == 'rar':
            file_pat = path + '/' + filename
            print('rar',file_pat)
            unrar(file_pat)
            # os.remove(filename)