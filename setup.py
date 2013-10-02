from setuptools import setup, find_packages

version = '4.3.0.0'

tests_require = [
    ]

setup(name='tomcom.plone.scripts',
      version=version,
      description='Little helpers',
      long_description=open("README.rst").read() + '\n' +
                       open('CHANGES.rst').read(),
      classifiers=[
        'Framework :: Plone',
        'Framework :: Plone :: 4.3',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        ],
      keywords='tomcom plone',
      author='tomcom GmbH',
      author_email='mailto:info@tomcom.de',
      url='https://github.com/tomcom-de//tomcom.plone.scripts',
      license='GPL2',
      packages=find_packages(),
      namespace_packages=['tomcom','tomcom.plone'],
      include_package_data=True,
      install_requires=[
        'setuptools',
      ],
      tests_require=tests_require,
      extras_require=dict(tests=tests_require,
                     ),
      zip_safe=False,
      entry_points={
        'console_scripts': ['i18n_to_template=tomcom.plone.scripts.i18n_to_template:main',
                           ]
      },
)

