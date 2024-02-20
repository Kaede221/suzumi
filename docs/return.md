# 返回格式

## 302跳转

直接重定向，加载一张图片出来。

如果图片无效，或者根据查询参数啥都没有，那么会返回一个404页面！

```
https://i.jitsu.top/img-original/img/2018/12/21/00/11/28/72203964_p0.jpg
```

## JSON

会返回下面这样格式的JSON数据（下面一个花括号，也叫做一个KData，你可能会在源代码中看到这个名词）

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