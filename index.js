const config = require('config-yml')
const express = require('express')
const app = express()
const kaede = require('./utils/kaede')

// 读取文件，在这里读取，就可以只用读取一次了，方便一点
const jsonData = require(`./data/${config.app.db}`)

// 直接查看访问的参数就好
app.get('/direct', (req, res) => {
    const query = req.query
    const r18 = query.r18 || config.app.r18
    const proxy = query.proxy || config.app.proxy
    const tag = query.tag || true
    res.redirect(kaede.getRandLink(jsonData, proxy, r18, tag))
})

// JSON情况
app.get('/json', (req, res) => {
    const query = req.query
    const r18 = query.r18 || config.app.r18
    const tag = query.tag || true
    const num = query.num || config.app.num
    res.json(kaede.getRandJson(jsonData, r18, tag, num))
})

// 以及直接访问 给两个方案就好
app.all('/', (req, res) => {
    // 正常获取需要的参数
    const query = req.query
    const r18 = query.r18 || config.app.r18
    const proxy = query.proxy || config.app.proxy
    const tag = query.tag || true
    const num = query.num || config.app.num

    // 根据具体情况进行判断
    if (req.method == "GET") {
        res.redirect(kaede.getRandLink(jsonData, proxy, r18, tag))
    } else if (req.method == "POST") {
        res.json(kaede.getRandJson(jsonData, r18, tag, num))
    }
})

app.listen(config.app.port, () => {
    console.log(`服务启动成功，端口：${config.app.port}`);
})