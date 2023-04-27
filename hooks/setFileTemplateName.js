module.exports = {
  'setFileTemplateName': (generator, hookArguments) => {
    const currentFilename = hookArguments.originalFilename;
    return currentFilename.replace("-", "_").replace(".", "_");
  },
};
