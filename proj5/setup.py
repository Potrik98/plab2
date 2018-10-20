from setuptools import setup

setup(name='keypad',
      version='0.1',
      description='keypad',
      url='http://github.com/potrik98/plab2',
      author='Erling Rorvik',
      author_email='potrik98@gmail.com',
      license='MIT',
      packages=['fsm'],
      install_requires=[],
      test_suite='nose.collector',
      tests_require=['nose', 'mock'],
      zip_safe=False)
