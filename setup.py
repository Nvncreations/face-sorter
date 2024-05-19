from setuptools import setup
setup(
    name = 'face_sorter',
    version = '0.1.0',
    packages = ['face_sorter'],
    install_requires=['face_recognition','tdqm'],
    package_dir={'face_sorter':'face_sorter'},
    entry_points = {
        'console_scripts': [
            'face_sorter = face_sorter.__main__:main'
        ]
    })