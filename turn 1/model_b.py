import unittest
import timeit
from memory_profiler import memory_usage
import random


def deduplicate_list(data_list):
    """
    Simple deduplication algorithm to remove duplicates from a list.
    """
    return list(set(data_list))


class TestDeduplicationPerformance(unittest.TestCase):
    def setUp(self):
        # Create a large dummy dataset with duplicate elements
        self.large_dataset = [random.randint(1, 1000000) for _ in range(1000000)]  # 1 million elements

    def test_deduplication_performance(self):
        """
        Performance test to measure deduplication algorithm's execution time and memory usage.
        """

        @memory_usage(max_usage=True)
        def memory_and_time_test():
            deduplicated_data = deduplicate_list(self.large_dataset)
            return deduplicated_data

        # Measure execution time
        start_time = timeit.default_timer()
        deduplicated_data = deduplicate_list(self.large_dataset)
        execution_time = timeit.default_timer() - start_time

        # Measure memory usage using memory_profiler
        memory_usage_in_mb = memory_and_time_test()

        # Set performance thresholds (adjust as needed based on your requirements)
        MAX_EXECUTION_TIME_SECONDS = 5  # Replace with actual expected threshold
        MAX_MEMORY_USAGE_MB = 100  # Replace with actual expected threshold

        # Assertions to check the performance
        self.assertLess(execution_time, MAX_EXECUTION_TIME_SECONDS, "Deduplication took too long to execute")
        self.assertLess(memory_usage_in_mb, MAX_MEMORY_USAGE_MB, "Deduplication used too much memory")
        print(f"Deduplication completed in {execution_time:.4f} seconds and used {memory_usage_in_mb:.2f} MB of memory")


if __name__ == '__main__':
    unittest.main()
