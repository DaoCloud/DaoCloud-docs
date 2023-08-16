const { defineConfig } = require('@vue/cli-service');
const { name } = require('./package.json');

module.exports = defineConfig({
  publicPath: process.env.VUE_APP_PUBLIC_BASE_PATH,
  transpileDependencies: true,

  configureWebpack: {
    output: {
      // 把子应用打包成 umd 库格式
      library: `${name}-[name]`,
      libraryTarget: 'umd',
      // chunkLoadingGlobal output.jsonpFunction -> output.chunkLoadingGlobal
      // https://github.com/webpack/webpack.js.org/issues/3940
      chunkLoadingGlobal: `webpackJsonp_${name}`,
    },
  },

  devServer: {
    port: 8000,
    headers: {
      'Access-Control-Allow-Origin': '*',
    },
  },
});
