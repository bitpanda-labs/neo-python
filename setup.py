#!/usr/bin/env python3
"""The setup script."""

from setuptools import setup, find_packages

try:  # pip version >= 19.3
    from pip._internal.network.session import PipSession
except ImportError:
    try:  # pip version >= 10.0
        from pip._internal.download import PipSession
    except ImportError:  # pip version < 10.0
        from pip.download import PipSession

with open('README.rst') as readme_file:
    readme = readme_file.read()

# get the requirements from requirements.txt
with open("requirements.txt") as requirements_file:
    install_reqs = requirements_file.readlines()
reqs = [req for req in install_reqs if not req.startswith("#")]

setup(
    name='neo-python',
    python_requires='>=3.7',
    version='0.9.1',
    description="Python Node and SDK for the NEO blockchain",
    long_description=readme,
    author="Thomas Saunders",
    author_email='tom@cityofzion.io',
    maintainer="Erik van den Brink",
    maintainer_email='erik@cityofzion.io',
    url='https://github.com/CityOfZion/neo-python',
    packages=find_packages(include=['neo']),
    entry_points={
        'console_scripts': [
            'np-prompt=neo.bin.prompt:main',
            'np-api-server=neo.bin.api_server:main',
            'np-bootstrap=neo.bin.bootstrap:main',
            'np-reencrypt-wallet=neo.bin.reencrypt_wallet:main',
            'np-sign=neo.bin.sign_message:main',
            'np-export=neo.bin.export_blocks:main',
            'np-import=neo.bin.import_blocks:main',
            'np-utils=neo.Core.bin.cli:main',
        ],
    },
    include_package_data=True,
    install_requires=reqs,
    license="MIT license",
    zip_safe=False,
    keywords='neo, python, node',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
    ]
)
