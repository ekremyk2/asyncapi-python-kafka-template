module.exports = {
  'setFileTemplateName': (generator, hookArguments) => {
    const currentFilename = hookArguments.originalFilename;
    return currentFilename.replaceAll("-", "_").replaceAll(".", "_").replaceAll("/", "_");
  },
};
