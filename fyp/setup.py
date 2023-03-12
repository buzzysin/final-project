from setuptools import setup, find_packages

package_name = 'fyp'
version = '0.1.0'
install_requires = [
    'comet_ml',
    'ultralytics'
]
packages = find_packages()

setup(
    name=package_name,
    version=version,
    packages=packages,
    install_requires=install_requires,
    entry_points={
        'console_scripts': [
        ],
    },
)
