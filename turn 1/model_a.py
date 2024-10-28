import unittest
import time
from memory_profiler import memory_usage

import random
import string


def deduplicate_data(data):
    seen = set()
    deduplicated_data = []
    for item in data:
        if item not in seen:
            deduplicated_data.append(item)
            seen.add(item)
    return deduplicated_data


class TestDeduplicationPerformance(unittest.TestCase):

    def test_deduplication_performance(self):
        # Generate dummy data for testing
        data_size = 100000
        dummy_data = [''.join(random.choice(string.ascii_letters) for _ in range(random.randint(1, 20))) for _ in
                      range(data_size)]

        @memory_usage(max_usage=True)
        def measure_memory_usage():
            start_time = time.time()
            deduplicated_data = deduplicate_data(dummy_data)
            end_time = time.time()
            execution_time = end_time - start_time
            return execution_time, deduplicated_data

        execution_time, mem_usage = measure_memory_usage()

        # Set performance thresholds
        max_execution_time_threshold = 2.0  # seconds
        max_memory_usage_threshold = 100 * 1024 * 1024  # 100 MB in bytes

        self.assertLess(execution_time, max_execution_time_threshold,
                        f"Deduplication execution time exceeded threshold: {execution_time:.2f} seconds > {max_execution_time_threshold:.2f} seconds")

        self.assertLess(mem_usage, max_memory_usage_threshold,
                        f"Deduplication memory usage exceeded threshold: {mem_usage:.2f} bytes > {max_memory_usage_threshold:.2f} bytes")


if __name__ == '__main__':
    unittest.main()
