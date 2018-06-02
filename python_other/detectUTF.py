# -*- coding: utf-8 -*-
"""
os.path.abspath(path) #���ؾ���·��
os.path.basename(path) #�����ļ���
os.path.commonprefix(list) #���ض��·���У�����path���е����·����
os.path.dirname(path) #�����ļ�·��
os.path.exists(path)  #·�������򷵻�True,·���𻵷���False
os.path.lexists  #·�������򷵻�True,·����Ҳ����True
os.path.expanduser(path)  #��path�а�����"~"��"~user"ת�����û�Ŀ¼
os.path.expandvars(path)  #���ݻ���������ֵ�滻path�а����ġ�$name���͡�${name}��
os.path.getatime(path)  #�������һ�ν����path��ʱ�䡣
os.path.getmtime(path)  #�����ڴ�path�����һ���޸ĵ�ʱ�䡣
os.path.getctime(path)  #����path�Ĵ�С
os.path.getsize(path)  #�����ļ���С������ļ������ھͷ��ش���
os.path.isabs(path)  #�ж��Ƿ�Ϊ����·��
os.path.isfile(path)  #�ж�·���Ƿ�Ϊ�ļ�
os.path.isdir(path)  #�ж�·���Ƿ�ΪĿ¼
os.path.islink(path)  #�ж�·���Ƿ�Ϊ����
os.path.ismount(path)  #�ж�·���Ƿ�Ϊ���ص㣨��
os.path.join(path1[, path2[, ...]])  #��Ŀ¼���ļ����ϳ�һ��·��
os.path.normcase(path)  #ת��path�Ĵ�Сд��б��
os.path.normpath(path)  #�淶path�ַ�����ʽ
os.path.realpath(path)  #����path����ʵ·��
os.path.relpath(path[, start])  #��start��ʼ�������·��
os.path.samefile(path1, path2)  #�ж�Ŀ¼���ļ��Ƿ���ͬ
os.path.sameopenfile(fp1, fp2)  #�ж�fp1��fp2�Ƿ�ָ��ͬһ�ļ�
os.path.samestat(stat1, stat2)  #�ж�stat tuple stat1��stat2�Ƿ�ָ��ͬһ���ļ�
os.path.split(path)  #��·���ָ��dirname��basename������һ��Ԫ��
os.path.splitdrive(path)   #һ������windows�£���������������·����ɵ�Ԫ��
os.path.splitext(path)  #�ָ�·��������·�������ļ���չ����Ԫ��
os.path.splitunc(path)  #��·���ָ�Ϊ���ص����ļ�
os.path.walk(path, visit, arg)  #����path������ÿ��Ŀ¼������visit������visit����������3������(arg, dirname, names)��dirname��ʾ��ǰĿ¼��Ŀ¼����names����ǰĿ¼�µ������ļ�����args��Ϊwalk�ĵ���������
os.path.supports_unicode_filenames  #�����Ƿ�֧��unicode·����
"""
import os
import cchardet

def check_unicode(fileName, unicodePath = [], GBKPath = [], otherCode = []):
    with open(fileName, 'rb') as f:
        data = f.read()
        resDic = cchardet.detect(data) # {'encoding': 'GB2312', 'confidence': 0.99, 'language': 'Chinese'}
        print(fileName, resDic['encoding'])

def check_dir_unicode(rootdir):
    rootdir = 'D:\Algorithm\DesignPattern'
    for fpathe,dirs,fs in os.walk(rootdir):
        for f in fs:
            file = os.path.join(fpathe,f)
            if os.path.isfile(file):
                check_unicode(file)

def check_file_unicode(fileName):
    pass





