# Python Confluent Kafka Template

This template generates a Python application with a Confluent Kafka client based on the AsyncAPI specification file as an input.

# Technical Requirements

- 0.50.0 =< [Generator](https://github.com/asyncapi/generator/) < 2.0.0,
- Generator specific [requirements](https://github.com/asyncapi/generator/#requirements)

# How to use the template

This template must be used with the AsyncAPI Generator. You can find all available options [here](https://github.com/asyncapi/generator/)

> You can find a complete tutorial on AsyncAPI Generator using this template [here](https://www.asyncapi.com/docs/tutorials/streetlights)

#### CLI

```bash
# Install the AsyncAPI Generator
$ npm install -g @asyncapi/generator

# Run the generator with this template
$ ag https://bit.ly/asyncapi @ekremyk2/python-confluent-kafka-template -o output
```