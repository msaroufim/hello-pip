import setuptools

# Import github readme as long description
with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
     name='hello-pip',  
     version='0.1',
     scripts=['hello-pip'] ,
     author="Mark Saroufim",
     author_email="marksaroufim@gmail.com",
     description="How to submit a pip package",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/msaroufim/hello-pip",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: BSD License",
         "Operating System :: OS Independent",
     ],
 )