const BundleTracker = require('webpack-bundle-tracker')

module.exports = {
  publicPath: 'http://0.0.0.0:8080/',
  outputDir: '../backend/dist/',
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

    config.optimization
      .splitChunks(false)

    if (process.env.NODE_ENV === 'production') {
      // Django Static Files for production
      config
        .plugin('BundleTracker')
        .use(BundleTracker, [{ filename: '../backend/dist/webpack-stats-prod.json' }])
    } else {
      config
        .plugin('BundleTracker')
        .use(BundleTracker, [{ filename: '../backend/vue_frontend/webpack-stats.json' }])
    }

    config.resolve.alias
      .set('__STATIC__', 'static')

    config.devServer
      .public('http://0.0.0.0:8080')
      .host('0.0.0.0')
      .port(8080)
      .hotOnly(true)
      .watchOptions({ poll: 1000 })
      .https(false)
      .headers({ 'Access-Control-Allow-Origin': ['\*'] })
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
