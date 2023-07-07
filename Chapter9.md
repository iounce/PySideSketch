# 第九章 案例解析之PySidePDF

PySidePDF是使用PySideFrameless作为骨架来搭建的，实现PDF与Word之间相互转换的应用程序。PySidePDF继承了PySideFrameless无边框窗体的效果，包括多主题，多语言的功能，支持多文件同时转换。

# 主窗体解析

主要涉及以下文件：
* ui_main.ui：
  主窗体的UI界面，可以使用【Qt *designer*】打开编辑，主要包括QGridLayout，QHBoxLayout，QVBoxLayout等布局的使用，增加了QTableWidget控件的使用；
* ui_main.py：
  使用*pyside6-uic ui_main.ui > ui_main.py*命令编译生成，将UI文件转换为对应的Python文件；
* main_window.py：
  主窗体文件，使用了ui_main.py，同时添加了业务逻辑；手动选择要转换的多个文件，然后通过启动线程来执行转换过程，转换过程中接收线程信号来更新列表状态：
  * init_tab_menu()函数：初始化转换功能菜单，如PDF转Word；
  * add_table_row()函数：在列表中增加行，用于增加要转换的文件；
  * update_action_column()函数：更新列表动作列；
  * update_status_column()函数：更新列表状态列；
  * thread_convert()函数：线程函数，用于多文件转换操作；
  * on_convert()函数：响应函数，启动线程执行转换操作；
  * proc_convert_signal()函数：处理转换信号。

# 线程类解析

主要涉及以下文件：
* thread.py:
通过线程来实现不同文件的转换操作，加快多文件转换速度：
  * start()函数：发送任务开始信号；
  * convert()函数：实现转换逻辑，并发送转换信号；
  * add()函数：添加转换任务，通过线程执行转换；
  * wait()函数：等待线程结束，并发送结束信号

# 转换类解析

主要涉及以下文件：
* converter.py：
定义不同的转换发送，如PDF转Word等：
  * do_pdf2word()函数：实现PDF转Word；
  * do_word2pdf()函数：实现Word转PDF。

<font size=2>
说明：</br>
designer.exe工具可在Python安装目录找到，参考路径：</br>
D:\Python\Python310\Lib\site-packages\PySide6\designer.exe</br></br>
pyside6-uic.exe工具可在Python安装目录找到，参考路径：</br>
D:\Python\Python310\Scripts\pyside6-uic.exe</br>
</font>
