from setuptools import setup, find_packages

def read(file_name):
    """Read a text file and return the content as a string."""
    with io.open(
        os.path.join(os.path.dirname(__file__), file_name), encoding="utf-8"
    ) as f:
        return f.read()

setup(
    name='encodepacakge',  
    read("encodepacakge/version")),
    author="uptownaravi",
    author_email="uptownaravi@gmail.com",
    description="encode string with given template",
    #long_description_content_type="text/markdown",
    url="https://github.com/uptownaravi/encoder",
    package_dir={"": "encoder"},
    packages=find_packages(where="encoder"),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
 )
