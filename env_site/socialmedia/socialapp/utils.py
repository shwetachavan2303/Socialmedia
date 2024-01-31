from socialapp.models import Post,likepost

def find_no_of_likes_received_by_user(user):
    post_id_of_user = user.post.all().values_list('id', flat=True)
    result = likepost.objects.filter(post_id__in=post_id_of_user).count()
    return result

