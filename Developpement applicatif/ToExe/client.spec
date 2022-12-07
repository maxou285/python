# -*- mode: python ; coding: utf-8 -*-

from kivymd import hooks_path as kivymd_hooks_path
block_cipher = None


a = Analysis(
    ['client.py'],
    pathex=[],
    binaries=[('ChunkFivePrint.otf', '.')],
    datas=[('*.kv', '.'),('ding.wav', '.'), ('ChunkFivePrint.otf', '.'), ('icon.png','.')],
    hiddenimports=["kivymd.icon_definitions"],
    hookspath=[kivymd_hooks_path],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
a.datas += [('Chunk Five Print.otf', 'src/ChunkFivePrint.otf', "DATA")]
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='client',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['icon.ico'],
)
app = BUNDLE(
    exe,
    name='client.app',
    icon='icon.ico',
    bundle_identifier=None,
)

# -*- mode: python ; coding: utf-8 -*-

from kivymd import hooks_path as kivymd_hooks_path
block_cipher = None














