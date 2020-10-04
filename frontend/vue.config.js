module.exports = {
  css: {
    loaderOptions: {
      scss: {
        data: '@import "@/scss/main.scss";'
      }
    }
  },
  pluginOptions: {
    webpackBundleAnalyzer: {
      openAnalyzer: false
    }
  }
}

module.rules = {
  test: /\.styl(us)?$/,
  use: ['vue-style-loader', 'css-loader', 'stylus-loader']
}
