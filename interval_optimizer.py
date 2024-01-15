import pandas as pd

def load_intervals(filename):
    return pd.read_csv(filename)

def optimize_intervals(intervals, importance_ratio):
    intervals = intervals.sort_values(by='Interval_end')
    n = len(intervals)
    
    dp = [0] * n
    picked_intervals = [[] for _ in range(n)]

    for i in range(n):
        dp[i] = intervals['Cost'][i]
        picked_intervals[i].append(i)

        for j in range(i):
            if intervals['Interval_end'][j] <= intervals['Interval_start'][i]:
                if dp[j] + intervals['Cost'][i] * importance_ratio < dp[i]:
                    dp[i] = dp[j] + intervals['Cost'][i] * importance_ratio
                    picked_intervals[i] = picked_intervals[j] + [i]

    best_combination = max(range(n), key=lambda x: dp[x])
    return picked_intervals[best_combination]

if __name__ == "__main__":
    filename = 'OptimizingIntervalCombinations_intervals.csv'
    importance_ratio = 0.5  # You can adjust this value to control the relative importance of both conditions

    intervals = load_intervals(filename)
    optimal_combination = optimize_intervals(intervals, importance_ratio)

    print("Optimal combination of intervals:")
    for index in optimal_combination:
        print(intervals.iloc[index])
