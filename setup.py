import setuptools

setuptools.setup(
    name="jupyter-kroki-magic",
    version='0.1.0',
    url='https://github.com/sunhwan/jupyter-kroki-magic',
    author="Sunhwan Jo",
    author_email='sunhwanj@gmail.com',
    description="A Jupyter Notebook %%magic for drawing diagram using kroki.io",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    license='MIT',
    install_requires=[
        'jupyter',
        'ipywidgets',
    ],
    keywords=['ipython', 'jupyter'],
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
    ]
)
