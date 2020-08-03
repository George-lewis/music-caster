# -*- mode: python ; coding: utf-8 -*-
import os
from PyInstaller.config import CONF
CONF['distpath'] = './dist'
block_cipher = None
# noinspection PyUnresolvedReferences
a = Analysis([f'{os.getcwd()}/music_caster.py'],
             pathex=[os.getcwd()],
             binaries=[],
             datas=[],
             hiddenimports=['pkg_resources.py2_warn'],
             hookspath=[],
             runtime_hooks=[],
             excludes=['pandas', 'simplejson', 'PySide2'],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
# noinspection PyUnresolvedReferences
pyz = PYZ(a.pure, a.zipped_data,
          cipher=block_cipher)
# noinspection PyUnresolvedReferences
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='Music Caster',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=False,
          upx_exclude=['vcruntime140.dll', 'msvcp140.dll', 'python36.dll', 'python37.dll', 'python38.dll'],
          runtime_tmpdir=None,
          console=False, version='mc_version_info.txt', icon=os.path.abspath('resources/Music Caster.ico'))
