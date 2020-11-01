"""将多个xml文件内容写入一个txt文件内，格式为：绝对地址，左上角标和左下角标，类别。"""
import os
import sys
import xml.etree.ElementTree as ET
import glob

def xml_to_txt(indir,outdir):
    f_w = open(outdir, 'w')
    os.chdir(indir)
    annotations = os.listdir('.')
    annotations = glob.glob(str(annotations)+'*.xml')
    for i, file in enumerate(annotations):
        # actual parsing
        in_file = open(file)
        tree=ET.parse(in_file)
        root = tree.getroot()
        for obj in root.iter('path'):
            f_w.write(str(obj.text)+',')
        for obj in root.iter('object'):
                current = list()
                name = obj.find('name').text
                xmlbox = obj.find('bndbox')
                xn = xmlbox.find('xmin').text
                xx = xmlbox.find('xmax').text
                yn = xmlbox.find('ymin').text
                yx = xmlbox.find('ymax').text
                #print xn
                f_w.write(xn+','+yn+','+xx+','+yx+',')
                f_w.write(str(name)+"\n")

indir='/home/lkx/E/dataset/1/csv/images'   #xml目录
outdir='/home/lkx/E/dataset/1/csv/labels.txt'  #txt目录

xml_to_txt(indir,outdir)

"""参考：
标注工具生成的xml文件转为txt格式
https://blog.csdn.net/Enjoy_endless/article/details/80819945
iFantasticMe
https://www.cnblogs.com/ifantastic/archive/2013/04/12/3017110.html
后续格式转换csv2coco/voc/labelme
https://github.com/spytensor/prepare_detection_dataset""""

