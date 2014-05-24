from setuptools import setup, find_packages

setup(
    name='django-grappelli-template-editor',
    version='0.1',
    description='A TTW Template Editor for Grappelli',
    author='Curtis Maloney',
    author_email='curtis@tinbrain.net',
    url='http://github.com/funkybob/django-grappelli-template-editor',
    keywords=['django', 'grappelli',],
    packages = find_packages(),
    zip_safe=False,
    classifiers = [
        'Environment :: Web Environment',
        'Framework :: Django',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    requires = [
        'Django (>=1.6)',
    ],
    install_requires = [
        'Django>=1.6',
    ],
)
