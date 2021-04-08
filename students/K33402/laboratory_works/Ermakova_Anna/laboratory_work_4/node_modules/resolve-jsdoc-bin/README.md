# resolve-jsdoc-bin
resolve the jsdoc executable

[![Build Status](https://travis-ci.org/cdaringe/resolve-jsdoc-bin.svg?branch=master)](https://travis-ci.org/cdaringe/resolve-jsdoc-bin) [![Build status](https://ci.appveyor.com/api/projects/status/bb2lqlqi6mw7wl60/branch/master?svg=true)](https://ci.appveyor.com/project/cdaringe/resolve-jsdoc-bin/branch/master) [![Coverage Status](https://coveralls.io/repos/github/cdaringe/resolve-jsdoc-bin/badge.svg?branch=master)](https://coveralls.io/github/cdaringe/resolve-jsdoc-bin?branch=master) ![](https://img.shields.io/badge/standardjs-%E2%9C%93-brightgreen.svg)


## usage

```js
var jsdocResolve = require('resolve-jsdoc-bin')
var jsdocBinFilename = jdr.resolve(__dirname)
console.log(jsdocBinFilename) // <== /path/to/node_modules/.bin/jsdoc[.cmd]
```

windows, linux, osx--it's all good!
