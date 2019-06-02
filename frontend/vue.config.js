module.exports = {
  devServer: {
    watchOptions: {
      poll: true
    }
  },
  productionSourceMap: false
};

module.rules = {
  test: /\.styl(us)?$/,
  use: ['vue-style-loader', 'css-loader', 'stylus-loader']
};

if (process.env.NODE_ENV === 'production') {
  module.exports.outputDir = '../backend/dist/';
  module.exports.publicPath = '/static/';
}
