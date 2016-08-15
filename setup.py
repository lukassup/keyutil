"""keyutil setup.py"""

from setuptools import setup, find_packages


def readme():
    with open("README.rst") as f:
        return f.read()

setup(name="keyutil",
      author="Lukas Šupienis",
      author_email="lukas.supienis@gmail.com",
      classifiers=[
          "Development Status :: 5 - Production/Stable",
          "Intended Audience :: Developers",
          "License :: OSI Approved :: GNU General Public License (GPL)",
          "Natural Language :: English",
          "Operating System :: OS Independent",
          "License :: OSI Approved :: MIT License",
          "Programming Language :: Python",
          "Programming Language :: Python :: 2.7",
          "Programming Language :: Python :: 3",
          "Programming Language :: Python :: 3.3",
          "Programming Language :: Python :: 3.4",
          "Programming Language :: Python :: 3.5",
          "Programming Language :: Python :: Implementation :: CPython",
          "Topic :: Utilities",
      ],
      description=("utility to generate SECRET_KEYs for securing "
                   "session data"),
      install_requires=[
          "docutils >=0.10",
          ],
      depends=[
          "six ==1.10",
          ],
      keywords="python cli keyutil secret django flask",
      license="BSD",
      long_description=readme(),
      packages=find_packages(exclude=["tests"]),
      test_suite="tests",
      url="http://github.com/lukassup/keyutil",
      version="0.1.0",
      zip_safe=True)
