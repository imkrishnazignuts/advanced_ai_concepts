from presidio_analyzer import AnalyzerEngine
from presidio_anonymizer import AnonymizerEngine

analyzer = AnalyzerEngine()

results = analyzer.analyze(
    text="my name is krishna my mail is :krishna@gmail.com",
    language="en"
)

anonymizer = AnonymizerEngine()

result = anonymizer.anonymize(
    text="my name is krishna my mail is :krishna@gmail.com",
    analyzer_results=results
)

print(result.text)