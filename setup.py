from setuptools import setup

setup(
    name='autoprep',
    version='0.1.0',
    description='Automated CSV Clinical Data Preprocessing',
    author='Mohammadreza Saraei',
    author_email='mrsaraei3@gmail.com',
    url='https://github.com/mrsaraei/autoprep',
    packages=['autoprep'],
    install_requires=['numpy', 'pandas', 'matplotlib', 'scikit-learn'],
    license='MIT License',
)
