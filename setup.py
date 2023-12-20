from setuptools import setup, find_packages

setup(
    name='florida',
    version='0.0.5',
    author='WJB Mattingly',
    description='A collection of Python utilities to simplify coding tasks',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/wjbmattingly/florida',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
    install_requires=[
    ],
    include_package_data=True,
    keywords='python utilities tools'
)
