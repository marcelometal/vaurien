from setuptools import setup, find_packages
from vaurien import __version__


install_requires = ['gevent', 'statsd-client', 'vaurienclient']

try:
    import argparse     # NOQA
except ImportError:
    install_requires.append('argparse')


with open('README.rst') as f:
    README = f.read()


classifiers = ["Programming Language :: Python",
               "License :: OSI Approved :: Apache Software License",
               "Development Status :: 1 - Planning"]


setup(name='vaurien',
      version=__version__,
      packages=find_packages(),
      description=("TCP Chaos Proxy"),
      long_description=README,
      author="Mozilla Foundation & contributors",
      author_email="services-dev@lists.mozila.org",
      include_package_data=True,
      zip_safe=False,
      classifiers=classifiers,
      install_requires=install_requires,
      test_requires=install_requires + ['nose', 'requests'],
      test_suite='nose.collector',
      entry_points="""
      [console_scripts]
      vaurien = vaurien.run:main
      """)
