from setuptools import setup, find_packages
 
setup(
    name='cab',
    version=__import__('cab').__version__,
    description='Basic Django snippets site',
    # long_description=open('docs/usage.txt').read(),
    author='Luke Hutscal',
    author_email='luke@creaturecreative.com',
    url='http://github.com/girasquid/cab/',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    include_package_data=True,
    zip_safe=False,
)