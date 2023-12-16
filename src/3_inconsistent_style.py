class dataProcessor:
    def __init__(self, DataInput):
        self.dataInput = DataInput

    def ProcessData(self):
        processed_data = []
        for index, value in enumerate(self.dataInput):
            if index % 2 == 0:
                processed_data.append(value * 2)
            else:
                processed_data.append(value + 5)
        return processed_data

    def calculateStatistics(self, data):
        MeanValue = sum(data) / len(data)
        maxValue = max(data)
        return {"mean": MeanValue, "max": maxValue}

def analyzeDATA(data_set):
    processor = dataProcessor(data_set)
    processedData = processor.ProcessData()
    return processor.calculateStatistics(processedData)