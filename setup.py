#!/usr/bin/env python
# -*- coding: gbk -*-

from distutils.core import setup
import py2exe
includes = ["bitmaps"] 
options = {"py2exe":  
             {   "compressed": 1,  
                 "optimize": 2, 
                 #"includes": includes,          
                 "bundle_files": 1 
             }  
           }

setup(
    # The first three parameters are not required, if at least a
    # 'version' is given, then a versioninfo resource is built from
    # them and added to the executables.
    version = "0.5.0",
    description = u"网络学堂助手",
    name = "MyDownloader",
    data_files=[("extra",
                 ["extra/DownAll.bmp",
                "extra/DownFile.bmp",
                "extra/Notice.bmp",
                "extra/Refresh.bmp",
                "extra/Stop.bmp",
                "extra/help.txt"]),("",["MyDownloader.exe.manifest",])],
    options = options,
    zipfile = None,
    windows = [{"script":"MyDownloader.py","icon_resources": [(1, "extra/MyDownloader.ico")]}]
    )
    
