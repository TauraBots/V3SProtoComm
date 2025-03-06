from setuptools import setup, find_packages

setup(
    name="V3SProtoComm",
    version="1.0.0",
    description="Pacote para comunicação e controle de robôs via Protobuf",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Thassio",
    author_email="thxssio@gmail.com",
    url="https://github.com/Taurabots/V3SProtoComm",
    packages=find_packages(),
    include_package_data=True, 
    install_requires=[
        "numpy",
        "protobuf",
        "six",
        "toml",
        "wrapt",
    ],
    extras_require={
        "dev": [
            "astroid",
            "isort",
            "lazy-object-proxy",
            "mccabe",
            "pylint",
        ]
    },
    entry_points={
        "console_scripts": [
            "gotoball=gotoball:gotoball",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
