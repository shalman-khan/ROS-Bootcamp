import os
from glob import glob
from setuptools import setup

package_name = 'tut4'

setup(
    name=package_name,
    version='0.7.0',
    packages=[package_name],
    install_requires=['setuptools'],
    zip_safe=True,
    author='rosi',
    author_email='adriel_ho@artc.a-star.edu.sg',
    maintainer='Adriel Ho',
    maintainer_email='adriel_ho@artc.a-star.edu.sg',
    keywords=['ROS'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    description='A simple ROS2 Python package',
    license='Apache License, Version 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'ar_tracking = tut4.ar_tracking:main',
            'maze_solver = tut4.maze_solver:main'
        ],
     },
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
        (os.path.join('share', package_name, 'config'), glob('config/*.yaml')),
        (os.path.join('share', package_name, 'worlds'), glob('worlds/*.model')),
    ],
)