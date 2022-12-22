import platform

if __name__ == '__main__':

    print(f'Machine: {platform.machine()}')
    print(f'Version: {platform.version()}')
    print(f'Uname: {platform.uname()}')
    print(f'Platform: {platform.platform()}')
    print(f'Release: {platform.release()}')
    print(f'System: {platform.system()}')
    print(f'Processor: {platform.processor()}')
