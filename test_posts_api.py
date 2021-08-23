from posts_api_client import PostsApiClient
from deepdiff import DeepDiff


class TestPosts:
    def test_get_post_call(self):
        post_id = 1
        client = PostsApiClient()
        post_res = client.get_post_by_id(post_id)
        assert post_res.status_code == 200, f"Unsuccesful at retrieving post using the following id: {post_id}, here is " \
                                            f"the status code:{post_res.status_code} "
        post_data = post_res.json()
        res_post_id = post_data.get('id')
        assert res_post_id == post_id, f"The posts API did not return the correct post, expected:{post_id}, but got {res_post_id} "

    def test_check_post_title(self):
        post_id = 8
        expected_post_title = "dolorem dolore est ipsam"
        client = PostsApiClient()
        post_res = client.get_post_by_id(post_id)
        assert post_res.status_code == 200, f"Unsuccesful at retrieving post using the following id: {post_id}, here is " \
                                            f"the status code:{post_res.status_code} "
        post_data = post_res.json()
        post_title = post_data.get('title')
        assert post_title == expected_post_title, f"We expected the post title for post_id; {post_id} to be {expected_post_title}, but then got {post_title}"

    def test_check_title_or_body(self):
        exptected_count = 16
        text_to_verify = 'occaecati'
        client = PostsApiClient()
        all_posts = client.get_all_posts().json()

        filtered_posts = [x for x in all_posts if (text_to_verify in x.get('title') or text_to_verify in x.get('body'))]
        actual_post_count = len(filtered_posts)
        assert exptected_count == actual_post_count, f"""After checking for the following text {text_to_verify} 
        in post body and post title, we expected {exptected_count} as a count but found only {actual_post_count}"""

    def test_create_a_post(self):
        data = {
            'id': 1,
            'title': 'ad hoc post creation',
            'body': 'Hopefully doing a great job with this interview, lets get a job at the end of it.',
            'userId': 1
        }

        client = PostsApiClient()
        post_creation_resp = client.create_a_post(data)
        assert post_creation_resp.status_code == (
                201 or 200), f"The post was not created, we expected 200 series resp codes but got {post_creation_resp.status_code}"
        creation_resp_data = post_creation_resp.json()
        check_value = DeepDiff(data, creation_resp_data, ignore_order=True)
        boolean_check_value = bool(check_value)
        error_message = None
        if boolean_check_value is True:
            error_message = f"""There were differences between the request_payload and the response data returned from the post request.
            Please check the following dictionary for those chagnes {check_value}"""

        assert boolean_check_value is False, error_message
