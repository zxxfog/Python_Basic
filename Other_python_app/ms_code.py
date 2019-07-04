# -*- coding:utf-8 -*-
#!/usr/bin/env python

# 2019年7月3日
# 将用户输入的短信息转换为摩斯密码，只能输入英文和数字，单词之间以空格分隔

import Tkinter

# 摩斯密码表
CODEC_DICT = {"0":"-----","1":".----","2":"..---","3":"...--","4":"....-","5":".....","6":"-....","7":"--...","8":"---..","9":"----.",
"A":".-","B":"-...","C":"-.-.","D":"-..","E":".","F":"..-.","G":"--.","H":"....","I":"..","J":".---","K":"-.-","L":".-..","M":"--",
"N":"-.","O":"---","P":".--.","Q":"--.-","R":".-.","S":"...","T":"-","U":"..-","V":"...-","W":".--","X":"-..-","Y":"-.--","Z":"--."}

class MorseCode(object):
    def __init__(self):
        # 创建主窗口,用于容纳其它组件
        self.root = Tkinter.Tk()
        # 给主窗口设置标题内容
        self.root.title("摩斯密码生成器")
        # 创建一个输入框,并设置尺寸
        self.code_input = Tkinter.Entry(self.root,width=36)
        # 创建一个回显列表
        self.display_info = Tkinter.Listbox(self.root, width=50)
        # 创建一个查询结果的按钮
        self.result_button = Tkinter.Button(self.root, command = self.find_position, text = "生成摩斯码")

    # 完成布局
    def gui_arrang(self):
        self.code_input.pack()
        self.display_info.pack()
        self.result_button.pack()

    # 根据输入生成密码 
    def find_position(self):
        the_code_info = []
        # 获取输入信息
        self.code_info_str = self.code_input.get()
        # 根据空格将输入分个成单词
        self.code_info_list = self.code_info_str.split()
        try:
            for item_str in self.code_info_list:
                the_code_info_tmp = []
                # 遍历单词里边的每个字符
                for every_char in item_str.upper():
                    # 对字符转码
                    if (CODEC_DICT.has_key(every_char)):
                        the_code_info_tmp.append(CODEC_DICT[every_char])
                        the_code_info_tmp.append("   ")
                    else:
                        pass
                # 完成一个单词的转码
                the_code_info_tmp_t = "".join(the_code_info_tmp)
                the_code_info.append(the_code_info_tmp_t)
        except:
            pass
        
        # 清空listbox的所有项
        self.display_info.delete(0,Tkinter.END)

        # 为回显列表赋值
        for item in the_code_info:
            self.display_info.insert(Tkinter.END,item)


def main():
    # 初始化对象
    FL = MorseCode()
    # 进行布局
    FL.gui_arrang()
    # 主程序执行
    Tkinter.mainloop()
    pass


if __name__ == "__main__":
    main()
    