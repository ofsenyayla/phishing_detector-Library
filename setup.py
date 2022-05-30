from setuptools import find_packages, setup

setup(
    name='phishing_detector',
    packages=find_packages(include=['phishing_detector']),
    version='0.1.0',
    description='Library that questions whether a site is phishing or not',
    author='ofaruk',
    license='MIT',
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent"
    ],
    install_requires=['requests', 'validators', 'pandas'],
)
