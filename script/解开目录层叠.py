import pathlib
import shutil


def checkdir(path: pathlib.WindowsPath):
    # 下层有目录则返回True，无目录返回False
    return bool([p for p in path.iterdir() if p.is_dir()])


path = pathlib.Path('E:\\新建文件夹\\新建文件夹').resolve()
new_path = pathlib.Path(
    'E:\\新建文件夹\\Coser小丁 Fanctasy Fanctory 25套圖合集[1192P10V18.2G]').resolve()


def refold_dir(path: pathlib.WindowsPath, newer_path: pathlib.WindowsPath):
    for p in path.iterdir():
        if p.is_dir():
            refold_dir(p, newer_path)
        else:

            if not checkdir(p):  # 下层无目录，则为最底层目录，移动
                shutil.move(p, newer_path)
            return
