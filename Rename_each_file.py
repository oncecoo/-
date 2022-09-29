import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--file_path',default='./images')
parser.add_argument('--label_path',default='./labels')
parser.add_argument('--file_new_path',default='./src/images')
parser.add_argument('--label_new_path',default='./src/labels')



args = parser.parse_args()


class FileRename:
    def __init__(self,args):
        self.file_path = args.file_path
        self.label_path = args.label_path
        self.new_file_path = args.file_new_path
        self.new_label_path = args.label_new_path
        self.file_path_list = os.listdir(self.file_path)
        self.label_path_list = os.listdir(self.label_path)

        if not os.path.exists(self.new_file_path):
            os.makedirs(self.new_file_path)
        if not os.path.exists(self.new_label_path):
            os.makedirs(self.new_label_path)

    def _compare_file(self):

        file_count = 0
        files = []
        for file in self.file_path_list:
            name,_ = file.rsplit('.',1)
            files.append(name)
            file_count += 1
        print('file num is {}'.format(file_count))

        return files

    def _rename(self,old_path,file,index,suffix,new_path):
        import shutil
        shutil.copyfile(os.path.join(old_path,file+'.'+suffix),os.path.join(new_path,str(index)+"."+suffix))

    def run(self):
        files = self._compare_file()


        for index,file in enumerate(files):
            # print(file)
            self._rename(self.file_path,file,index,'jpg',self.new_file_path)
            self._rename(self.label_path,file,index,'txt',self.new_label_path)




filerename = FileRename(args)
filerename.run()



