from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError





class FriendshipRequestManager(models.Manager):
    
    # add, cancel, accept, reject
    
    def friend_add(self, from_user, to_user):
        FriendshipRequest.objects.create(from_user=from_user, to_user=to_user)
    
    def friend_cancel(self, from_user, to_user):
        FriendshipRequest.objects.filter(from_user=from_user, to_user=to_user).delete()

    def friend_accept(self, from_user, to_user):
        Friendship.objects.create(from_user=from_user, to_user=to_user)
        Friendship.objects.create(from_user=to_user, to_user=from_user)
        
        FriendshipRequest.objects.filter(from_user=from_user, to_user=to_user).delete()
        """ FriendshipRequest.objects.filter(from_user=to_user, to_user=from_user).delete() """
        
    def friend_reject(self, from_user, to_user):
        FriendshipRequest.objects.filter(from_user=from_user,to_user=to_user).delete()
        

        
    


class FriendshipRequest(models.Model):
    from_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="friendship_requset_sent")
    to_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="friendship_requests_received")
    
    objects = FriendshipRequestManager()
    
    class Meta:
        db_table = 'friendshiprequest_table'
        verbose_name = 'friendshiprequest'
        verbose_name_plural = 'friendshiprequests'
        
    



class FriendshipManager(models.Manager):
    
    # remove, is_friend
    
    def friend_remove(self, from_user, to_user):
        Friendship.objects.filter(from_user=from_user,to_user=to_user).delete()
        Friendship.objects.filter(from_user=to_user,to_user=from_user).delete()
         
    
class Friendship(models.Model):
    
    from_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="friendships_from")
    to_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="friendships_to")
    created_date = models.DateTimeField(auto_now_add=True)
    
    objects = FriendshipManager()
    
    class Meta:
        db_table = 'friendship_table'
        verbose_name = 'friendship'
        verbose_name_plural = 'friendships'


        
