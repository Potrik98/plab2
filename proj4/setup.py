from setuptools import setup

setup(name='calculator',
      version='0.1',
      description='calculator',
      url='http://github.com/potrik98/plab2',
      author='Erling Rorvik',
      author_email='potrik98@gmail.com',
      license='MIT',
      packages=['data', 'calculator'],
      install_requires=['numpy'],
      test_suite='nose.collector',
      tests_require=['nose'],
      zip_safe=False)
