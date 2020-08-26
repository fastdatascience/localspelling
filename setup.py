from distutils.core import setup
setup(
  name = 'localspelling',
  packages = ['localspelling'],
  version = '0.1',
  license='MIT', 
  description = 'Translates input between UK and US spelling',  
  author = 'Thomas Wood',                 
  author_email = 'thomas@fastdatascience.com',      
  url = 'https://fastdatascience.com',   
  download_url = 'https://github.com/fastdatascience/localspelling/archive/v_01.tar.gz',
  keywords = ['spelling', 'localisation', 'localization', 'uk', 'us', 'british english', 'us english'],   # Keywords that define your package best
  install_requires=[            
          
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',   
    'Intended Audience :: Developers',   
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT',
    'Programming Language :: Python :: 3',   
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
  include_package_data=True,
)
