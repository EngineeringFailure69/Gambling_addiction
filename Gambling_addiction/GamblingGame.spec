# -*- mode: python ; coding: utf-8 -*-

a = Analysis(
    ['start_screen.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('icons/casino_icon.webp', 'icons'),
        ('icons/door_icon.webp', 'icons'),
        ('icons/home_icon.webp', 'icons'),
        ('icons/work_icon.webp', 'icons'),
        ('background_photos/casino_roulette.jpg', 'background_photos'),
        ('background_photos/city_screen_background.webp', 'background_photos'),
        ('background_photos/home_background.png', 'background_photos'),
        ('background_photos/start_screen_background.webp', 'background_photos')
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
    a.binaries,
    a.datas,
    [],
    name='GamblingGame',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
