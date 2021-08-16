# EpiWrap

This is a wrapper for the epitech intranet 'api'

You can see here some examples:

````python
import epiwrap

client = epiwrap.EpiWrap("your token here")

user = client.getProfile()

print("Name: " + user.fullname + "\nCredits: " + str(user.credits))
````


## How to get your token ?

You must be connected to the [intranet](https://intra.epitech.eu/)

Now with the network tool (firefox "ctrl + shift + e", chrome "ctrl + shift + i" and then go in the network tab)
Click on the `/` request  
![img](images/network.png)  
Now go on the `cookies tab` and copy your user token (it should look like this)  
![img](images/cookie.png)  
Now you have your token, (don't forget that the cookie resets, so you have to change it when it's reset. Unfortunately I can't do anything to correct this)