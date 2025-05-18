# 系统大管家，负责文件目录管理、环境变量操作等基础系统任务
import os
# 文件搬运专家，专门处理高级的文件和目录复制、移动操作
# 全称 shell utilities，shell 就像是人与计算机之间的翻译官和传声筒
import shutil
# 脚本运行的记录员，记录脚本运行过程中的各种信息
import logging

#1. 把日志文件app.log移到脚本的同一目录下
file_dir=os.path.dirname(os.path.abspath(__file__))
log_path=os.path.join(file_dir,'app.log')

# 2. 配置日志
logging.basicConfig(
    # 1.1 设置日志级别为 INFO，日志级别从低到高依次为 DEBUG、INFO、WARNING、ERROR、CRITICAL。只有 INFO以上级别的日志消息会被记录，
    level=logging.INFO,
    # 1.2 设置日志输出格式，
    # s 表示字符串占位符。%(asctime)s：日志记录的时间，会自动替换为实际记录时间
    # %(levelname)s：日志的级别，如 INFO、WARNING 等
    # %(message)s：具体的日志内容，即调用 logging 方法时传入的消息
    format='%(asctime)s - %(levelname)s - %(message)s',
    # 1.3 日志文件名/路径
    filename=log_path,
    # 日志内容编码格式
    encoding='utf-8'
)

# 3. 记录日志
logging.info('这是一条信息日志')


#4. 定义桌面文件整理函数
def organize_files(desk_path):
    # 4.1 将文件类型及其对应的文件扩展名装进字典types
    types = {
    # 办公文档类
    'Excel': ('.xlsx', '.xls', '.xlsm', '.xlsb', '.xltx', '.xltm'),
    'Word': ('.docx', '.doc', '.docm', '.dotx', '.dotm'),
    'PowerPoint': ('.pptx', '.ppt', '.pptm', '.potx', '.potm', '.ppsx', '.ppsm'),
    'PDF': ('.pdf',),
    # 多媒体类
    'Image': ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.tif', '.webp', '.ico'),
    'Video': ('.mp4', '.avi', '.mov', '.mkv', '.flv', '.wmv', '.mpeg', '.mpg'),
    'Audio': ('.mp3', '.wav', '.ogg', '.flac', '.aac', '.wma'),
    # 文本类
    'Text': ('.txt', '.md', '.rtf', '.log'),
    # 编程类
    'Python': ('.py', '.pyc', '.pyw', '.pyd'),
    'JavaScript': ('.js', '.jsx', '.mjs'),
    'CSS': ('.css', '.scss', '.sass'),
    'HTML': ('.html', '.htm'),
    'XML': ('.xml', '.xsd', '.xslt'),
    # 压缩类
    'Zip': ('.zip', '.rar', '.7z', '.tar', '.gz', '.bz2')
}
    

    # 4.2 遍历桌面目录下的文件、文件夹
    for file in sorted(os.listdir(desk_path)):
        # 获取文件的完整路径
        file_path = os.path.join(desk_path, file)
        # 判断是否为文件
        if os.path.isfile(file_path):
            # 遍历文件类型和对应的扩展名
            for file_type, exts in types.items():
                # 判断文件是否以指定扩展名结尾
                if file.endswith(exts):
                    # 生成用于存储同类文件的目标文件夹路径
                    target = os.path.join(desk_path, file_type)
                    try:
                        # 创建目标文件夹，若已存在则不报错
                        os.makedirs(target, exist_ok=True)
                        # 移动文件到目标文件夹下
                        shutil.move(file_path, os.path.join(target, file))
                        # 记录文件移动成功的日志
                        logging.info(f'移动{file} 至 {file_type} 文件夹。')
                        # 找到了当前文件的类型得以整理进文件夹，跳出循环
                        break
                    except Exception as e:
                        # 记录文件移动失败的日志。{e}是异常类型的占位符
                        logging.error(f'将 {file} 移动至 {file_type}时出错: {e}')

# 5. 获取用户输入的要整理的桌面目录
# 5.1 为了该模块导入到其他脚本里时不自动执行，只在模块直接运行时执行
if __name__ == "__main__":
    # 5.2 获取用户输入的文件夹路径
    path = input('请输入要整理的文件夹路径: ')
    # 5.3 判断路径是否存在
    if os.path.exists(path):
        # 5.4 调用桌面文件整理函数
        organize_files(path)
        print('文件整理完成，详细信息请查看 app.log 文件。')
    else:
        print('你输入的路径不存在，请检查后重新运行。')