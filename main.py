import tweepy as tw
import time
import details


class TweeterBot:
    def __init__(self):
        api_key = details.API_KEY
        api_secret = details.API_KEY_SECRET
        access_token = details.ACCESS_TOKEN
        access_token_secret = details.ACCESS_TOKEN_SECRET

        auth = tw.OAuthHandler(api_key, api_secret)
        auth.set_access_token(access_token, access_token_secret)
        self.api = tw.API(auth, wait_on_rate_limit=True,
                          wait_on_rate_limit_notify=True)

    def _followersCount(self) -> str:
        """
        retruns number of followers the account has
        """
        return str(self.api.me().followers_count).strip()

    def _getDisplayName(self):
        """ 
        Display Name should be always in the format of "Space seperated your initial name and at the end we will add the count"
        last thing will be the count 

        eg my display Name was "Jay Saha | count = 0
        so the 0 at the end will be updated with number of followers
        """
        display_name = self.api.me().name.split()
        suffix_display_name = display_name[-1]
        display_name = display_name[:-1]
        prefix_display_name = ""
        for elm in display_name:
            prefix_display_name += f"{elm} "
        return prefix_display_name, suffix_display_name.strip()

    def _getBio(self):
        """
        return bio in map of static nd change required data
        the last part of bio sould be "|something=Display Name of other user" 
        spliting character used is '|' you can change it with ur intrest of delemetor

        eg my bio is
        "Chegg Expert | AI/ML🤖 | Flutter💙 | Indian🇮🇳 | last_follower= this_string_will_be_updated"
        """
        bio = self.api.me().description
        bio = bio.split('|')
        suffix_bio = bio[-1]
        bio = bio[:-1]
        prefix_bio = ""
        for elm in bio:
            prefix_bio += f"{elm}|"
        return prefix_bio, suffix_bio

    def _getRecentFollowers(self, initialLength):
        """
        returns username of recent follower and if it is too big then remove just the maximum that can be holded
        """
        followersObj = self.api.me().followers()
        followers = [f for f in followersObj]
        result = None
        try:
            _userName = str(followers[0].screen_name)
            if len(' @' + _userName) < (100 - initialLength):
                result = ' @' + _userName
            else:
                result = ' ' + _userName[:(100 - (initialLength + 1))]
        except:
            result = "Opps error"
        return result

    def updatedBio(self):
        """
        returns the new updated bio
        """
        prefix_bio, sufix_bio = self._getBio()
        identifier, _ = sufix_bio.split('=')
        initial_bio_length = len(prefix_bio + identifier) + 1
        recentFollower = self._getRecentFollowers(initial_bio_length)
        sufix_bio = identifier + '=' + recentFollower
        return prefix_bio + sufix_bio

    def updateProfile(self):
        """
        updates displayName and bio if needed to
        """
        name, oldCount = self._getDisplayName()
        newCount = self._followersCount()

        if newCount != oldCount:
            newBio = self.updatedBio()
            newName = name + newCount
            self.api.update_profile(name=newName, description=newBio)
            print("---> Updated Dislplay Name to:", newName)
            print("---> Updated Bio to:", newBio)
        else:
            print(" :: Nothing changed!")


def main():
    bot = TweeterBot()
    while True:
        try:
            bot.updateProfile()
            time.sleep(details.SLEEP_TIME)
        except Exception as e:
            print("Error in main :: ", e)
            break


if __name__ == '__main__':
    print("Bot running ..")
    main()
