import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
     name='slack_utils',
     version='0.1',
     author="Luis Cruz",
     author_email="lcruzc@gmail.com",
     description="A Slack utils package for working with block and dialogs",
     long_description=long_description, long_description_content_type="text/markdown",
     url="https://github.com/lcruz/slack_utils",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )
