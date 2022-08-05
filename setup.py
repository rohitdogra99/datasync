from setuptools import find_packages, setup

import os
import shutil


OUTPUT_DIR = 'target'

if __name__ == "__main__":
    setup(name='datasync',
          version='1.0.0',
          description='datasync framework to aggregate the features',
          author='Rohit Kumar',
          author_email='rohitdogra99@gmail.com',
          license='Open',
          packages=find_packages(), # This line will make dirs with __init__.py as python packages.
          package_data={'resources' : ['*.yaml'], '':['*.yaml']}, # to export all yaml files wile packaging.
          # include_package_data=True,
          zip_safe=False)


    egg_name = os.listdir('dist')[0]

    os.rename(
        os.path.join('dist', egg_name),
        os.path.join(OUTPUT_DIR, egg_name)
    )

    shutil.rmtree('build')
    shutil.rmtree('dist')
    shutil.rmtree('datasync.egg-info')
