String formatting is a useful string method. The format method is udes to construct strings by inserting values into template strings. 

An example for generating log messages for a hypothetical web server.

log_message = "IP address {} accessed {} at {}".format(user_ip, url, now)

If the variables user_ip, url and now are defined then they will be substituted for the {} placeholder values:

>print(log_message)

IP address 208.94.117.90 accessed /bears/koala at 16:20

Any type can be passed into the format method, format will convert values into strings as needed.