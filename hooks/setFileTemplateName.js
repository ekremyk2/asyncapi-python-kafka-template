module.exports = {
  "generate:before": (generator) => {
    const asyncapi = generator.asyncapi;
    for (let [key, value] of Object.entries(asyncapi.channels())) {
      console.log(key, value);
      let newKey = key;
      while (
        newKey.includes("-") ||
        newKey.includes(".") ||
        newKey.includes("/")
      ) {
        newKey = newKey.replace("-", "_").replace(".", "_").replace("/", "_");
      }
      asyncapi._json.channels[newKey] = asyncapi._json.channels[key];
      delete asyncapi._json.channels[key];
      console.log(newKey, asyncapi._json.channels[newKey]);
    }
    console.log(generator.asyncapi.channels());
  },
};
