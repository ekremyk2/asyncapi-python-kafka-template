module.exports = {
  'setFileTemplateName': (generator, hookArguments) => {
    const currentFilename = hookArguments.originalFilename;
    while (currentFilename.includes('-') || currentFilename.includes('.') || currentFilename.includes('/')){
      currentFilename = currentFilename.replace("-", "_").replace(".", "_").replace("/", "_");
    }
    return currentFilename;
  },
};
