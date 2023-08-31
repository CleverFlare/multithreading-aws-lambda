# A Multithreading Event Processing System with AWS Lambda Integration
This system basically accepts connections through sockets, then the connected client is able to stream event objects,
these objects are then handled through a multithreading client handler that uses a maximum of three threads concurrently,
while waiting for working threads to complete their task every other event object is stored in a Queue data structure,
each thread sends an HTTP Request to AWS API Gateway, which acts as the bridge connecting our system with the AWS Lambda
function, each AWS Lambda function then receives the event as an input, sleeps/waits 1 to 5 seconds randomly, and returns
the input that was passed to it.

## Summary
This system does the following:
1. connects to a multi-events server that streams event objects.
1. a multithreading event handler receives the streamed events individually.
1. the multithreading event handler stores the event objects in a thread-safe buffer, which is a Queue data structure.
1. the multithreading event handler sets a thread pool executor with a maximum of three concurrently working threads.
1. each thread sends an HTTP request payloaded with the event object to an AWS API Gateway which in turn sends it to the AWS Lambda function.
1. the AWS Lambda function sleeps/waits 1 to 5 seconds randomly before sending back the event object that it received as an input paramater.
