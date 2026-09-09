from django.db import models

# Create your models here.
def submission_code_path(instance, filename):
    #submissions/problem_45/user_12/filename
    return f"submissions/problem_{instance.problem.problem_id}/user_{instance.user.id}/{filename}"


class Submission(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name='submissions')
    problem = models.ForeignKey('problems.Problem', on_delete=models.CASCADE, related_name='submissions')

    source_code_path = models.FileField(upload_to=submission_code_path)
    lang = models.CharField(max_length=50)

    VERDICT_CHOICES = [
        ('Pending', 'Pending'),
        ('AC', 'Accepted'),
        ('WA', 'Wrong Answer'),
        ('TLE', 'Time Limit Exceeded'),
        ('MLE', 'Memory Limit Exceeded'),
        ('RE', 'Runtime Error'),
        ('CE', 'Compilation Error'),
    ]
    verdict = models.CharField(max_length=20, choices=VERDICT_CHOICES, default='Pending')
    max_time_ms = models.IntegerField(null=True, blank=True)
    max_memory_kb = models.IntegerField(null=True, blank=True)

    failed_testcase_sequence = models.IntegerField(null=True, blank=True)    
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Submission #{self.id} | User: {self.user} | Problem: {self.problem.problem_id} | {self.verdict}"


class SubmissionTestcase(models.Model):
    submission = models.ForeignKey(Submission, on_delete=models.CASCADE, related_name='testcase_results')
    testcase = models.ForeignKey('problems.TestCase', on_delete=models.CASCADE, related_name='submission_results')

    verdict = models.CharField(max_length=20, choices=Submission.VERDICT_CHOICES, default='Pending')
    execution_time_ms = models.IntegerField(null=True, blank=True)
    execution_mem_kb = models.IntegerField(null=True, blank=True)

    class Meta:
        ordering = ['testcase__sequence_number']

    def __str__(self):
        return f"Sub #{self.submission.id} | TC #{self.testcase.sequence_number} | {self.verdict}"