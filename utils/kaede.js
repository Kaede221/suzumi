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

// 获取一个随机的链接
function getRandLink(jsonData, proxy, r18, tag) {
    // 创建空列表，用来储存获取的所有链接
    let urlList = []

    // 判断r18和tags，进行筛选，获得链接
    jsonData.forEach(element => {
        if ((element['r18'] == r18) || r18 == 3 && tag || element['tags'].includes(tag)) {
            // 直接加入列表就好
            urlList.push(element['url'])
        }
    });
    // 根据列表长短，获取一个随机的链接
    return useProxy(proxy, urlList[getRandomInt(0, urlList.length)])
}

// 获取随机的JSON文件
function getRandJson(jsonData, r18, tag, num) {
    // 首先判断num的范围是否成立
    if (num < 1 || num > 10) {
        // 如果超出范围，那么返回空数组
        return []
    }
    // 创建空列表，用来储存数据
    let objectList = []

    // 先进行筛选
    jsonData.forEach(element => {
        if ((element['r18'] == r18) || r18 == 3 && tag || element['tags'].includes(tag)) {
            // 直接加入列表就好
            objectList.push(element)
        }
    })
    // 筛选后，直接随机num个对象加入就好
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