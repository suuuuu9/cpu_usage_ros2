from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'cpu_usage_ros2'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*.launch.py'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='kiuchi',
    maintainer_email='kiuchi.ju@gmail.com',
    description='ROS2 node reading CPU usage',
    license='BSD-3-Clause',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'cpu_usage = cpu_usage_ros2.cpu_usage:main',
        ],
    },
)
