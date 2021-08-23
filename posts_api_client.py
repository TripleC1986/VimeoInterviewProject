import requests
from configparser import ConfigParser
from pathlib import Path


def get_route_config(config_name: str):
    """
    Returns config property as a string from the configs.cfg file
    :param config_name:
    :return:
    """
    config_parser = ConfigParser()
    config_parser.read(str(Path("./configs.cfg")))
    return config_parser.get("routes", config_name)


class PostsApiClient:

    def __init__(self):
        self.session = requests.session()
        self.base_url = get_route_config("base_url")

    def get_post_by_id(self, post_id: int):
        """
        Executes a get request against the posts resource
        and a response object
        :param post_id:
        :return: A response object from the given call
        """
        route = self.base_url+"posts/{}".format(str(post_id))
        return self.session.get(route)

    def get_all_posts(self):
        """
        :return:  Executes a get request against the posts resource
        and returns a response object
        """
        return self.session.get(self.base_url+"posts")

    def create_a_post(self, post_data: dict):

        return self.session.post(self.base_url+"posts", data=post_data)



