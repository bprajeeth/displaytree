from distutils.core import setup
VERSION="1.0.0"
setup(
  name = 'displaytree',        
  packages = ['displaytree'], 
  version = VERSION,   
  license='MIT',  
  description = 'Python package that helps you visualize your binary tree',  
  author = 'bprajeeth',               
  author_email = 'bprajeeth285@gmail.com',    
  url = 'https://github.com/bprajeeth/displaytree',  
  download_url = 'https://github.com/bprajeeth/displaytree/archive/refs/tags/v1.0.0.tar.gz',  
  keywords = ['BINARY TREE', 'PRINT', 'VISUALIZE', 'TREE', 'PRINT BINARY TREE', 'DISPLAY'], 
  install_requires=[],
  classifiers=[
    'Intended Audience :: Developers', 
    'Intended Audience :: Education',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 3',

  ],
)
