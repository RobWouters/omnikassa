
import os

from setuptools import (
    setup,
    find_packages,
)

HERE = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(HERE, 'README.rst')).read()
CHANGES = open(os.path.join(HERE, 'CHANGES.rst')).read()

requires = [
]

setup(
    name='omnikassa',
    version='0.0.4',
    description='Python library for implementing Omnikassa',
    long_description=README + '\n\n' + CHANGES,
    classifiers=[
        "Programming Language :: Python",
    ],
    author='Rob Wouters',
    author_email='rob@rob-wouters.nl',
    url='https://github.com/RobWouters/omnikassa',
    download_url='https://github.com/RobWouters/omnikassa/tarball/0.0.4',
    keywords='python omnikassa payment',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=requires,
)
