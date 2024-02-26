var http = require('http');
var fs = require('fs');
var url = require('url');

http.createServer(function (req,res){
    var exp = /^\/c\d+$/
    console.log(req.method + ' ' + req.url)
    var q = url.parse(req.url, true)
    console.log(q.pathname)
    if(exp.test(q.pathname)){
        var path = 'mapa_site' + q.pathname + '.html'
        console.log(path)
        fs.readFile(path, function(erro, data){
            if(erro){
                res.writeHead(404, {'Content-Type': 'text/html; charset=utf-8'})
                res.write('<p>O URL ' + q.pathname + ' pedido não foi encontrado neste servidor.</p>')
                res.end()
            }
            else{
            res.writeHead(200, {'Content-Type': 'text/html; charset=utf-8'})
            res.write(data)
            res.end()
            }
        })
    }
    else if(q.pathname == '/w3.css'){
        fs.readFile('mapa_site/w3.css', function(erro, data){
            res.writeHead(200, {'Content-Type': 'text/css'})
            res.write(data)
            res.end()
        })
    }
    else if (q.pathname == '/'){
        fs.readFile('mapa_site/index.html', function(erro, data){
            res.writeHead(200, {'Content-Type': 'text/html; charset=utf-8'})
            res.write(data)
            res.end()
        })
    }
    else{
        res.writeHead(400, {'Content-Type': 'text/html; charset=utf-8'})
        res.write('<p>Bad Request.</p>')
        res.end()
    }
}).listen(7777)