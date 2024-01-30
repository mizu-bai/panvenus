import setuptools

setuptools.setup(
    name="panvenus96",
    version="0.1.0",
    author="mizu-bai",
    author_email="shiragawa4519@outlook.com",
    description="Read VENUS96 output.",
    url="https://github.com/mizu-bai/panvenus",
    packages=setuptools.find_packages(),
    classifiers=[],
    python_requires=">=3.8",
    install_requires=[
        "pyvenus96",
        "pandas",
    ],
)
