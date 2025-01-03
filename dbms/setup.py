from setuptools import setup, find_packages

setup(
    name="dbms",
    version="1.0.0",
    description="A simple database management system for ICT training courses.",
    author="Gen Fernandez",
    author_email="genrevepfernandez@gmail.com",
    packages=find_packages(),
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            'dbms-app=dbms.main:main_menu',
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
