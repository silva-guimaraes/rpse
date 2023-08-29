from setuptools import setup

setup(
        name='rpse',
        install_requires=['pysubs2', 'argparse', 'pathlib'],
        packages=['rpse'],
        entry_points={
            'console_scripts': [
                'rpse=rpse.rpse:main',
                ],
            }
        )
