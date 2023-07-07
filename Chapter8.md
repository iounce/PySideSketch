# 第八章 案例解析之PySideFrameless

PySideFrameless主要使用了PySide6窗体的Qt.FramelessWindowHint属性来实现无边框的效果，同时自定义了标题栏，如图标，最大化，最小化，关闭按钮，以及自定义菜单等。

除此之外，还增加了多主题，多语言的支持，只需增加业务功能即可实现相对完善的无边框应用程序。

## 主窗体解析

主要涉及以下文件：
ui_main.ui
ui_main.py
main_window.py

* ui_main.ui：
  主窗体的UI界面，可以使用【Qt *designer*】打开编辑，主要包括QGridLayout，QHBoxLayout，QVBoxLayout等布局的使用，合理拆分界面，保证界面伸缩而控件相对大小不变；
* ui_main.py：
  使用*pyside6-uic ui_main.ui > ui_main.py*命令编译生成，将UI文件转换为对应的Python文件；
* main_window.py：
  主窗体文件，使用了ui_main.py，同时添加了业务逻辑：
  * init_window()函数：通过属性Qt.FramelessWindowHint，设置窗体为无边框模式；
  * init_app_bar()函数：主要设置标题栏，自定义图标，包括最大化/最小化/还原等，还有logo，标题等；主要使用QPushButton控件，设置为扁平模式，并增加图标；图标来自于开源库qtawesome，推荐使用，非常方便；
  * init_more_menu()函数：主要用于添加下拉菜单，包括语言切换，主题，关于等；主要使用QMenu，QAction等控件。
  * init_language()函数：主要用于设置默认语言；
  * update_dynamic_widgets()函数：主要用于切换语言时手动更新控件标题；
  * proc_theme_signal()函数：主要用于获取语言窗体发送的信号，用于保存当前使用的语言；
  * get_cursor_direction()函数：主要用于获取鼠标移动的方向，便于拖动操作；
  * mousePressEvent()函数：鼠标按下的事件响应，用于获取鼠标的坐标值；
  * mouseMoveEvent()函数：鼠标移动的事件响应，用于设置窗体位置；
  * mouseReleaseEvent()函数：鼠标释放的事件响应，用于释放鼠标状态。

## 多主题解析

主要涉及以下文件：

* ui_theme.ui：
  主窗体的UI界面，主要设计窗体布局；
* ui_theme.py：
  使用*pyside6-uic ui_theme.ui > ui_theme.py*命令编译生成，将UI文件转换为对应的Python文件；
* theme_window.py：
  主窗体文件，使用了ui_theme.py，同时添加了业务逻辑：
  * init_window()函数：通过属性Qt.FramelessWindowHint，设置窗体为无边框模式；
  * init_menu()函数：主要用于设置关闭窗体按钮及其响应；
  * init_themes()函数：主要用于添加可用的主题风格，通过分组布局来实现多行多列展示。

## 多语言解析

主要涉及以下文件：

* zh_CN.ts：
  中文翻译源文件，可以使用文本编辑器打开编辑，其中不同窗体的翻译需要在不同的 `<context></context>`之间编辑，只能在指定窗体中使用；
* zh_CN.qm
  使用语言工具【Qt *Linguist*】打开zh_CN.ts发布后生成；
* en_US.ts：
  英文翻译源文件，是zh_CN.ts的英文翻译，格式相同；
* en_US.qm：
  使用语言工具【Qt *Linguist*】打开en_US.ts发布后生成。

## 基类解析

主要涉及以下文件：

* base_window.py：
  基本可以取代主窗体使用的ui_main.py文件的功能，无.ui文件的依赖；直接通过代码实现布局，所以也无法使用编辑器编辑界面：
  * init_layout()函数：通过QGridLayout，QHBoxLayout，QVBoxLayout等布局，分割界面，设计标题栏(head)，主体(body)，状态栏(tail)等功能模块；
  * init_app_bar()函数：主要用于设置标题栏，自定义图标，包括最大化/最小化/还原等，还有logo，标题等；
  * init_window()函数：通过属性Qt.FramelessWindowHint，设置窗体为无边框模式。
* base_window_demo.py：
  使用base_window.py的示例程序。

<font size=2>
说明：</br>
designer.exe工具可在Python安装目录找到，参考路径：</br>
D:\Python\Python310\Lib\site-packages\PySide6\designer.exe</br></br>
linguist.exe工具可在Python安装目录找到，参考路径：</br>
D:\Python\Python310\Lib\site-packages\PySide6\linguist.exe</br></br>
pyside6-uic.exe工具可在Python安装目录找到，参考路径：</br>
D:\Python\Python310\Scripts\pyside6-uic.exe</br>
</font>
