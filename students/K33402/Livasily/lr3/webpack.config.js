const path = require("path")


module.exports = {
    entry: "./FlexAir3/frontend/src/index.js",
    output:{
        path:path.resolve(__dirname, "./FlexAir3/frontend/static/frontend"),
        filename: "main.js",
    },
    module:{
        rules:[
            {
                test: /\.js$/,
                exclude: /node_modules/,
                use:{
                    loader: "babel-loader"
                }
            }
        ]
    }
}