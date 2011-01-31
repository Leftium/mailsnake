import urllib2
import json

class MailSnake(object):
    def __init__(self, apikey = '', extra_params = {}):
        """
            Cache API key and address.
        """
        self.apikey = apikey

        self.default_params = {'apikey':apikey}
        self.default_params.update(extra_params)

        dc = 'us1'
        if '-' in self.apikey:
            dc = self.apikey.split('-')[1]
        self.base_api_url = 'https://%s.api.mailchimp.com/1.3/?method=' % dc

    def call(self, method, params = {}):
        url = self.base_api_url + method
        params.update(self.default_params)

        post_data = json.dumps(params)
        response = urllib2.urlopen(url, post_data)

        return json.loads(response.read())

    def __getattr__(self, method_name):

        def get(self, *args, **kwargs):
            params = dict((i,j) for (i,j) in enumerate(args))
            params.update(kwargs)
            return self.call(method_name, params)

        return get.__get__(self)

