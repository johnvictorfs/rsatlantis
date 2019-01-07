module.exports = {
  devServer: {
    watchOptions: {
      poll: true
    }
  },
};

if (process.env.NODE_ENV === 'production') {
  module.exports.outputDir = "../server/static/";
  module.exports.baseUrl = "./static/";
}
