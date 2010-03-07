#!/usr/bin/env python
# -*- coding: gbk -*-

from distutils.core import setup
import py2exe
from glob import glob


manifest = '''
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<assembly xmlns="urn:schemas-microsoft-com:asm.v1" manifestVersion="1.0">
<assemblyIdentity
    version="5.0.0.0"
    processorArchitecture="x86"
    name="MyDownloader"
    type="win32"
/>
<description>Program</description>
<dependency>
    <dependentAssembly>
        <assemblyIdentity
            type="win32"
            name="Microsoft.Windows.Common-Controls"
            version="6.0.0.0"
            processorArchitecture="X86"
            publicKeyToken="6595b64144ccf1df"
            language="*"
        />
    </dependentAssembly>
</dependency>
</assembly>
'''



includes = ["bitmaps"] 
options = {"py2exe":  
             {   "compressed": 1,  
                 "optimize": 2, 
                 #"includes": includes,          
                 "bundle_files": 1 
             }  
           }


MyDownloader = dict(
    script = "MyDownloader.py",
    icon_resources = [(1, "extra/MyDownloader.ico")],
    other_resources = [(24, 1, manifest)]
    )

setup(
    # The first three parameters are not required, if at least a
    # 'version' is given, then a versioninfo resource is built from
    # them and added to the executables.
    version = "0.5.0",
    description = u"网络学堂助手",
    name = "MyDownloader",
    data_files=[("extra",
                 ["extra/DownAll.png",
                "extra/DownFile.png",
                "extra/Notice.png",
                "extra/Refresh.png",
                "extra/Stop.png",
                "extra/Login.png",
                "extra/Hide.png",
                "extra/MyDownloader.ico",
                "extra/help.txt"])
                ],
    options = options,
    zipfile = None,
    windows = [MyDownloader]
    )
    
