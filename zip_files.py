import os
import re
import zipfile

#zip_dir = 'C:\\Users\\weizhou\\PycharmProjects\\test\\1'

zip_dir = input('请输入需要压缩的文件路径，源文件将会被删除：')
#list = os.listdir(zip_dir)
for root, dirs, files in os.walk(zip_dir, topdown=True):
    for name in files:
        if(re.search('.isf',name)):
            file_name_full = os.path.join(root, name)
            # Split with \
            ret = re.split(r'\\', file_name_full)
            # Last element is file name
            file_name_short = ret[-1]
            # Remoing ".isf", saving to file_name_tmp
            file_name_tmp = file_name_full[: -4]
            print('zipping:'+file_name_full)
            zip = zipfile.ZipFile(file_name_tmp+'.zip','w',zipfile.zlib.DEFLATED)
            zip.write(file_name_full, file_name_short, zipfile.ZIP_DEFLATED)
            zip.close
            os.remove(file_name_full)
            print(file_name_full+' Removed!')
print('All files are Finished!!')
