# twitter-realtime-update

A python bot that will update your display name with number of followers you are having currently and bio with most recent new user that followed you

## 🖼 Demo

![](assets/demo.png) <br>
You can visit [my twitter profile](https://twitter.com/chotathanos) to see the app in action 🐦 <br>
The app triggers after every 30 sec so you should have a patience of atleast 30 SEC 😂
<br><br>

## ⚙️ Steps to implement this in your own twitter profile

1. ⬇️ Clone the repo

```sh
$ git clone https://github.com/ponder2000/twitter-realtime-update.git
$ cd twitter-realtime-update
```

2. 🔑 Get the `AUTH KEYS` for your app from your [twitter developer account](https://developer.twitter.com) and update it with values in `details.py`

3. ✅ Make sure your display name has `space` seperated and bio is `|` seperated as explained in comments of `main.py`

4. 🏃🏻‍♂️ Run the following command

```sh
$ python main.py
```

And it is up and running 😁 <br>
For realtime updates deploy it. I used heroku<br>
