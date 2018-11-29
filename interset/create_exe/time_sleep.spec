# -*- mode: python -*-

block_cipher = None


a = Analysis(['time_sleep.py'],
             pathex=['/Users/gouweiqi/Documents/code_py/code_file/interset/create_exe'],
             binaries=[],
             datas=[],
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
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='time_sleep',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False , icon='football.ico')
app = BUNDLE(exe,
             name='time_sleep.app',
             icon='football.ico',
             bundle_identifier=None)
