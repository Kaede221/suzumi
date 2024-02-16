// 在这里实现一些工具方法
const url = require('url')

// 修改代理地址
// 这里的proxy需要https前缀
function useProxy(proxy, url_target) {
    // 直接返回需要的内容即可
    return url.resolve(proxy, url.parse(url_target, true).path)
}

// 随机数函数
function getRandomInt(min, max) {
    const minCeiled = Math.ceil(min);
    const maxFloored = Math.floor(max);
    return Math.floor(Math.random() * (maxFloored - minCeiled) + minCeiled); // 不包含最大值，包含最小值
}

// 根据数组，判断是否有交集 有就是true，没有就是false
function haveIntersection(arr1, arr2) {
    let set1 = new Set(arr1);
    return arr2.some(value => set1.has(value));
}

// 写一个筛选器出来
// 传入一个K-Data，根据规则进行筛选，返回视情况而定
// 默认参数
// - r18 int 是否为R18内容，默认使用0，防止传入错误参数
// - tag string 是否有Tag，如果没有的话默认就是null，否则就是一个内容
// - uid string 根据具体作者进行筛选
// - keyword string 可以查找作品名称中以及tags中的关键字
function dataFilter(kData, r18 = 0, tag = null, uid = null, keyword = null) {
    if (kData['r18'] == r18) {
        if (tag == null || haveIntersection(kData['tags'], tag.split("|"))) {
            if (uid == null || parseInt(kData['uid']) == uid) {
                if (keyword == null || kData['tags'].includes(keyword) || kData['title'].includes(keyword)) {
                    return kData
                }
            }
        }
    }
    return false
}

// 获取一个随机的链接
function getRandLink(jsonData, proxy, r18, tag, uid, keyword) {
    // 创建空列表，用来储存获取的所有链接
    let urlList = []

    // 判断r18和tags，进行筛选，获得链接
    jsonData.forEach(element => {
        if (dataFilter(element, r18, tag, uid, keyword)) {
            // 直接加入列表就好
            urlList.push(element['url'])
        }
    });
    // 这里判断一下，是否有链接，如果没有，就是一个空列表，那么返回一个404页面就好
    if (urlList.length == 0) {
        return '404.html'
    }
    // 根据列表长短，获取一个随机的链接
    return useProxy(proxy, urlList[getRandomInt(0, urlList.length)])
}

// 获取随机的JSON文件
function getRandJson(jsonData, r18, tag, num, uid, keyword) {
    // 首先判断num的范围是否成立
    if (!(num >= 1 && num <= 20)) {
        // 如果超出范围，那么返回空数组
        return []
    }
    // 创建空列表，用来储存数据
    let objectList = []

    // 先进行筛选
    jsonData.forEach(element => {
        if (dataFilter(element, r18, tag, uid, keyword)) {
            // 直接加入列表就好
            objectList.push(element)
        }
    })
    let finalList = []
    let l = objectList.length
    for (let i = 0; i < num; i++) {
        finalList.push(objectList[getRandomInt(0, l)])
    }
    // 直接返回就好
    return finalList
}

module.exports = {
    getRandLink,
    getRandJson
}