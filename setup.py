from setuptools import find_packages, setup


setup(
    name="hello-world-demo",
    version="0.2.1",
    description="Download and run the testfile release binary",
    packages=find_packages(),
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "helloworld=helloworld.cli:main",
        ],
    },
)
