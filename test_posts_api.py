from posts_api_client import PostsApiClient


def test_get_post_call():
    post_id = 1
    client = PostsApiClient()
    post_res = client.get_post_by_id(post_id)
    assert post_res.status_code == 200, f"Unsuccesful at retrieving post using the following id: {post_id}, here is " \
                                        f"the status code:{post_res.status_code} "
    post_data = post_res.json()
    res_post_id = post_data.get('id')
    assert res_post_id == post_id, f"The posts API did not return the correct post, expected:{post_id}, but got {res_post_id} "


