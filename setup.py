from setuptools import setup

setup(
    name='DSFacebookStalker',
    version='0.0.0.1',
    description='Stalker your friends friendships',
    url='https://github.com/DiSiqueira/DSFacebookStalker',
    author='Diego Siqueira',
    author_email='dieg0@live.com',
    license='MIT',
    package_dir={'DSFacebookStalker': 'src'},
    packages=['DSFacebookStalker'],
    zip_safe=False,
    keywords=['Facebook', 'Stalker', 'API', 'Graph', 'Friends', 'Friendship'],
    entry_points=
    {
        'console_scripts':
            [
                'dsdownload = DSFacebookStalker:main',
            ],
    },
    install_requires=['facebook'],
    requires=['facebook', 'requests']
)
