# Suzumi-API

一个简单易用的随机图片API！

下载源代码后，先`npm install`，随后`npm run serve`即可启动服务！

启动前建议修改config文件！

> 为了更加方便使用，我将文档直接写在这个地方，方便修改，查阅。
>
> 下方的Url中，host和Port均为默认配置，如果你在本地进行部署，理论上可以直接打开

# 请求地址

## 302跳转

```
https://127.0.0.1:4500/direct
```

## JSON

```
https://127.0.0.1:4500/json
```

## 通用

```
https://127.0.0.1:4500/
```

# 请求方法

## URL路径

### `/direct`

> 注意
> 
> 仅支持GET请求，POST请求无效

### `/json`

> 提示
> 
> 仅支持GET请求，POST请求无效

### `/`

> 提示
> 
> PST和GET都可以访问，根据不同访问方式返回内容

- `GET`: 302重定向到图片
- `POST`: 返回随机JSON

# 请求参数

## 参数表

| 参数名 |  类型  |        默认值        |          说明          |
| :----: | :----: | :------------------: | :--------------------: |
|  num   |  int   |          1           |       图片的数量       |
|  r18   |  int   |          0           |    年龄分级（0，1）    |
|  tag   | string |         null         | 图片tags所包含的关键字 |
| proxy  | string | `https://i.pixiv.re` | 图片链接使用的反代地址 |
|   db   | string |     `data.json`      |  使用的图库（数据库）  |

## 补充说明

### num

一个属于1~20的整数，只能在`/json`中调用，如果超出返回则返回空数组`[]`。

### r18

用来判断是否显示R18内容：

```json
{
    0: "不显示",
    1: "显示",
    2: "随机"
}
```

### tag

可以进行tag查询，目前只支持单个Tag的查询哦！

比如这样子，可以请求到一张tag有`genshin`的图片：

```
https://suzumi.hikai.top/direct?tags=genshin
```

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

# 返回格式

## 302跳转

直接重定向，加载一张图片出来。

如果图片无效，那么会返回一个404页面！

```
https://i.jitsu.top/img-original/img/2018/12/21/00/11/28/72203964_p0.jpg
```

## JSON

会返回下面这样格式的JSON数据

```json
[
    {
        "pid": 110315846,
        "p": 8,
        "uid": "78823052",
        "title": "artoria pendragon",
        "author": "Emmanuel costa",
        "r18": 0,
        "width": 512,
        "height": 768,
        "tags": [
            "Fate/staynight",
            "アルトリア・ペンドラゴン",
            "Fate/GrandOrder",
            "女の子",
            "オリジナル",
            "水着",
            "Beach"
        ],
        "url": "https://i.pximg.net/img-original/img/2023/07/28/20/50/03/110315846_p0.png",
        "urls": {
            "thumb_mini": "https://i.pximg.net/c/128x128/img-master/img/2023/07/28/20/50/03/110315846_p0_square1200.jpg",
            "small": "https://i.pximg.net/c/540x540_70/img-master/img/2023/07/28/20/50/03/110315846_p0_master1200.jpg",
            "regular": "https://i.pximg.net/img-master/img/2023/07/28/20/50/03/110315846_p0_master1200.jpg",
            "original": "https://i.pximg.net/img-original/img/2023/07/28/20/50/03/110315846_p0.png"
        }
    }
]
```