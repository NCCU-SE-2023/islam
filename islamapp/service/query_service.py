import networkx as nx
from flask import jsonify
from service.util import (
    _gen_error_response,
    INTERNAL_SERVER_ERROR,
    INVALID_INPUT_ERROR,
    NUMBER_EXCEEDED_ERROR,
)
from model.query import InvalidInputError, NumberExceededError, ResultNumberError
from model.data_models.user_followers import UserFollowers
from model.data_models.user_following import UserFollowing


def query(request):
    """
    body:
    {
      "result_num" : 3
      "accounts" : ["user1","user2","user3"]  (5 most)
    }
    return:
    {
      "accounts" : ["result1","result2"...]
    }
    """
    try:
        all_account = request.json.get("accounts")
        if len(all_account) > 5 or len(all_account) < 2:
            raise NumberExceededError(
                f"The number of accounts cannot exceed 5 or less than 2"
            )
        for account in all_account:
            userFollowers = UserFollowers.objects(scraped_ig_id=str(account))
            if userFollowers is None or len(userFollowers) == 0:
                raise InvalidInputError(f"account {account} not found")
        result_num = request.json.get("result_num")
        if result_num < 1:
            raise ResultNumberError(f"The number of results cannot be less than 1")
        accounts = {}
        i = 1
        for account in all_account:
            followers = UserFollowers.get_all_user_followers_by_ig_id(str(account))
            follower_lists = [obj.followers_list for obj in followers]
            following = UserFollowing.get_all_user_following_by_ig_id(str(account))
            following_lists = [obj.following_list for obj in following]
            accounts["account" + str(i)] = {
                "followers": follower_lists[0],
                "following": following_lists[0],
            }
            i += 1

        # 測試acc
        # accounts = {
        #     'account1':
        #     {
        #         'followers': [],
        #         'following': []
        #     },
        #     'account2':
        #     {
        #         'followers': [],
        #         'following': []
        #     },
        #     'account3':
        #     {
        #         'followers': [],
        #         'following': []
        #     }
        # }

        # 購建圖
        G = nx.Graph()
        for account, data in accounts.items():
            followers = data["followers"]
            following = data["following"]
            G.add_edges_from((follower, account) for follower in followers)
            G.add_edges_from((account, followee) for followee in following)

        # K-cores
        k_value = 1  # K=1，確保所有節點都被考慮
        k_cores = nx.k_core(G, k=k_value)

        # 找出前3名最有可能被所有acc都認識的acc
        candidate_scores = {}
        for node in k_cores:
            if node not in accounts.keys():  # 排除已知acc
                count = sum(
                    node in data["followers"] or node in data["following"]
                    for data in accounts.values()
                )
                candidate_scores[node] = count

        top_candidates = sorted(
            candidate_scores, key=candidate_scores.get, reverse=True
        )
        # if(len(top_candidates)>result_num):
        # top_candidates = top_candidates[1:result_num+1]
        output = [{name: candidate_scores[name]} for name in top_candidates]
        if len(output) > result_num:
            output = output[1 : result_num + 1]

        return jsonify(output), 201

    #   # print結果
    #   print("Top 3 candidates:")
    #   for candidate in top_candidates:
    #       print(candidate)
    except ResultNumberError as exception:
        return _gen_error_response(
            status_code=401,
            error_code=INVALID_INPUT_ERROR,
            message=f"ISLAM Exception: {str(exception)}",
        )
    except InvalidInputError as exception:
        return _gen_error_response(
            status_code=404,
            error_code=INVALID_INPUT_ERROR,
            message=f"ISLAM Exception: {str(exception)}",
        )
    except NumberExceededError as exception:
        return _gen_error_response(
            status_code=400,
            error_code=NUMBER_EXCEEDED_ERROR,
            message=f"ISLAM Exception: {str(exception)}",
        )
    except Exception as exception:
        return _gen_error_response(
            status_code=500,
            error_code=INTERNAL_SERVER_ERROR,
            message=f"ISLAM Exception: {str(exception)}",
        )


# query()
def get_account(request):
    """
    body:
    {
        "user_account" : "rice_to_islam"
    }
    return:
    {
        "accounts" : ["result1","result2"...]
    }
    """
    try:
        user_account = request.json.get("user_account")
        userFollowing = UserFollowing.objects(scraped_ig_id=str(user_account))
        if userFollowing is None or len(userFollowing) == 0:
            raise InvalidInputError(f"account {user_account} not found")
        scrape_user_list = [obj.following_list for obj in userFollowing]
        output = scrape_user_list[-1]
        return jsonify(output), 201
    except InvalidInputError as exception:
        return _gen_error_response(
            status_code=404,
            error_code=INVALID_INPUT_ERROR,
            message=f"ISLAM Exception: {str(exception)}",
        )
    except Exception as exception:
        return _gen_error_response(
            status_code=500,
            error_code=INTERNAL_SERVER_ERROR,
            message=f"ISLAM Exception: {str(exception)}",
        )
