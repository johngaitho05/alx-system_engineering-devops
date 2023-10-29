# 0x09-web_infrastructure_design

## [0-simple_web_stack](0-simple_web_stack)
- A simple web stack with 1 server
- The server contains a web server (Nginx) which interacts with both the codebase (for static content) and application server (for dynamic content).
- The application server communicates the database to process the business logic and prepare dynamic content to be sent back to the client

![Simple Web Stack](https://res.cloudinary.com/da3jmmlpj/image/upload/v1698478767/ALX/Simple_web_stack_o9zwfp.jpg)

## [1-distributed_web_infrastructure](1-distributed_web_infrastructure)

- This design consists of 2 servers and a load balancer that distributes the traffic to the two servers evenly using the round-robin algorithm
- I used an active-active setup such that both servers are always active and waiting for requests. 
- The active-active setup ensures that the resources are well utilized and guarantees a lower turnaround time as opposed to active-passive since multiple requests can be processed concurrently

![Distributed web infrastructure](https://res.cloudinary.com/da3jmmlpj/image/upload/v1698478564/ALX/Distributed_web_infrastructure_vytoa8.jpg)

## [2-secured_and_monitored_web_infrastructure](2-secured_and_monitored_web_infrastructure)

- This design is an improved version of the distributed web infrastructure. 
- It adds an extra server and a firewall to control the traffic in and out of each server
- Additionally, the design ensures a secure connection via HTTPS and any insecure connections are terminated before reaching the server
- Each server is monitored by an external client to ensure everything's works as expected

![Secured and monitored web infrastructure](https://res.cloudinary.com/da3jmmlpj/image/upload/v1698481823/ALX/Secured_and_monitored_web_infrastructure_ro3jih.jpg)

## [3-scale_up](3-scale_up)

- This is an improvement of the secured and monitored web infrastructure
- The setup comprises 2 load balancers configured as a cluster. 
- One load balancer is always active and the other one is passive but standby to take over if the active one fails. Basically the load balancers have an active-passive setup
- The servers on the other end have an active-active setup.
- Each component is running on it's on server but is able to communicate with the other servers where other components are hosted

![Scale up](https://res.cloudinary.com/da3jmmlpj/image/upload/v1698566383/ALX/Scale_up_jbwkih.jpg)