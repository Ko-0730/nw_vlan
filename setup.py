from setuptools import setup, find_packages

setup(
    name='nw_vlan',
    version='0.1.0',
    packages=find_packages(),
    py_modules=['nw_vlan'],
    install_requires=[
        'PyYAML==6.0.1',
    ],
    entry_points={
        'console_scripts': [
            'nw_vlan = nw_vlan:main',
        ],
    },
)
