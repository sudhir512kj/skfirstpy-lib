from setuptools import find_packages, setup

setup(
    name='skpylib',
    packages=find_packages(include=['skpylib']),
    version='0.1.0',
    description='My first Python library',
    author='Sudhir Meena',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)
