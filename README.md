## GlyCulator2 restart utility
This script serves the purpose of restarting a shiny server.

#### Requirements:
+ python distribution. Version at least 2.5. Package was tested on python v3.7
+ pip distribution

#### Installation:
##### Linux
Copy paste and run this into your console:

> pip install git+https://github.com/kpagacz/glyculator-services.git@master

You might need to specify a --user flag, if you are not sudo:
> pip install --user git+https://github.com/kpagacz/glyculator-services.git@master

#### Running
The most simple is:
> glyculator-restart

##### Logging
The restart service is outputting a single text 
file called debug.log in the **working directory**. So make sure to create
a folder for it:
> mkdir glyculator-services

and then:
> cd glyculator-services  
glyculator-restart

Logs should be empty unless there was an error in the script
or the glyculator site was down.


