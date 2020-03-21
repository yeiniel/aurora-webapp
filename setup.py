import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="aurora-webapp",  # Replace with your own username
    version="0.0.1",
    author="Yeiniel Suarez Sosa",
    author_email="yeiniel@gmail.com",
    description="Aurora Web Application Framework",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yeiniel/aurora-webapp",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Framework",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI",
    ],
    python_requires='>=3.7',
    install_requires=[
        'WebOb>=1.2a1'
    ],
    extras_require={
        "development": ["nose", "sphinx", "flake8"]
    }
)
