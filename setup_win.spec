# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

add_files = [
    ('./UIs', 'UIs'),
    ('./img', 'img')
]

app_name = 'GotoWork_PC_v2.1'

a = Analysis(['Main_v2.py'],
             pathex=['D:\\HG\\Programing\\GotoWork_PC'],
             binaries=[],
             datas=add_files,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name=app_name,
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name=app_name)
