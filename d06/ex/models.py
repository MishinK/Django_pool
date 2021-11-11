from django.db import models
from django.contrib.auth.models import User


class UpVoteModel(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


class DownVoteModel(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


class TipModel(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    date = models.DateTimeField(auto_now_add=True)

    content = models.TextField(null=False)
	
    up_votes = models.ManyToManyField(UpVoteModel)
    down_votes = models.ManyToManyField(DownVoteModel)

    def upvote(self, user):
        try:
            down_vote: DownVoteModel = self.down_votes.get(author=user)
            down_vote.delete()
        except DownVoteModel.DoesNotExist:
            pass
        try:
            up_vote: UpVoteModel = self.up_votes.get(author=user)
            up_vote.delete()
        except UpVoteModel.DoesNotExist:
            up_vote = UpVoteModel(author=user)
            up_vote.save()
            self.up_votes.add(up_vote)
            self.save()

    def downvote(self, user):
        try:
            up_votes: UpVoteModel = self.up_votes.get(author=user)
            up_votes.delete()
        except UpVoteModel.DoesNotExist:
            pass
        try:
            down_vote: DownVoteModel = self.down_votes.get(author=user)
            down_vote.delete()
        except DownVoteModel.DoesNotExist:
            down_vote = DownVoteModel(author=user)
            down_vote.save()
            self.down_votes.add(down_vote)
            self.save()