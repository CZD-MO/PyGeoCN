from setuptools import setup, find_packages

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pygeo_cn',
    version='0.1.2',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'geopandas',
        'shapely',
    ],
    author='czd',
    author_email='caozuodong666@gmail.com',
    description='A package for reverse geocoding in China',
    long_description_content_type='text/markdown',
    url='https://github.com/CZD-MO/PyGeoCN',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
