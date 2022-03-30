from setuptools import setup

APP = ['YTDownloader.py']
OPTIONS = {
    'iconfile': 'YT-DownloaderLogo.icns',
    'argv_emulation': True,
    'packages': ['certifi'],
}

setup(
    app=APP,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)