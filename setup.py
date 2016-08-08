from setuptools import setup, find_packages
import sys

lbforum = __import__('lbforum')

readme_file = 'README.rst'
try:
    long_description = open(readme_file).read()
except IOError:
    sys.stderr.write(
        "[ERROR] Cannot find file specified as "
        "``long_description`` (%s)\n" % readme_file
    )
    sys.exit(1)

install_requires = [
    'Django==1.10',
    'django-el-pagination==3.0',
    'easy_thumbnails==2.3',
    'postmarkup==1.2',
    'BeautifulSoup==3.2',
    'python-dateutil==2.5',
    'django-constance==1.2',
    'django_picklefield==0.3',
    'django-lbattachment==1',
    'django-lbutils==1',
]

setup(name='LBForum',
      version=lbforum.get_version(),
      description='A forum engine written in Python using Django',
      long_description=long_description,
      zip_safe=False,
      author='vicalloy',
      author_email='zbirder@gmail.com',
      url='https://github.com/vicalloy/LBForum',
      packages=find_packages(exclude=[]),
      include_package_data=True,
      install_requires=install_requires,
      test_suite='tests.main',
      classifiers=[
          'Development Status :: 4 - Beta',
          'Environment :: Web Environment',
          'Framework :: Django',
          'Framework :: Django :: 1.10',
          'Intended Audience :: Developers',
          'License :: BSD License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Topic :: Utilities'
      ],
      )
