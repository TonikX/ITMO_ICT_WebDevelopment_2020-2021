/**
 * @module resolve-jsdoc-bin
 * @description enables a user to resolve the path to the jsdoc binary, cross-platform
 */

'use strict'

var os = require('os')
var path = require('path')
var fs = require('fs')

module.exports = {
  /**
   * @property _isWin
   * @type boolean
   * @description indicates if platform is windows*
   */
  _isWin: /^win/.test(os.platform()),

  /**
   * Locates the JSDoc executable command.  Since a module is not provided,
   * `require.resolve('jsdoc')` does not work and must be done manually.
   * @ref https://github.com/mrjoelkemp/jsdoc3-parser/pull/9/files code borrowed and
   * robustified from this original PR
   * @param {string}  dir The starting directory to search.
   * @return {string} The executable path, or null if not found.
   */
  resolve: function resolve (dir) {
    /* istanbul ignore next */
    var executable = 'jsdoc' + (this._isWin ? '.cmd' : '')
    var cmd
    dir = path.resolve(dir)
    try {
      fs.statSync(dir)
    } catch (err) {
      throw new Error('initial start directory ' + dir + ' not found')
    }
    while (dir) {
      try {
        cmd = path.join(dir, 'node_modules', '.bin', executable)
        // End the search if the command is found.
        // If not found, an exception is thrown.
        fs.statSync(cmd)
        break
      } catch (err) {
        cmd = null
        if (path.dirname(dir) === dir) {
          throw new Error('unable to find jsdoc executable: ' + executable)
        } else {
          dir = path.resolve(path.dirname(dir))
        }
      }
    }
    return cmd
  }
}
