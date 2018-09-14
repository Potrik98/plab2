from setuptools import setup

setup(name='paper_scissors_rock',
      version='0.1',
      description='Paper scissors rock',
      url='http://github.com/potrik98/plab2',
      author='Erling Rorvik',
      author_email='potrik98@gmail.com',
      license='MIT',
      packages=['paper_scissors_rock'],
      test_suite='nose.collector',
      tests_require=['nose'],
      zip_safe=False)
