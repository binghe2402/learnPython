# 根据扩展名删除广告文件，但是这样容易误伤视频，下次可以考虑根据大小

import pathlib
import shutil
p = pathlib.Path('E:\\新建文件夹\\新建文件夹')
temp_p = p/'temp'
NN = 0
if not (temp_p).exists():
    pathlib.Path(temp_p.mkdir())
for path in p.glob('**/*'):
    if path.is_file() and not path.match('*.jpg'):
        if (temp_p/path.name).exists():
            path = path.rename(pathlib.Path(path.name+str(NN := NN + 1)))
        shutil.move(str(path), str(temp_p))
