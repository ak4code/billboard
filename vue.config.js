const {CleanWebpackPlugin} = require('clean-webpack-plugin');
const ManifestPlugin = require('webpack-manifest-plugin');

module.exports = {
    css: {
        extract: true
    },
    filenameHashing: false,
    configureWebpack: {
        plugins: [
            new CleanWebpackPlugin(),  // removes outdated assets from the output dir
            new ManifestPlugin.WebpackManifestPlugin(),  // generates the required manifest.json file
        ]
    },

    devServer: {
        port: 8080,
        allowedHosts: [
            '127.0.0.1:8000',
            '127.0.0.1'
        ],
        historyApiFallback: true,
        writeToDisk: true,
        headers: {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, PATCH, OPTIONS',
            'Access-Control-Allow-Headers': 'X-Requested-With, content-type, Authorization'
        }
    },

    runtimeCompiler: true
}