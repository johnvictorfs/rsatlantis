const BundleTracker = require('webpack-bundle-tracker')

module.exports = {
  css: {
    loaderOptions: {
      scss: {
        data: '@import "@/scss/main.scss";'
      }
    }
  }
}

module.rules = {
  test: /\.styl(us)?$/,
  use: ['vue-style-loader', 'css-loader', 'stylus-loader']
}
