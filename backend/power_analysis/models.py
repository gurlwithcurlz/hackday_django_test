from django.db import models
import numpy as np
from scipy.stats import norm, ttest_ind, ttest_ind_from_stats


def binomial_std(n, p):
    """Calculate the standard deviation of the sample i.e. sqrt( var(X/n) ) or standard error."""
    return np.sqrt(p*(1 - p)/n)


# Create your models here.
class PowerAnalysis(models.Model):
    base_conversion = models.FloatField()
    a_grade_proportion = models.FloatField()
    uplift = models.FloatField()
    days_max = models.IntegerField()
    calls_per_day = models.IntegerField()

    def calculate_power_analysis(self):
        avg_conversion = self.base_conversion
        A_conversion = self.base_conversion * (1 + self.uplift)

        n_non_A = self.calls_per_day * (1 - self.a_grade_proportion)
        n_A = self.calls_per_day * self.a_grade_proportion

        days_list = range(2, self.days_max)
        confidence = []
        nAs_sig = []
        p_sig = [0.80, 0.85, 0.90, 0.95, 0.99]
        for days in days_list:
            t, p = ttest_ind_from_stats(
                avg_conversion, binomial_std(n_non_A, avg_conversion), days * n_non_A,
                A_conversion, binomial_std(n_A, A_conversion), days * n_A,
                equal_var=False
            )

            confidence.append(1 - p)
            nAs_sig.append(n_A * days)

        first_day = np.array(days_list)[np.where(np.array(confidence)>=0.95)][0]
        nAs_firstday = np.array(nAs_sig)[np.where(np.array(confidence)>=0.95)][0]

        return first_day, nAs_firstday
