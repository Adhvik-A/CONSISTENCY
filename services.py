class BattingConsistencyService:

    def __init__(self):
      
        self.p = 100   # mean runs
        self.q =  0 # standard deviation
        self.r = 0   # failure rate

    def calculate_bci(self):

       
        if self.p == 0:
            bci = 0
        else:
            relative_volatility = self.q / self.p
            stability = 1 - relative_volatility
            reliability = 1 - self.r

            bci = stability * reliability * 100

      
        if bci >= 70:
            label = "Highly Consistent"
        elif bci >= 50:
            label = "Consistent"
        elif bci >= 30:
            label = "Moderately Consistent"
        else:
            label = "Unstable"

        return {
            "mean_runs": self.p,
            "std_deviation": self.q,
            "failure_rate": self.r,
            "consistency_index": round(bci, 2),
            "consistency_label": label
        }
