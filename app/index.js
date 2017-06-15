const express = require('express')
const pythonshell = require('python-shell')
let app = express()

app.get('/', function(req, res) {
  pythonshell.run('my_script.py', function (err) {
    if (err) throw err;
    console.log('finished');
  });
  res.send('finished')
})

app.listen(3000, function () {
  console.log('Example app listening on port 3000!')
})
