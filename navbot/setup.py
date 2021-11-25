from setuptools import setup
import os
from glob import glob
package_name = 'navbot'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share',package_name),glob('launch/*.py')),
        (os.path.join('share',package_name),glob('description/*')),
        (os.path.join('share',package_name),glob('rviz/*')),
        (os.path.join('share',package_name),glob('meshes/*')),


    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='markostamos',
    maintainer_email='gimarkostamos@gmail.com',
    description='template for Ros2-gazebo',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
