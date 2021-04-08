'use strict'

var jdr = require('../')
var tape = require('tape')

tape('finds jsdoc', function (t) {
  var rootStarDir = jdr._isWin ? 'C:\\' : '/'
  t.ok(jdr.resolve(__dirname), 'finds jsdoc bin')
  t.throws(function () {
    jdr.resolve('bogus')
  }, 'throws on bogus start path')
  t.throws(function () { jdr.resolve(rootStarDir) }, 'throws on rootStarDir')
  t.end()
})
