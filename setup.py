from setuptools import find_packages,setup
setup(
    name='mcqgen',
    version='0.0.1',
    author='Ashish',
    author_email='ashishmehta10100@gmail.com',
    install_requires=["openai","langchain","streamlit","python-dotenv","pyPDF2"],
    packages=find_packages()
)