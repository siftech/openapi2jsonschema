from setuptools import setup

setup(
    name="openapi2jsonschema",
    version="1.0.1",
    description="Converts openAPI YAML into JSON. Modified from https://github.com/instrumenta/openapi2jsonschema",
    author="",
    author_email="",
    packages=["openapi2jsonschema"],  # same as name
    install_requires=[
        "click==7.0",
        "colorama==0.4.1",
        "jsonref==0.2",
        "pyyaml>=5.1",
    ],  # external packages as dependencies
    scripts=[],
)
