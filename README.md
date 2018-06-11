# Connected在线UM


## 当前使用的项目
- MW41
- CPE(HH70/HH41/HH40/MW70)项目

## 在线访问地址

url前缀http://www.alcatel-move.com/um/

例子:http://www.alcatel-move.com/um/MW41/00_generic/USER_Manual_fr.pdf


- `www.alcatel-move.com`和`www.tcl-move.com`指向一致

- CPE的在线路径规则:
  - `http://www.alcatel-move.com/um/url.html?project=项目名&custom=定制ID&lang=语言ID&version=版本号`
  - `http://www.alcatel-move.com/um/url.html?project=HH70&custom=IA&lang=en&version=HH70_IA_02.00_10`

## 使用方法：
- 运行auto.sh
- 提交到git
- 生产环境服务器拉取git代码


## 维护
- 线上服务器：
  - 服务器维护为`服务器组`
  - 服务器地址：`58.251.35.66`
  - 服务器环境代码路径:`/data/www/um/`