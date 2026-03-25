from setuptools import setup, find_packages
setup(
    name="mental-health-latin-america-depression-anxiety-suicide-2000-2024",
    version="1.0.0",
    description="Mental health database for 18 Latin American countries (2000–2024): depression, anxiety, suicide rat",
    author="de la Serna, Juan Moisés",
    url="https://github.com/juanmoisesd/mental-health-latin-america-depression-anxiety-suicide-2000-2024",
    packages=find_packages(),
    install_requires=["pandas>=1.3.0","requests>=2.26.0"],
    python_requires=">=3.7",
    classifiers=["Programming Language :: Python :: 3","License :: OSI Approved :: MIT License","Topic :: Scientific/Engineering"],
    keywords="zenodo, open-data",
)