from setuptools import setup, find_packages

with open('./README.md', 'r') as file :
    long_description = file.read()
with open('./requirements.txt','r') as file :
    requires = [package.strip('\n ') for package in file.readlines()]
AUTHOR_USER_NAME = 'HarishKumarSedu'
AUTHOR_EMAIL = 'harishkumarsedu@gmail.com'
REPO_NAME = 'IVM6303'
setup(
    name=f'{REPO_NAME}',
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    version='0.0.1',
    description=[ 'text/markdown','text/x-rst',],
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    long_description=long_description,
    packages=find_packages(include="*"),
    requires=requires,
    py_modules=['./src']
    
)