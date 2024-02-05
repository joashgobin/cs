# Styles of APIs
APIs are the interface across which two applications can communicate with each other. 
An API determines the behaviour of the two applications and the means by which they exchange information.
Erik Wilde has a video:
!video{{https://youtu.be/bWFXGHXo_pY?si=iDv1Smv1cf6Ogzx4}}
in which he mentions five (5) styles of Application Programming Interfaces (APIs):
- Remote Procedure Call (RPC) (aka Tunnel)
- Resource
- Hypermedia
- Query
- Event-based

The design of an API is determined by the constraints the system has to perform under. 
The three (3) constraints are:
- the API consumer
- the API producer
- the AI scenario

Remember to design APIs based on these and avoid "if the only tool you have is a hammer, then every problem looks like a nail".

## Remote procedure call APIs/tunnel APIs
This is where the consumer calls functions within the producer.
An example of this is the Godot Game Engine's Multiplayer API. The host and clients can
make remote procedure calls to specific functions defined by the developer on each other's devices.

## Resource APIs
This is where the consumer accesses and interacts with resources exposed to it by the producer. The resources exposed can
be dependent on the authorization level of the consumer. An example is HTTP/OpenAPI where your browser asks for resources such
as web pages and images. Interactions are facilitated through the elements on the web pages.
This is the most popular form of API.

## Hypermedia APIs
This is where the consumer transforms data on the producer by interacting with resources. An example is the world-wide web (WWW)
where accessing a web page can cause another page to become available to you.

## Query APIs
This is where the consumer asks the producer for its data using a querying language. An example is MySQL.

## Event-based APIs
This is where an event on the producer (the publisher) is communicated to the consumer if the consumer has subscribed to that event. 
An example is Kafka.
