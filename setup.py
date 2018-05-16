from distutils.core import setup
import py2exe

import glob

import warnings
warnings.simplefilter(action = 'ignore', category = UserWarning )
 
opts={
          "py2exe":
          {
              'packages': ['FileDialog'],
              "includes": ["sip", "PyQt4.QtGui", "matplotlib.backends",  "matplotlib.backends.backend_qt4agg",
                               "matplotlib.figure","pylab", "numpy", "decimal",
                               "matplotlib.backends.backend_tkagg", "pandas"],
                'excludes': ['_gtkagg', '_tkagg', '_agg2', '_cairo', '_cocoaagg',
                             '_fltkagg', '_gtk', '_gtkcairo', ],
                'dll_excludes': ['libgdk-win32-2.0-0.dll',
                                 'libgobject-2.0-0.dll', 'OCI.dll']
              }
       }

# Save matplotlib-data to mpl-data ( It is located in the matplotlib\mpl-data
# folder and the compiled programs will look for it in \mpl-data
# note: using matplotlib.get_mpldata_info
data_files = [
    (r'mpl-data', glob.glob(r'C:\Users\Bordee\Desktop\venv\Lib\site-packages\matplotlib\mpl-data\*.*')),
                    # Because matplotlibrc does not have an extension, glob does not find it (at least I think that's why)
                    # So add it manually here:
<<<<<<< HEAD
                  (r'mpl-data', [r'C:\Users\Bordee\Desktop\venv\Lib\site-packages\matplotlib\mpl-data\matplotlibrc']),
                  (r'mpl-data\images',glob.glob(r'C:\Users\Bordee\Desktop\venv\Lib\site-packages\matplotlib\mpl-data\images\*.*')),
                  (r'mpl-data\stylelib',glob.glob(r'C:\Users\Bordee\Desktop\venv\Lib\site-packages\matplotlib\mpl-data\stylelib\*.*')),
                  (r'mpl-data\fonts',glob.glob(r'C:\Users\Bordee\Desktop\venv\Lib\site-packages\matplotlib\mpl-data\fonts\*.*')),
                  (r'resources',glob.glob(r'C:\Users\Bordee\Desktop\dataanalyzer\resources\*.*')),
=======
                  (r'mpl-data', [r'C:\Environment\Project\Lib\site-packages\matplotlib\mpl-data\matplotlibrc']),
                  (r'mpl-data\images',glob.glob(r'C:\Environment\Project\Lib\site-packages\matplotlib\mpl-data\images\*.*')),
                  (r'mpl-data\stylelib',glob.glob(r'C:\Environment\Project\Lib\site-packages\matplotlib\mpl-data\stylelib\*.*')),
                  (r'mpl-data\fonts',glob.glob(r'C:\Environment\Project\Lib\site-packages\matplotlib\mpl-data\fonts\*.*')),
                  (r'resources',glob.glob(r'C:\LaBCoV\resources\*.*')),
				  (r'',glob.glob(r'C:\LaBCoV\default_config.cfg')),
>>>>>>> da8870a7392830937b922194008b7ce023f60c97
			  # oracle files
			  (r'Oracle',glob.glob(r'C:\Users\Bordee\Desktop\venv\Lib\site-packages\Oracle\*.*')),
            (r'Oracle\instantclient_11_2',glob.glob(r'C:\Users\Bordee\Desktop\venv\Lib\site-packages\Oracle\instantclient_11_2\*.*')),
			  (r'Oracle\instantclient_11_2\vc8',glob.glob(r'C:\Users\Bordee\Desktop\venv\Lib\site-packages\Oracle\instantclient_11_2\vc8\*.*')),
			  (r'Oracle\instantclient_11_2\vc9',glob.glob(r'C:\Users\Bordee\Desktop\venv\Lib\site-packages\Oracle\instantclient_11_2\vc9\*.*')),
			  (r'Oracle\network\admin',glob.glob(r'C:\Users\Bordee\Desktop\venv\Lib\site-packages\Oracle\network\admin\*.*')),
                (r'', glob.glob(r'C:\Users\Bordee\Desktop\dataanalyzer\default_config.cfg'))
                  ]
                    # this will add all images which we've used. (first put them in folder named resources. and use your path inplace of mine)
 
# for console program use 'console = [{"script" : "scriptname.py"}]
setup(windows=[{"script" : "UserLogin.py",
                "icon_resources": [(1, "analytic_icon.ico"),]}],
                  options=opts, data_files=data_files)
