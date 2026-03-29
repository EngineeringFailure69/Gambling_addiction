# -*- mode: python ; coding: utf-8 -*-
a = Analysis(
    ['start_screen.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('icons/*', 'icons'),
        ('background_photos/*', 'background_photos'),
        ('save_files/information.txt', 'save_files'),
        ('const.py', '.'),
        ('music_files/*', 'music_files')
    ],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='Gambling_addiction',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='Gambling_addiction',
)