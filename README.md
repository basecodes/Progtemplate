# Progtemplate
### Python实现的可编程模板，类似于html里的javascript动态生成html。以数据导入模板形式生成模型。

## 用途
---
1. 可用于配置文件映射类生成
2. 可用于类自动化生成(比如：协议生成)

## 介绍
---
- Data文件夹：存放模板需要的数据文件，文件名和对应模板文件名必须一致。数据配置文件格式支持(xml,json,yaml,csv)。
- template文件夹：存放模板，模板以.template后缀。
- publish文件夹：存放模型。
- execute.py：构建模型，准备好模板和数据后，执行当前文件，生成模板对应模型

>模板主体：
```template
{{start file}}
...
{{end cpp}}
```
上面主体是每个模板都必须有的，解析模板时只会解析两个标签间内容。之外的内容将忽略。file字段代表文件对象(使用参见用法)，cpp字段是生成模型后文件的后缀名。

>模板简单替换：
```
{{= file.obj.name}}
```
当前位置会用file文件里的obj对象name字段文本替换

>模板编程替换：
```
{{writeln(file.obj.name + file.obj.description)}}
```
执行当前替换之前，会先执行writeln语句，writeln方法会写入一行，类似于println打印语句，会把当前位置替换成写入的内容。编程替换需要懂一点python基本语法。

## 用法
1. 编写模板：
```
{{start file}}
public class  {{=file.class.name}}{

}
{{end cs}}
```

2. 编写数据以json为例：
```json
{
    "class": {
        "name": "Test"
    }
}
```

3. 生成模型，执行execute.py文件。

## 环境
Python 3.4
