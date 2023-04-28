module.exports = {
  'setFileTemplateName': (generator, hookArguments) => {
    let currentFilename = hookArguments.originalFilename;
    while (currentFilename.includes('-') || currentFilename.includes('.') || currentFilename.includes('/')){
      currentFilename = currentFilename.replace("-", "_").replace(".", "_").replace("/", "_");
    }
    return currentFilename;
  },
  'generate:before': (a, b, c) => {
    console.log("generate:before", a, b, c)
  },
  'generate:after': (a, b, c) => {
    console.log("generate:after", a, b, c)
  }
};
