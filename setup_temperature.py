from setuptools import setup

setup(name='temp-convertor',
      version='0.2-dev',
      description='A Celsius-Fahrenheit Conversion Temperature Applet',
      author='Soheil Asadi',
      author_email='suheyl.asadi@gmail.com',
      REQUIRES_PYTHON='>=3.6.0',
      packages=['temp-convertor'],
      entery_points={
          'console_scripts': [
              'temp_run=temp-convertor.temperature:main',
          ],
      },
      )

__author__ = 'Soheil Asadi'
