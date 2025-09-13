# 请求参数

## 参数表

| 参数名  |       类型       |        默认值        |          说明          |
| :-----: | :--------------: | :------------------: | :--------------------: |
|   num   |       int        |          1           |       图片的数量       |
|   tag   |      string      |         null         | 图片tags所包含的关键字 |
|  proxy  |      string      | `https://i.pixiv.re` | 图片链接使用的反代地址 |
|   db    |      string      |     `data.json`      |  使用的图库（数据库）  |
|   uid   | string(自动转换) |         null         |     需要查询的UID      |
| keyword |      string      |         null         |      查询的关键字      |

## 补充说明

### num

一个属于1~20的整数，只能在`/json`中调用，如果超出返回则返回空数组`[]`。

### tag

可以进行tag查询，目前只支持单个Tag的查询哦！

比如这样子，可以请求到一张tag有`genshin`的图片：

```
https://suzumi.hikai.top/direct?tags=genshin
```

还可以使用`|`进行分割，这个符号代表`或者`，即假设我访问`http://127.0.0.1:4500/?r18=1&tag=genshin|arknights`，那么查询的就是Arknights的或者Genshin的图片√，很好理解吧

### proxy

代理地址，允许自己进行修改，只要是pixiv的代理地址就可以√

> 注意
> 
> proxy必须包含前面的https，否则报错！

使用方法差不多，还是用查询参数修改：

```
https://suzumi.hikai.top/direct?proxy=https://www.proxy.top
```

### db

使用的数据库的名称，具体请询问管理员！

### uid

根据`uid`进行查找，会扫描用户的uid进行返回，填入的数据（数字）会自动转换为字符串

### keyword

就是一个关键字查找，自动扫描用户名和Tags进行查找，存在的话就进入筛选部分，然后正常按照需求返回