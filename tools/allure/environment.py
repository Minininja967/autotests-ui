from config import settings
import platform
import sys


def create_allure_environment_file():
    items = [f'{key}={value}' for key, value in settings.model_dump().items()]
    properties = '\n'.join(items)
    os_info = f'os_info={platform.system()}, {platform.release()}'
    python_version = f'python_version={sys.version}'

    with open(settings.allure_results_dir.joinpath('environment.properties'), 'w+') as file:
        file.write(properties + '\n')
        file.write(os_info + '\n')
        file.write(python_version + '\n')
