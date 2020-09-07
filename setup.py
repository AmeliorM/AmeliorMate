import setuptools

REQUIRED = [
    "openai"
]

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="AmeliorMate-AmeliorM",
    version="0.0.2",
    author="Katie Evanko-Douglas",
    author_email="katie@ameliormate.com",
    description="A a few methods for making GPT3 chatbots",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AmeliorM/AmeliorMate",
    packages=setuptools.find_packages(),
    install_requires=REQUIRED,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)