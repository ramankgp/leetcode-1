class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_counts = collections.Counter(tasks)
        max_freq = max(task_counts.values())
        num_max_freq_tasks = list(task_counts.values()).count(max_freq)
        min_itvs = (max_freq - 1) * (n + 1) + num_max_freq_tasks
        return min_itvs if len(task_counts) <= n + 1 else max(min_itvs, len(tasks))