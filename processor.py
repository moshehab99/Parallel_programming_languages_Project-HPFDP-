from strategies import (
    SequentialProcessingStrategy,
    ParallelProcessingStrategy
)


class DataProcessor:

    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def execute(self, file_path):
        return self.strategy.process(file_path)



def start_sequential_processing(file_path):
    processor = DataProcessor(
        SequentialProcessingStrategy()
    )

    return processor.execute(file_path)



def start_parallel_processing(file_path):
    processor = DataProcessor(
        ParallelProcessingStrategy()
    )

    return processor.execute(file_path)