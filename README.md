# MedaReda 
## Medium data Real time analyitics

# MySite
Docker containers can be used to provide the infrastructure required to supply the parallel computing power to deliver medium data real time data analytics.

Micro services hosted in Docker containers are used to get real time market data and publish it to to a cloud based message bus. Additional Docker services subscribe to the bus, then using dataflow programming, recalculate the output and publish the value back on the bus. I am then using more micro services to read the values and pump the results into web pages using web sockets.

This provides a scalable solution to providing real time data analytics for medium data.

## MedaReda Architecture
![Alt text](/MedaRedaArch.jpg?raw=true "MedaReda Architecture")


##A video of an example working demo

<a href="http://www.youtube.com/watch?feature=player_embedded&v=QW_b3DqW17M
" target="_blank"><img src="http://img.youtube.com/vi/QW_b3DqW17M/0.jpg" 
alt="IMAGE ALT TEXT HERE" width="960" height="720" border="10" /></a>

[Flask-User-starter-app](https://github.com/lingthio/Flask-User-starter-app) was used as one of the starting points for this code repository.
