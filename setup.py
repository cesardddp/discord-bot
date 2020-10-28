from setuptools import setup ,find_packages

def get_requeires_file(filename:str)->list:
    with open(filename,'r') as file:
        lista = [req.strip() for req in file if req.strip()]
    return lista


setup(
    name='discord-bot',
    version='0.1.0',
    description='',
    url='',
    author=['@cesardddp','Leonardo Bezerra'],
    author_email=['cesardddp@hotmail.com','leonardo@não_sei'],
    license='',
    packages=find_packages(
        exclude='./.venv',
        where='app'),
    include_package_data=True,
    install_requires=get_requeires_file("requeriments.txt"),
    extras_require={
        'dev':  get_requeires_file("requeriments-dev.txt")
    }
)