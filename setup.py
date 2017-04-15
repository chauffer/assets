from setuptools import setup


setup(
    name='assets',
    version='0.1.0',
    url='https://github.com/chauffer/assets',
    author='Simone Esposito',
    author_email='chaufnet@gmail.com',
    download_url='https://github.com/chauffer/assets',
    description='Simple HTTP caching server',
    packages=['assets'],
    entry_points={'console_scripts': 'assets=assets:main'},
    include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ]
)
