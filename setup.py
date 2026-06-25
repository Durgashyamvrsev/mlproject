from setup import setup, find_packages




setup(
    name='mlproject',
    version='0.1.0',
    author='syam',
    author_email='durgashyam88@gmail.com',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
        'scikit-learn',
        'matplotlib',
        'seaborn',]
)