import setuptools

setuptools.setup(
    name='audio-speech-to-sign-language-converter',
    version='0.1.0',
    description='Python project',
    author='Tejashwini Poshamoni',
    author_email='tejashwiniposhamoni@gmail.com',
    url='https://github.com/Tejashwini7174/audio-to-sign-language-translator',
    packages=setuptools.find_packages(),
    setup_requires=['nltk', 'joblib','click','regex','sqlparse','setuptools'],
)
