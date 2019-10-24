from setuptools import setup

setup(name='SQLBackupToGoogleDrive',
      version='0.1',
      description='',
      url='http://github.com/nicholasceliano/sqlbackuptogoogledrive',
      author='Nick',
      author_email='nicholasceliano@gmail.com',
      license='MIT',
      packages=['sqlbackuptogoogledrive', 'sqlbackuptogoogledrive.services', 'sqlbackuptogoogledrive.models'],
      package_data={'sqlbackuptogoogledrive': ['config.json', 'client_secrets.json', 'GoogleDriveCreds.txt']},
      install_requires=[
          'PyDrive',
      ],
      entry_points={"console_scripts": ["gnucashBackup=sqlbackuptogoogledrive.app:main"]},
      zip_safe=False)