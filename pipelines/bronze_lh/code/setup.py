from setuptools import setup, find_packages
setup(
    name = 'bronze_lh',
    version = '1.0',
    packages = find_packages(include = ('bronze_lh*', )) + ['prophecy_config_instances', 'prophecy_config_instances.bronze_lh'],
    package_dir = {'prophecy_config_instances' : 'configs/resources'},
    package_data = {'prophecy_config_instances.bronze_lh' : ['*.json', '*.py', '*.conf']},
    description = 'workflow',
    install_requires = [
'prophecy-libs==2.1.17'],
    entry_points = {
'console_scripts' : [
'main = bronze_lh.pipeline:main'], },
    data_files = [(".prophecy", [".prophecy/workflow.latest.json"])],
    extras_require = {
'test' : ['pytest', 'pytest-html', 'pytest-cov'], }
)
