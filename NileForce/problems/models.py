from django.db import models

def testcase_input_path(instance, filename):
    return f"testcases/problem_{instance.problem.problem_id}/inputs/{filename}"

def testcase_output_path(instance, filename):
    return f"testcases/problem_{instance.problem.problem_id}/outputs/{filename}"

class Problem(models.Model):
    author = models.ForeignKey(
        'accounts.User', 
        on_delete=models.CASCADE, 
        related_name='problems'
    )
    title = models.CharField(max_length=255)
    statement = models.TextField()
    inputs_format = models.TextField()
    output_format = models.TextField()
    constraints_text = models.TextField()
    time_limit_ms = models.FloatField()
    memory_limit_mb = models.IntegerField()
    CHECKER_CHOICES = [
        ('standard', 'Standard Token Matcher'),
        ('custom', 'Custom Checker'),
    ]
    checker_type = models.CharField(max_length=50, choices=CHECKER_CHOICES, default='standard')
    
    checker_file_path = models.FileField(upload_to='checkers/', null=True, blank=True)
    checker_lang = models.CharField(max_length=50, null=True, blank=True, help_text="e.g., cpp, python")
    
    difficulty_status = models.CharField(max_length=50, null=True, blank=True) 
    
    is_visible = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.problem_id} - {self.title}"

    class Meta:
        ordering = ['-created_at']


class TestCase(models.Model):
    problem = models.ForeignKey(
        Problem, 
        on_delete=models.CASCADE, 
        related_name='testcases'
    )
    
    sequence_number = models.IntegerField()
    
    input_file_path = models.FileField(upload_to=testcase_input_path)
    output_file_path = models.FileField(upload_to=testcase_output_path)

    is_sample = models.BooleanField(default=False)

    def __str__(self):
        sample_tag = " (Sample)" if self.is_sample else ""
        return f"Test Case #{self.sequence_number} for Problem {self.problem.problem_id}{sample_tag}"

    class Meta:
        unique_together = ['problem', 'sequence_number']
        ordering = ['problem', 'sequence_number']