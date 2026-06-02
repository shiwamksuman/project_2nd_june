from setuptools import setup, find_packages
setup(
    name = 'error_handling',
    version = '1.0',
    packages = (
      find_packages(include = ('error_handling*', ))
      + ['prophecy_config_instances', 'prophecy_config_instances.error_handling']
    ),
    package_dir = {'prophecy_config_instances' : 'configs/resources'},
    package_data = {'prophecy_config_instances.error_handling' : ['*.json', '*.py', '*.conf']},
    description = 'workflow',
    install_requires = [
'prophecy-libs==2.1.17'],
    entry_points = {
'console_scripts' : [
'main = error_handling.pipeline:main'], },
    data_files = [(".prophecy", [".prophecy/workflow.latest.json"])],
    extras_require = {
'test' : ['pytest', 'pytest-html', 'pytest-cov'], }
)
