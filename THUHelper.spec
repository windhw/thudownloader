# -*- mode: python -*-

block_cipher = None


a = Analysis(['THUHelper.py'],
             pathex=['D:\\user\\user\\thudownloader'],
             binaries=None,
             datas=None,
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None,
             excludes=None,
             win_no_prefer_redirects=None,
             win_private_assemblies=None,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
          cipher=block_cipher)

# 来自http://yidao620c.github.io/blog/20150423/pyinstaller.html
# #############################################################
def extra_datas(mydir):
    def rec_glob(p, files):
        import os
        import glob
        for d in glob.glob(p):
            if os.path.isfile(d):
                files.append(d)
            rec_glob("%s/*" % d, files)
    files = []
    rec_glob("%s/*" % mydir, files)
    extra_datas = []
    for f in files:
        extra_datas.append((f, f, 'DATA'))

    return extra_datas

# append the 'extra' dir
a.datas += extra_datas('extra')
# #############################################################

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='THUHelper',
          debug=False,
          strip=None,
          upx=True,
          console=False, icon='extra\\MyDownloader.ico')
