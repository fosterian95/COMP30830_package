from importlib_metadata import entry_points
from setuptools import setup

setup(name='practical2_package',
      version='0.1',
      description='Package created for COMP30830 practical 2',
      url='https://github.com/fosterian95/COMP30830_package',
      author='fosterian95',
      author_email='fosterian95@gmail.com',
      license='MIT',
      packages=['practical2_package'],
      entry_points={
            'console_scripts': [
                  'sys_info_comp30830=__info__:main'
            ]
      },
      zip_safe=False)