import operator

def find_min(jobs):
    min_idx = 0
    for i in range(1, len(jobs)):
        if jobs[i][1] < jobs[min_idx][1]:
            min_idx = i
    return min_idx

def optimal_scheduling(jobs):
    jobs = sorted(jobs, key=operator.itemgetter(1))
    job_count = len(jobs)
    max_jobs = [0] * job_count
    for i in range(1, job_count):
        max_jobs[i] = max(max_jobs[i-1], max_jobs[i-2] + jobs[i][0])

    result = max_jobs[job_count-1]
    end_time = result
    count = 0

    for i in range(job_count-1, -1, -1):
        if end_time - jobs[i][0] >= 0:
            end_time -= jobs[i][0]
            result -= jobs[i][0]
            count += 1

    print(f"Maximum profit is {result}")
    print(f"Number of jobs performed is {count}")

if __name__ == "__main__":
    jobs = [(3, 10), (2, 19), (4, 23), (2, 27), (3, 30), (2, 40), (3, 50)]
    optimal_scheduling(jobs)