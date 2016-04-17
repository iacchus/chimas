# Modular

Modular as much as possible.

The most simple use case is a forum that has only option to connect.
So maybe core has only the option to connect, even if there are no modules.

### Even Auth is an optional module

Can it be a case which a auth is not necessary? Yes, we can think of a guest/anonymous board for posting only.

BUT as this is a obviously rare case, auth module ships with the package.

# Namespaces

IF we have namespaces even for users we can later transform it in a federated bbs.

### Namespaces for modules

We should have namespaces even for modules. Special ids should be reserved for the core app.

Or we can reserve an namespace for the default apps too.

# Abstraction Layers

We should be aware that the main point of building this is doing it using good abstraction layers.

It is better to look for the horizon before building it, so that when we begin, it begins correctly.

# Extensibility

Extensibility should be done very naturally.

### Triggers

Triggesrs seem to be the most picky part of developing this.

# Database

Database will use namespaces, so we can reuse code.

# Development

It should be more centered in easy development and API exposition for developers.

# Other stuff

* It should be fun to extend. And also easy.
* It should be fun to run. (not much black magic to run and setup)
* It should be fun to use.
* It should be beautiful.
* Better if it works out-of-box with minimal setup.
* It should be easy to write clients.
