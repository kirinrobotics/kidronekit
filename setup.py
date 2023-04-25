import setuptools
import os

version = '1.0.0'

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as f:
    LongDescription = f.read()

setuptools.setup(
    name='kidronekit',
    zip_safe=True,
    version=version,
    description='Premium extended version of dronekit.',
    long_description_content_type="text/markdown",
    long_description=LongDescription,
    url='https://github.com/kirinslab/kidronekit.git',
    author='3D Robotics, Kirinlab',
    install_requires=[
        'pymavlink>=2.2.20',
        'monotonic>=1.3',
    ],
    author_email='tim@3drobotics.com, kevinh@geeksville.com, haiquantran2897@gmail.com',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering',
    ],
    license='apache',
    packages=setuptools.find_packages()
)
