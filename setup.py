from setuptools import setup, find_packages

setup(
    name="latex_generator",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],
    author="Dmitriy Yukachev",
    author_email="dim.youka4@gmail.com",
    description="Библиотека для генерации LaTeX-кода таблиц и изображений",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/latex_generator",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.12",
)
