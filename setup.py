from setuptools import setup, find_packages

with open("README.md","r",encoding='utf-8') as f:
    long_description=f.read()


REPO_NAME="End_to_end-book_recommendation_sys"
AUTHOR_USER_NAME="Codesbalu"
SRC_REPO="books_recommendor"
LIST_OF_REQUIREMENTS=[]


setup(
    name=SRC_REPO,
    version="0.0.1",
    author="Codesbalu",
    description="A small local packages for ML based books recommondation",
    long_description=long_description,
    url="https://github.com/Codesbalu/End_to_end-book_recommendation_sys.git",
    auhtor_email="balajibalusbvb@gmail.com",
    packages=find_packages(),
    license="MIT",
    python_requires=">=3.7",
    install_requires=LIST_OF_REQUIREMENTS
)

