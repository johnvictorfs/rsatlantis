module.exports = {
  devServer: {
    watchOptions: {
      poll: true
    }
  },
  productionSourceMap: false
};

if (process.env.NODE_ENV === 'production') {
  module.exports.outputDir = "../backend/dist/";
  module.exports.publicPath = "/static/";
}
