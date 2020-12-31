from setuptools import find_packages, setup


setup(
    name = 'testapp',
    version='1.0.0',
    packages = find_packages(),
    include_package_data = True,
    zip_safe = False,
    install_requiers=[
        'flask',
    ],
)