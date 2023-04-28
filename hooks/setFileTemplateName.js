module.exports = {
  'setFileTemplateName': (generator, hookArguments) => {
    let currentFilename = hookArguments.originalFilename;
    while (currentFilename.includes('-') || currentFilename.includes('.') || currentFilename.includes('/')){
      currentFilename = currentFilename.replace("-", "_").replace(".", "_").replace("/", "_");
    }
    return currentFilename;
  },
  'generate:before': (generator) => {
    const asyncapi = generator.asyncapi;
    for (let [key, value] of Object.entries(asyncapi.channels())){
      console.log(key);
      let newKey = key;
      while (newKey.includes('-') || newKey.includes('.') || newKey.includes('/')){
        newKey = newKey.replace("-", "_").replace(".", "_").replace("/", "_");
      }
      console.log(newKey);
      asyncapi._json.channels[newKey] = value;
      delete asyncapi._json.channels[key];
    }
    console.log(generator.asyncapi.channels());
  }
};
