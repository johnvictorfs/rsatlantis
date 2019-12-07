module.exports = {
  css: {
    loaderOptions: {
      scss: {
        data: '@import "@/scss/main.scss";'
      }
    }
  },
  devServer: {
    watchOptions: {
      poll: true
    }
  },
  productionSourceMap: false,
  chainWebpack(config) {
    config.module.rule('md')
      .test(/\.md/)
      .use('vue-loader')
      .loader('vue-loader')
      .end()
      .use('vue-markdown-loader')
      .loader('vue-markdown-loader/lib/markdown-compiler')
      .options({
        raw: true
      })
  }
}

module.rules = {
  test: /\.styl(us)?$/,
  use: ['vue-style-loader', 'css-loader', 'stylus-loader']
}

if (process.env.NODE_ENV === 'production') {
  module.exports.outputDir = '../backend/dist/'
  module.exports.publicPath = '/static/'
}
