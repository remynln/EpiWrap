# IMPORTANT:
This is a rewrite of Wrapitech with the new Oauth2 from the intra go check [here](https://github.com/Epiteks/Wrapitech)

##Usage
main route:
````html
https://etipech.eu/api
````

Info route ``/v1/infos``
````
arguments: 
  token *
````

Info route ``/v1/planning``
````
arguments: 
  token *
  start_time: format: year-month-day (optional)
  end_time: format: year-month-day (optional)
````

`*` = mendatory argument

## How to get your token ?

You must be connected to the [intranet](https://intra.epitech.eu/)

Now with the network tool (firefox "ctrl + shift + e", chrome "ctrl + shift + i" and then go in the network tab)
Click on the `/` request  
![img](images/network.png)  
Now go on the `cookies tab` and copy your user token (it should look like this)  
![img](images/cookie.png)  
Now you have your token, (don't forget that the cookie resets, so you have to change it when it's reset. Unfortunately I can't do anything to correct this)