import json, csv

INPUT_FILE = "example_annotations.json"
OUTPUT_FILE_JSON = "output.json"
OUTPUT_FILE_CSV = "output.csv"

lines = []
with open(INPUT_FILE, 'r') as f:
	for line in f:
		lines.append(json.loads(line.strip()))

with open(OUTPUT_FILE_JSON, 'w') as f:
	json.dump(lines, f)

with open(OUTPUT_FILE_CSV, 'w', newline='') as f:
	writer = csv.writer(f)
	max_mentions = max([len(line['mentions']) for line in lines])
	writer.writerow(('doc_idx', 'tokens', *['mention_%d' % (i + 1) for i in range(max_mentions)])) # headings
	for line in lines:
		tokens = line['tokens']
		mentions = []
		for m in line['mentions']:
			start = m['start']
			end = m['end']
			labels = m['labels']
			mentions.append((start, end, " ".join(tokens[start:end]), labels))

		writer.writerow((line['doc_idx'], " ".join(tokens), *mentions))
