from distutils.core import setup

setup(
    name='CProfileV',
    version='0.0.8',
    url='https://github.com/ymichael/cprofilev',
    author='Michael Yong',
    author_email='wrong92@gmail.com',
    install_requires=["bottle"],
    entry_points={
        'console_scripts': [
            'cprofilev = cprofilev:main',
        ]
    },
    license='MIT',
    description='Thin wrapper for viewing python cProfile output',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Environment :: Web Environment',
        'Framework :: Bottle',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Topic :: Software Development :: Testing',
    ]
)
