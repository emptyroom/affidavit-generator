from distutils.core import setup
import py2exe

setup(windows=['generator.py'],
      options={'py2exe': {'packages':
                          ['Tkinter', 'docx', 'lxml._elementpath']}})
