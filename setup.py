"""keyutil package installation script"""

from setuptools import setup, find_packages


def readme():
    with open("README.rst") as f:
        return f.read()


setup(
    name="keyutil",
    version="0.1.0",
    url="http://github.com/lukassup/keyutil",
    description=("utility to generate SECRET_KEYs for securing "
                 "session data"),
    long_description=readme(),
    author="Lukas Šupienis",
    author_email="lukas.supienis@gmail.com",
    keywords="python cli keyutil secret django flask",
    license="BSD",
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
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Utilities",
    ],
    packages=find_packages(exclude=["tests"]),
    install_requires=[
        "docutils >=0.10",
        "six ==1.10",
    ],
    tests_require=[
        'nose',
    ],
    test_suite="nose.collector",
    zip_safe=True,
    entry_points={
        'console_scripts': [
            'keyutil=keyutil.keyutil:main',
        ],
    },
)
