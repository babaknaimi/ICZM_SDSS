from distutils.core import setup
import py2exe



setup(windows=[{'script': 'DSS_Admin.py',
	'icon_resources': [(1, 'iczm16.ico')]}],
	options={
                "py2exe":{
                        "optimize": 2,
                         }
        }
)